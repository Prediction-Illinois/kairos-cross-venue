"""Build the daily Kalshi × Polymarket report from Kairos data.

    python report.py --archive archive/pairs.jsonl.gz --out reports

The report has four parts:

1. Pairs: Kairos's matched-market catalog, with outcomes lined up by
   oracle3-extras.
2. Gaps today: pairs whose prices break P(A) = P(B) after both venues' fees,
   checked against the order books.
3. Gaps around game time: the two venues' last trades in the same minute
   (Kairos candles), for games that started 6 to 30 hours before the report.
4. Settlement: whether both venues paid out the same way (Kairos resolutions),
   for games that started in the last seven days.

Parts 3 and 4 read the pair archive that `oracle3-extras kairos snapshot`
keeps, because Kairos drops a pair from its catalog once the markets expire.
Only aggregate statistics, charts and a few example rows are published.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt  # noqa: E402
from oracle3_extras.arbitrage import scan_relations  # noqa: E402
from oracle3_extras.market.archive import load_archive, started_between  # noqa: E402
from oracle3_extras.market.kairos import (  # noqa: E402
    check_settlements,
    history_summary,
    kairos_relations,
    price_history,
    settlement_summary,
)

#: Pairs need this many minutes traded on both venues to be listed as widest.
WIDEST_MIN_MINUTES = 10

README_START = '<!-- report:start -->'
README_END = '<!-- report:end -->'

LEAGUES = {
    'NCAAF': 'College football',
    'NFL': 'NFL',
    'NBA': 'NBA',
    'WNBA': 'WNBA',
    'NHL': 'NHL',
    'AHL': 'AHL',
    'KHL': 'KHL',
    'MLB': 'MLB',
    'KBO': 'KBO',
    'NPB': 'NPB',
    'MLS': 'MLS',
    'USL': 'USL',
    'EPL': 'Premier League',
    'LALIGA': 'La Liga',
    'SERIEA': 'Serie A',
    'LIGUE1': 'Ligue 1',
    'BUNDESLIGA': 'Bundesliga',
    'UCL': 'Champions League',
    'UEL': 'Europa League',
    'UECL': 'Conference League',
    'LIGAMX': 'Liga MX',
    'BRASILEIRO': 'Brasileirão',
    'ATP': 'ATP',
    'ATPCHALLENGER': 'ATP Challenger',
    'WTA': 'WTA',
    'WTACHALLENGER': 'WTA 125',
    'ITF': 'ITF men',
    'ITFW': 'ITF women',
}


def league(ticker: str) -> str:
    """Readable league name from a Kalshi series ticker (KXNCAAFTOTAL -> College football)."""
    code = re.sub(r'^KX', '', ticker.split('-')[0])
    code = re.sub(r'(GAME|TOTAL|MATCH|SPREAD)$', '', code)
    return LEAGUES.get(code, code.title())


def cents(value: float | None) -> str:
    return '–' if value is None else f'{value * 100:.0f}¢'


def percent(value: float | None) -> str:
    return '–' if value is None else f'{value * 100:.0f}%'


async def collect(archive: Path, now: datetime) -> dict[str, Any]:
    catalog = await kairos_relations()
    scan = await scan_relations(catalog.relations)
    archived = load_archive(archive) if archive.exists() else []
    recent = started_between(archived, now - timedelta(hours=30), now - timedelta(hours=6))
    histories = await price_history(recent, now=now)
    enough = [h for h in histories if len(h.points) >= WIDEST_MIN_MINUTES]
    widest = sorted(enough, key=lambda h: max(abs(g) for g in h.gaps), reverse=True)[:5]
    week = started_between(archived, now - timedelta(days=7), now - timedelta(hours=6))
    checks = await check_settlements(week)
    leagues = Counter(league(r.market_a['market_id']) for r in catalog.relations)
    return {
        'generated_at': now.isoformat(timespec='seconds'),
        'catalog': catalog.summary(),
        'leagues': dict(leagues.most_common()),
        'scan': scan.to_dict(top=5),
        'history': {**history_summary(histories, widest=0), 'widest': [h.summary() for h in widest]},
        'settlement': settlement_summary(checks),
        'archive_pairs': len(archived),
    }


def draw(data: dict[str, Any], img: Path) -> None:
    img.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})

    leagues = list(data['leagues'].items())[:12][::-1]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.barh([name for name, _ in leagues], [n for _, n in leagues], color='#3b6ea5')
    ax.set_xlabel('Kalshi–Polymarket pairs lined up today')
    ax.set_title('Pairs by league (Kairos catalog)', loc='left')
    fig.tight_layout()
    fig.savefig(img / 'pairs-by-league.png', dpi=150)
    plt.close(fig)

    bins = data['history']['by_minutes_from_start']
    centers = [(b['from'] + b['to']) / 2 for b in bins]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(centers, [b['minutes'] for b in bins], width=26, color='#d9e2ec', label='minutes compared')
    ax.set_ylabel('minutes compared')
    ax.set_xlabel('minutes from the start of the game')
    twin = ax.twinx()
    twin.spines['top'].set_visible(False)
    for key, style, label in (('median_abs_gap', '-', 'median gap'), ('p90_abs_gap', '--', '90th percentile')):
        points = [(c, b[key] * 100) for c, b in zip(centers, bins, strict=True) if b[key] is not None]
        if points:
            twin.plot(*zip(*points, strict=True), style, color='#b23b3b', marker='o', label=label)
    twin.set_ylabel('gap between last trades (cents)')
    twin.set_ylim(bottom=0)
    ax.axvline(0, color='#888888', linewidth=1)
    twin.legend(loc='upper left', frameon=False)
    ax.set_title('Kalshi vs Polymarket last-trade gap around game time', loc='left')
    fig.tight_layout()
    fig.savefig(img / 'gap-by-minute.png', dpi=150)
    plt.close(fig)


def markdown(data: dict[str, Any], day: str, *, charts: bool = True) -> str:
    cat, scan, hist, sett = data['catalog'], data['scan'], data['history'], data['settlement']
    s = scan['summary']
    lines = [
        f'# Cross-venue report, {day}',
        '',
        f"Generated {data['generated_at'][:16].replace('T', ' ')} UTC from Kairos's matched-market "
        "catalog and Market Data API, and Kalshi's and Polymarket's public APIs.",
        '',
        '## Pairs',
        '',
        f"Kairos listed {cat['kalshi_polymarket']:,} Kalshi–Polymarket pairs; "
        f"{cat['aligned']:,} were lined up ({percent(cat['aligned'] / cat['kalshi_polymarket'] if cat['kalshi_polymarket'] else None)}), "
        f"{cat['with_warnings']} of them with a warning such as a postponed game.",
        '',
        *(['![Pairs by league](img/pairs-by-league.png)', ''] if charts else []),
        '| Not lined up | Pairs |',
        '|---|---|',
        *[f'| {reason} | {n} |' for reason, n in cat['rejected'].items()],
        '',
        '## Gaps today',
        '',
        '| | Pairs |',
        '|---|---|',
        f"| Quoted | {s['quoted']:,} |",
        f"| Break P(A) = P(B) before fees | {s['violated_before_fees']} |",
        f"| Edge after both venues' fees, top of the book | {s['profitable_after_fees_top_of_book']} |",
        f"| Edge left after walking the order books | {s['opportunities']} |",
        '',
    ]
    if scan['opportunities']:
        lines += [
            '| Kalshi market (A) | Polymarket market (B) | Basket | Contracts | Net edge |',
            '|---|---|---|---|---|',
        ]
        for o in scan['opportunities']:
            d = o['depth'] or {}
            lines.append(
                f"| {o['market_a']['name']} | {o['market_b']['name']} | {o['basket']} | "
                f"{d.get('contracts', '–')} | ${d.get('net_edge', 0):.4f} |"
            )
        lines.append('')
    lines += [
        'Most gaps that show at the top of the book disappear after fees or in the order books.',
        '',
        '## Gaps around game time',
        '',
    ]
    if hist['minutes']:
        lines += [
            f"Games that started 6 to 30 hours ago: {hist['pairs_with_overlap']} of {hist['pairs']} pairs "
            f"traded on both venues in the same minute, {hist['minutes']:,} minutes in all. "
            f"The median gap between the two last trades was {cents(hist['median_abs_gap'])} and the "
            f"90th percentile {cents(hist['p90_abs_gap'])}; before the start the 90th percentile was "
            f"{cents(hist['before_start']['p90_abs_gap'])}.",
            '',
            *(['![Gap around game time](img/gap-by-minute.png)', ''] if charts else []),
            f'| Widest gaps (at least {WIDEST_MIN_MINUTES} minutes compared) | Median | Largest | Minutes compared |',
            '|---|---|---|---|',
            *[
                f"| {w['polymarket']} | {cents(w['median_abs_gap'])} | {cents(w['max_abs_gap'])} | {w['minutes']} |"
                for w in hist['widest']
            ],
            '',
            'These are trade prices up to a minute apart, not quotes: a gap shows the venues '
            'disagreeing, not an arbitrage that could have been executed.',
            '',
        ]
    else:
        lines += ['No archived games started 6 to 30 hours ago yet; the archive is still filling.', '']
    lines += ['## Settlement', '']
    if sett['settled']:
        lines += [
            f"Games that started in the last seven days: {sett['settled']} pairs have settled on both "
            f"venues and {sett['agree']} settled the same way ({percent(sett['agreement_rate'])}); "
            f"{sett['pending']} are still settling.",
            '',
        ]
        if sett['mismatches']:
            lines += ['| Kalshi market | Polymarket market | Kalshi YES paid | Polymarket first outcome paid |', '|---|---|---|---|']
            for m in sett['mismatches'][:10]:
                lines.append(
                    f"| {m['kalshi_market']} | {m['polymarket_market']} | "
                    f"{m['kalshi_yes_paid']} | {m['polymarket_first_outcome_paid']} |"
                )
            lines.append('')
    else:
        lines += ['No archived pairs have settled yet; the archive is still filling.', '']
    lines += [
        '## Method',
        '',
        '- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) '
        'checks each one on both venues and decides which Polymarket outcome pays when Kalshi YES pays.',
        "- Gaps today use each venue's published fee schedule (oracle3) and the live order books.",
        '- Gaps around game time use Kairos one-minute candles; settlement uses Kairos `/v1/resolutions`.',
        '- Only aggregates and a few example rows are published here.',
        '',
    ]
    return '\n'.join(lines)


def readme_block(data: dict[str, Any], day: str) -> str:
    cat, s, hist, sett = data['catalog'], data['scan']['summary'], data['history'], data['settlement']
    rows = [
        f'**Latest report: [{day}](reports/latest.md)**',
        '',
        '| | |',
        '|---|---|',
        f"| Kalshi–Polymarket pairs lined up | {cat['aligned']:,} of {cat['kalshi_polymarket']:,} |",
        f"| Edge after fees, after the order books | {s['opportunities']} of {s['quoted']:,} pairs |",
        f"| Median last-trade gap, games 6–30 h ago | {cents(hist['median_abs_gap'])} over {hist['minutes']:,} minutes |",
        f"| Settled the same way, last 7 days | {sett['agree']} of {sett['settled']} |",
        '',
        '![Gap around game time](reports/img/gap-by-minute.png)',
    ]
    return '\n'.join(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--out', type=Path, default=Path('reports'))
    parser.add_argument('--readme', type=Path, default=Path('README.md'))
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    day = now.date().isoformat()
    data = asyncio.run(collect(args.archive, now))

    args.out.mkdir(parents=True, exist_ok=True)
    draw(data, args.out / 'img')
    # Dated reports keep the numbers; only the latest report carries charts,
    # so the repository does not grow by two images a day.
    (args.out / f'{day}.md').write_text(markdown(data, day, charts=False))
    (args.out / 'latest.md').write_text(markdown(data, day))
    summaries = args.out / 'data'
    summaries.mkdir(exist_ok=True)
    (summaries / f'{day}.json').write_text(json.dumps(data, indent=2, default=str))

    if args.readme.exists():
        readme = args.readme.read_text()
        if README_START in readme and README_END in readme:
            head, rest = readme.split(README_START, 1)
            _, tail = rest.split(README_END, 1)
            block = readme_block(data, day)
            args.readme.write_text(f'{head}{README_START}\n{block}\n{README_END}{tail}')
    print(json.dumps({
        'day': day,
        'aligned': data['catalog']['aligned'],
        'opportunities': data['scan']['summary']['opportunities'],
        'history_minutes': data['history']['minutes'],
        'settled': data['settlement']['settled'],
        'agree': data['settlement']['agree'],
    }))


if __name__ == '__main__':
    main()
