"""Build the daily Kairos cross-venue report, by Prediction@Illinois's six market divisions.

    python report.py --archive archive/pairs.jsonl.gz --out reports

Kairos (https://kairos.trade) matches the same market across Kalshi,
Polymarket, Predict.fun and Hyperliquid. The report covers every pair it lists,
sorted into the club's six divisions by Kairos's own categories:

1. Overview: one line per division.
2. Pairs: what Kairos matched, by division and venue pair.
3. Live check: prices that break P(A) = P(B) after both venues' fees, then
   checked against the order books (Kairos fee quotes for Predict.fun).
4. Price agreement over the last 24 hours: both venues' hourly last trades,
   up to each event's start.
5. Sports around game time: one-minute last trades, for games that started 6 to
   30 hours before the report.
6. Trading activity: 24-hour volume on both sides of a sample of pairs.
7. Settlement: whether both venues paid out the same way, for events of the
   last seven days.
8. Notes for Kairos: coverage gaps and data issues found along the way.

Sections 5 and 7 read the pair archive that `oracle3-extras kairos snapshot`
keeps, because Kairos drops a pair from its catalog once the markets expire.
Only aggregate statistics, charts and a few example rows are published.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import statistics
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping, Sequence
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from oracle3.market.relations import MarketRelation  # noqa: E402
from oracle3_extras.arbitrage import ScanItem, ScanReport, scan_relations  # noqa: E402
from oracle3_extras.market.archive import load_archive, started_between  # noqa: E402
from oracle3_extras.market.kairos import (  # noqa: E402
    KairosClient,
    KairosRelations,
    MatchedPair,
    PairHistory,
    SettlementCheck,
    check_settlements,
    history_summary,
    kairos_relations,
    price_history,
    recent_history,
    settlement_summary,
)

README_START = '<!-- report:start -->'
README_END = '<!-- report:end -->'

DIVISIONS = {
    'elections': 'Elections & Politics',
    'sports': 'Sports',
    'crypto': 'Crypto',
    'economics': 'Economics & Finance',
    'tech': 'Tech & Science',
    'weather': 'Climate & Weather',
}
OTHER = 'other'
ALL_GROUPS = (*DIVISIONS, OTHER)

#: Kairos category -> club division. Kairos's Culture category has none.
CATEGORY_DIVISION = {
    'Politics': 'elections',
    'World': 'elections',
    'Elections': 'elections',
    'Sports': 'sports',
    'Esports': 'sports',
    'Crypto': 'crypto',
    'Finance': 'economics',
    'Economics': 'economics',
    'Tech': 'tech',
    'Science': 'tech',
    'Weather': 'weather',
    'Climate': 'weather',
}

#: The two sides of a pair can carry different Kairos categories (a tennis
#: match tagged Crypto on one side, Fed-rate markets tagged Politics). A pair
#: goes to the first division in this order that either side points to.
PRECEDENCE = ('sports', 'weather', 'economics', 'elections', 'tech', 'crypto')

VENUE_NAMES = {
    'kalshi': 'Kalshi',
    'polymarket': 'Polymarket',
    'predictfun': 'Predict.fun',
    'hyperliquid': 'Hyperliquid',
}
VENUE_PAIRS = [
    f'{VENUE_NAMES[a]}–{VENUE_NAMES[b]}'
    for n, a in enumerate(VENUE_NAMES)
    for b in list(VENUE_NAMES)[n + 1 :]
]

#: Buckets traded on both venues before a pair can be listed among the widest.
WIDEST_MIN_MINUTES = 10
WIDEST_MIN_HOURS = 3
#: Pairs per division whose 24-hour volume is looked up.
ACTIVITY_SAMPLE = 40


# ── Divisions and venues ─────────────────────────────────────────────────


def division(categories: Iterable[str | None]) -> str:
    """The club division for a pair, from its Kairos categories."""
    found = {CATEGORY_DIVISION.get(c or '') for c in categories}
    return next((d for d in PRECEDENCE if d in found), OTHER)


def pair_division(pair: MatchedPair) -> str:
    return division([pair.a.category, pair.b.category])


def relation_division(relation: MarketRelation) -> str:
    categories = relation.analysis_b.get('kairos_categories')
    if categories is None and venues_of(relation) == 'Kalshi–Polymarket':
        # Archived by oracle3-extras 0.3, which kept no categories; every
        # Kalshi–Polymarket pair Kairos listed then was a game.
        return 'sports'
    return division(categories or [])


def venue_pair(*venues: str | None) -> str:
    order = list(VENUE_NAMES)
    known = sorted((v for v in venues if v in VENUE_NAMES), key=order.index)
    return '–'.join(VENUE_NAMES[v] for v in known)  # type: ignore[index]


def venues_of(relation: MarketRelation) -> str:
    return venue_pair(relation.market_a.get('venue'), relation.market_b.get('venue'))


def by_group(items: Iterable[Any], key: Any) -> dict[str, list[Any]]:
    groups: dict[str, list[Any]] = defaultdict(list)
    for item in items:
        groups[key(item)].append(item)
    return groups


# ── Formatting ───────────────────────────────────────────────────────────


def cents(value: float | None) -> str:
    if value is None:
        return '–'
    amount = value * 100
    return f'{amount:.1f}¢' if amount < 10 else f'{amount:.0f}¢'


def percent(value: float | None) -> str:
    return '–' if value is None else f'{value * 100:.0f}%'


def dollars(value: float | None) -> str:
    if value is None:
        return '–'
    return f'${value:,.0f}' if value >= 100 else f'${value:,.2f}'


def of(part: int, whole: int) -> str:
    return '–' if not whole else f'{part:,} of {whole:,}'


def cell(text: Any) -> str:
    """Text safe inside a Markdown table cell."""
    return str(text).replace('|', '/').replace('\n', ' ').strip()


def joined(names: Sequence[str]) -> str:
    if len(names) < 3:
        return ' and '.join(names)
    return ', '.join(names[:-1]) + ', and ' + names[-1]


# ── Collecting ───────────────────────────────────────────────────────────


def activity_sample(
    relations: Sequence[MarketRelation], per_division: int, seed: str
) -> list[MarketRelation]:
    """Up to ``per_division`` relations from each division, the same all day."""
    chosen: list[MarketRelation] = []
    for group in by_group(relations, relation_division).values():
        group.sort(
            key=lambda r: hashlib.sha256(f'{seed}:{r.relation_id}'.encode()).hexdigest()
        )
        chosen.extend(group[:per_division])
    return chosen


async def collect(archive: Path, now: datetime, *, sample: int) -> dict[str, Any]:
    client = KairosClient()
    found = await kairos_relations(client)
    relations = found.relations
    scan = await scan_relations(relations, client=client)
    recent = await recent_history(relations, client, now=now)
    archived = load_archive(archive) if archive.exists() else []
    games = [
        r
        for r in started_between(
            archived, now - timedelta(hours=30), now - timedelta(hours=6)
        )
        if relation_division(r) == 'sports'
    ]
    around = await price_history(games, client, now=now)
    week = started_between(archived, now - timedelta(days=7), now - timedelta(hours=6))
    checks = await check_settlements(week, client)
    sampled = activity_sample(relations, sample, now.date().isoformat())
    volumes = await client.trade_metrics(
        (side['venue'], str(side['market_id']))
        for r in sampled
        for side in (r.market_a, r.market_b)
    )
    data = summarize(found, scan, recent, around, checks, sampled, volumes, archived, now)
    data['with_key'] = client.credentials is not None
    return data


# ── Summaries ────────────────────────────────────────────────────────────


def coverage(found: KairosRelations) -> dict[str, dict[str, Any]]:
    listed: dict[str, Counter[str]] = defaultdict(Counter)
    for pair in found.catalog.pairs:
        listed[pair_division(pair)][venue_pair(pair.a.provider, pair.b.provider)] += 1
    aligned: dict[str, Counter[str]] = defaultdict(Counter)
    for relation in found.relations:
        aligned[relation_division(relation)][venues_of(relation)] += 1
    rejected: dict[str, Counter[str]] = defaultdict(Counter)
    for pair, reason in found.rejected:
        rejected[pair_division(pair)][reason.split(':')[0]] += 1
    return {
        d: {
            'listed': sum(listed[d].values()),
            'aligned': sum(aligned[d].values()),
            'by_venues': {
                v: {'listed': n, 'aligned': aligned[d][v]}
                for v, n in listed[d].most_common()
            },
            'rejected': dict(rejected[d].most_common()),
        }
        for d in ALL_GROUPS
    }


def live_check(items: Sequence[ScanItem]) -> dict[str, Any]:
    """Live-book and last-trade results kept apart: last trades can be weeks old."""
    live = [i for i in items if i.check is not None and not i.indicative]
    traded = [i for i in items if i.check is not None and i.indicative]
    return {
        'pairs': len(items),
        'live_quotes': len(live),
        'live_break_before_fees': sum(1 for i in live if i.check.violated),  # type: ignore[union-attr]
        'live_edge_after_fees': sum(
            1
            for i in live
            if i.check.profitable_after_fees  # type: ignore[union-attr]
        ),
        'live_edge_after_books': sum(1 for i in live if i.opportunity),
        'last_trade_prices': len(traded),
        'last_trade_edge_after_fees': sum(
            1
            for i in traded
            if i.check.profitable_after_fees  # type: ignore[union-attr]
        ),
        'fee_quotes_checked': sum(1 for i in traded if i.depth is not None),
        'fee_quote_edge': sum(1 for i in traded if i.opportunity),
        'not_priced': dict(
            Counter(
                i.skipped.split(':')[0] for i in items if i.check is None and i.skipped
            ).most_common()
        ),
    }


def opportunity_rows(scan: ScanReport, top: int = 10) -> list[dict[str, Any]]:
    rows = []
    for item in scan.opportunities()[:top]:
        depth = item.depth
        best = item.best
        rows.append(
            {
                'division': DIVISIONS.get(relation_division(item.relation), 'Other'),
                'venues': venues_of(item.relation),
                'market_a': item.relation.market_a.get('name'),
                'market_b': item.relation.market_b.get('name'),
                'basket': best.description if best else None,
                'contracts': depth.contracts if depth else best.contracts if best else None,
                'net_edge': depth.net_edge if depth else best.net_edge if best else None,
                'checked_with': 'Kairos fee quotes' if item.indicative else 'order books',
            }
        )
    return rows


def gap_stats(histories: Sequence[PairHistory]) -> dict[str, Any]:
    summary = history_summary(histories, widest=0)
    return {
        key: summary[key]
        for key in (
            'pairs',
            'pairs_with_overlap',
            'minutes',
            'median_abs_gap',
            'p90_abs_gap',
            'max_abs_gap',
            'share_wide',
        )
    }


def widest(histories: Sequence[PairHistory], least: int, top: int) -> list[dict[str, Any]]:
    """Pairs whose venues disagreed most persistently (largest median gap)."""
    enough = [h for h in histories if len(h.points) >= least]
    ranked = sorted(
        enough, key=lambda h: statistics.median(abs(g) for g in h.gaps), reverse=True
    )
    return [
        {
            **h.summary(),
            'venues': venues_of(h.relation),
            'division': DIVISIONS.get(relation_division(h.relation), 'Other'),
        }
        for h in ranked[:top]
    ]


def recent_gaps(histories: Sequence[PairHistory]) -> dict[str, dict[str, Any]]:
    groups = by_group(histories, lambda h: relation_division(h.relation))
    out = {}
    for d in ALL_GROUPS:
        group = groups.get(d, [])
        venues = by_group(group, lambda h: venues_of(h.relation))
        out[d] = {
            **gap_stats(group),
            'by_venues': {v: gap_stats(hs) for v, hs in sorted(venues.items())},
            'widest': widest(group, WIDEST_MIN_HOURS, 3),
        }
    return out


def around_start(histories: Sequence[PairHistory]) -> dict[str, Any]:
    summary = history_summary(histories, widest=0)
    venues = by_group(histories, lambda h: venues_of(h.relation))
    return {
        **summary,
        'by_venues': {v: gap_stats(hs) for v, hs in sorted(venues.items())},
        'widest': widest(histories, WIDEST_MIN_MINUTES, 5),
    }


def activity(
    sampled: Sequence[MarketRelation],
    volumes: Mapping[tuple[str, str], Mapping[str, float]],
) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for d in ALL_GROUPS:
        group = [r for r in sampled if relation_division(r) == d]
        per_venue: dict[str, list[Mapping[str, float]]] = defaultdict(list)
        for relation in group:
            for side in (relation.market_a, relation.market_b):
                found = volumes.get((side['venue'], str(side['market_id'])))
                if found is not None:
                    per_venue[side['venue']].append(found)
        venues = {}
        for venue in VENUE_NAMES:
            rows = per_venue.get(venue)
            if not rows:
                continue
            traded = [r['volume_usd'] for r in rows if r['trade_count'] > 0]
            venues[VENUE_NAMES[venue]] = {
                'markets': len(rows),
                'traded': len(traded),
                'median_volume_usd': round(statistics.median(traded), 2) if traded else None,
                'volume_usd': round(sum(traded), 2),
            }
        out[d] = {'pairs': len(group), 'venues': venues}
    return out


def settlement(checks: Sequence[SettlementCheck]) -> dict[str, Any]:
    groups = by_group(checks, lambda c: relation_division(c.relation))
    asked: Counter[str] = Counter()
    resolved: Counter[str] = Counter()
    for check in checks:
        for side, value in (
            (check.relation.market_a, check.first),
            (check.relation.market_b, check.second),
        ):
            asked[side['venue']] += 1
            resolved[side['venue']] += value is not None
    overall = settlement_summary(checks)
    return {
        **{k: v for k, v in overall.items() if k != 'mismatches'},
        'mismatches': overall['mismatches'][:10],
        'by_division': {
            d: {
                k: v
                for k, v in settlement_summary(groups.get(d, [])).items()
                if k != 'mismatches'
            }
            for d in ALL_GROUPS
        },
        'by_venue': {
            VENUE_NAMES[v]: {'asked': asked[v], 'resolved': resolved[v]}
            for v in VENUE_NAMES
            if asked[v]
        },
    }


def kairos_notes(
    found: KairosRelations,
    cover: Mapping[str, Mapping[str, Any]],
    scan: ScanReport,
    settle: Mapping[str, Any],
) -> list[str]:
    """Coverage gaps and data issues worth telling Kairos about."""
    notes = []
    empty = [DIVISIONS[d] for d in DIVISIONS if not cover[d]['listed']]
    if empty:
        notes.append(f'No matched pairs in {joined(empty)}.')
    reach: dict[str, Counter[str]] = defaultdict(Counter)
    for pair in found.catalog.pairs:
        group = pair_division(pair)
        for venue in {pair.a.provider, pair.b.provider}:
            reach[venue][group] += 1
    for venue in VENUE_NAMES:
        groups = reach.get(venue)
        if groups and len(groups) == 1:
            ((group, n),) = groups.items()
            notes.append(
                f'Every {VENUE_NAMES[venue]} pair ({n:,}) is '
                f'{DIVISIONS.get(group, "outside the six divisions")}.'
            )
    split = [
        p
        for p in found.catalog.pairs
        if p.a.category and p.b.category and p.a.category != p.b.category
    ]
    if split:
        crossing = [
            p for p in split if division([p.a.category]) != division([p.b.category])
        ]
        kinds: dict[frozenset[str], MatchedPair] = {}
        for p in crossing or split:
            kinds.setdefault(frozenset({p.a.category, p.b.category}), p)  # type: ignore[arg-type]
        examples = '; '.join(
            f'"{p.a.title}" is {p.a.category} on {VENUE_NAMES.get(p.a.provider, p.a.provider)} '
            f'and {p.b.category} on {VENUE_NAMES.get(p.b.provider, p.b.provider)}'
            for p in list(kinds.values())[:3]
        )
        notes.append(
            f'{len(split):,} pairs carry a different category on each side '
            f'({len(crossing):,} of them point to different divisions); for example {examples}.'
        )
    missing = Counter(
        (p.b if p.a.category else p.a).provider
        for p in found.catalog.pairs
        if bool(p.a.category) != bool(p.b.category)
    )
    if missing:
        sides = ', '.join(
            f'{VENUE_NAMES.get(v, v)} {n:,}' for v, n in missing.most_common()
        )
        notes.append(
            f'{sum(missing.values()):,} pairs have a category on one side only '
            f'(side without one: {sides}).'
        )
    # Pairs whose two markets turned out to be different events, games or
    # lines; pairs the checks merely could not confirm are counted once.
    mismatched = [(p, r) for p, r in found.rejected if r.startswith('different ')]
    groups = Counter(
        (venue_pair(p.a.provider, p.b.provider), r.split(':')[0]) for p, r in mismatched
    )
    for (venues, reason), n in groups.most_common(3):
        example, full = next(
            (p, r)
            for p, r in mismatched
            if venue_pair(p.a.provider, p.b.provider) == venues
            and r.split(':')[0] == reason
        )
        names = (
            f'"{example.a.title}"'
            if example.a.title == example.b.title
            else f'"{example.a.title}" and "{example.b.title}"'
        )
        detail = full.split(':', 1)[1].strip() if ':' in full else ''
        notes.append(
            f'{n:,} {venues} pairs are matched across {reason}; for example {names}'
            + (f' ({detail})' if detail else '')
            + '.'
        )
    unconfirmed = len(found.rejected) - len(mismatched)
    if unconfirmed:
        notes.append(
            f'{unconfirmed:,} more pairs could not be confirmed automatically and were '
            'left out (see "Not lined up" above).'
        )
    untraded = sum(1 for i in scan.items if i.skipped == 'no Predict.fun trades yet')
    with_predictfun = sum(
        1
        for i in scan.items
        if 'predictfun' in (i.relation.market_a.get('venue'), i.relation.market_b.get('venue'))
    )
    if untraded:
        notes.append(
            f'{of(untraded, with_predictfun)} pairs with a Predict.fun side have no '
            'Predict.fun trades yet (no mark), so they cannot be priced.'
        )
    for venue, row in settle['by_venue'].items():
        if row['asked'] and not row['resolved']:
            notes.append(
                f'No resolutions came back for {venue} ({row["asked"]:,} markets '
                'whose events started 6 hours to 7 days before the report).'
            )
    return notes


def summarize(
    found: KairosRelations,
    scan: ScanReport,
    recent: Sequence[PairHistory],
    around: Sequence[PairHistory],
    checks: Sequence[SettlementCheck],
    sampled: Sequence[MarketRelation],
    volumes: Mapping[tuple[str, str], Mapping[str, float]],
    archived: Sequence[MarketRelation],
    now: datetime,
) -> dict[str, Any]:
    cover = coverage(found)
    items = by_group(scan.items, lambda i: relation_division(i.relation))
    gaps = recent_gaps(recent)
    active = activity(sampled, volumes)
    settle = settlement(checks)
    other = Counter(
        c
        for pair in found.catalog.pairs
        if pair_division(pair) == OTHER
        for c in ({pair.a.category, pair.b.category} - {None, ''} or {'no category'})
    )
    return {
        'generated_at': now.isoformat(timespec='seconds'),
        'catalog': found.summary(),
        'divisions': {
            d: {
                'name': DIVISIONS.get(d, 'Other'),
                **cover[d],
                'live': live_check(items.get(d, [])),
                'recent': gaps[d],
                'activity': active[d],
                'settlement': settle['by_division'][d],
            }
            for d in ALL_GROUPS
        },
        'other_categories': dict(other.most_common()),
        'scan': {
            **live_check(scan.items),
            'scanned_at': scan.scanned_at,
            'opportunities': opportunity_rows(scan),
        },
        'around_start': around_start(around),
        'settlement': settle,
        'notes': kairos_notes(found, cover, scan, settle),
        'archive_pairs': len(archived),
    }


# ── Charts ───────────────────────────────────────────────────────────────


def draw(data: dict[str, Any], img: Path) -> dict[str, bool]:
    """Draw the charts; returns which ones have data."""
    img.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False}
    )
    drawn = {}

    matrix = np.array(
        [
            [data['divisions'][d]['by_venues'].get(v, {}).get('aligned', 0) for v in VENUE_PAIRS]
            for d in DIVISIONS
        ],
        dtype=float,
    )
    shade = np.log10(matrix + 1)
    top = max(1.0, float(shade.max()))
    fig, ax = plt.subplots(figsize=(8.5, 3.6))
    ax.imshow(shade, cmap='Blues', aspect='auto', vmin=0, vmax=top)
    ax.set_xticks(range(len(VENUE_PAIRS)), [v.replace('–', '–\n') for v in VENUE_PAIRS])
    ax.set_yticks(range(len(DIVISIONS)), list(DIVISIONS.values()))
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for i, row in enumerate(matrix):
        for j, n in enumerate(row):
            ax.text(
                j,
                i,
                f'{int(n):,}' if n else '–',
                ha='center',
                va='center',
                color='white' if shade[i, j] > 0.6 * top else '#333333',
            )
    ax.set_title('Pairs lined up, by division and venues (Kairos catalog)', loc='left')
    fig.tight_layout()
    fig.savefig(img / 'pairs-by-division.png', dpi=150)
    plt.close(fig)
    drawn['pairs'] = True

    rows = [
        (DIVISIONS[d], data['divisions'][d]['recent'])
        for d in DIVISIONS
        if data['divisions'][d]['recent']['median_abs_gap'] is not None
    ]
    drawn['recent'] = bool(rows)
    if rows:
        fig, ax = plt.subplots(figsize=(7.5, 0.5 * len(rows) + 1.4))
        for y, (_, g) in enumerate(rows):
            ax.plot(
                [0, g['p90_abs_gap'] * 100],
                [y, y],
                color='#d9e2ec',
                linewidth=8,
                solid_capstyle='butt',
            )
            ax.plot(g['median_abs_gap'] * 100, y, 'o', color='#b23b3b')
            ax.text(
                g['p90_abs_gap'] * 100,
                y,
                f"  {g['pairs_with_overlap']:,} pairs",
                va='center',
                fontsize=8,
                color='#555555',
            )
        ax.set_yticks(range(len(rows)), [name for name, _ in rows])
        ax.invert_yaxis()
        ax.set_xlim(left=0)
        ax.set_xlabel("gap between the venues' last trades in the same hour (cents)")
        ax.set_title(
            'Last 24 hours: median gap (dot) and 90th percentile (bar)', loc='left'
        )
        fig.tight_layout()
        fig.savefig(img / 'gap-by-division.png', dpi=150)
        plt.close(fig)

    bins = data['around_start']['by_minutes_from_start']
    drawn['around'] = bool(data['around_start']['minutes'])
    if drawn['around']:
        centers = [(b['from'] + b['to']) / 2 for b in bins]
        fig, ax = plt.subplots(figsize=(7.5, 4))
        ax.bar(
            centers,
            [b['minutes'] for b in bins],
            width=26,
            color='#d9e2ec',
            label='minutes compared',
        )
        ax.set_ylabel('minutes compared')
        ax.set_xlabel('minutes from the start of the game')
        twin = ax.twinx()
        twin.spines['top'].set_visible(False)
        for key, style, label in (
            ('median_abs_gap', '-', 'median gap'),
            ('p90_abs_gap', '--', '90th percentile'),
        ):
            points = [
                (c, b[key] * 100)
                for c, b in zip(centers, bins, strict=True)
                if b[key] is not None
            ]
            if points:
                twin.plot(
                    *zip(*points, strict=True),
                    style,
                    color='#b23b3b',
                    marker='o',
                    label=label,
                )
        twin.set_ylabel('gap between last trades (cents)')
        twin.set_ylim(bottom=0)
        ax.axvline(0, color='#888888', linewidth=1)
        twin.legend(loc='upper left', frameon=False)
        ax.set_title('Sports: last-trade gap around game time, all venue pairs', loc='left')
        fig.tight_layout()
        fig.savefig(img / 'gap-by-minute.png', dpi=150)
        plt.close(fig)
    return drawn


# ── Markdown ─────────────────────────────────────────────────────────────


def overview_rows(data: dict[str, Any]) -> list[str]:
    rows = [
        '| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |',
        '|---|---|---|---|---|---|',
    ]
    for d in DIVISIONS:
        row = data['divisions'][d]
        live, recent, sett = row['live'], row['recent'], row['settlement']
        quoted = live['live_quotes'] + live['last_trade_prices']
        confirmed = live['live_edge_after_books'] + live['fee_quote_edge']
        gap = (
            f"{cents(recent['median_abs_gap'])} ({recent['pairs_with_overlap']:,} pairs)"
            if recent['median_abs_gap'] is not None
            else '–'
        )
        rows.append(
            f"| {row['name']} | {row['listed']:,} | {row['aligned']:,} | {of(confirmed, quoted)} "
            f"| {gap} | {of(sett['agree'], sett['settled'])} |"
        )
    return rows


def markdown(data: dict[str, Any], day: str, drawn: Mapping[str, bool], *, charts: bool = True) -> str:
    cat, divs, scan = data['catalog'], data['divisions'], data['scan']
    other = divs[OTHER]
    lines = [
        f'# Kairos cross-venue report, {day}',
        '',
        f"Generated {data['generated_at'][:16].replace('T', ' ')} UTC from Kairos's matched-market "
        f"catalog, Market Data API{' and fee quotes' if data.get('with_key') else ''}, and Kalshi "
        'and Polymarket order books. Pairs are grouped into '
        "[Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by "
        "Kairos's own categories.",
        '',
        '## Overview',
        '',
        *overview_rows(data),
        '',
    ]
    if other['listed']:
        kinds = ', '.join(f'{k} {n:,}' for k, n in data['other_categories'].items())
        lines += [
            f"Another {other['listed']:,} pairs fall outside the six divisions ({kinds}).",
            '',
        ]

    lines += [
        '## Pairs',
        '',
        f"Kairos listed {cat['pairs']:,} matched pairs across "
        f"{len(cat['pairs_by_venues'])} venue combinations; oracle3-extras lined up the outcomes of "
        f"{cat['aligned']:,} ({percent(cat['aligned'] / cat['pairs'] if cat['pairs'] else None)}), "
        f"{cat['with_warnings']} of them with a warning such as a postponed game.",
        '',
        *(['![Pairs by division](img/pairs-by-division.png)', ''] if charts else []),
        '| Division | Venues | Lined up |',
        '|---|---|---|',
    ]
    for d in ALL_GROUPS:
        for venues, row in divs[d]['by_venues'].items():
            lines.append(f"| {divs[d]['name']} | {venues} | {of(row['aligned'], row['listed'])} |")
    if cat['rejected']:
        lines += ['', '| Not lined up | Pairs |', '|---|---|']
        lines += [f'| {cell(reason)} | {n} |' for reason, n in cat['rejected'].items()]

    lines += [
        '',
        '## Live check',
        '',
        'Each pair is priced on both venues and checked for a basket that pays more than it costs '
        "after both venues' fees. Kalshi and Polymarket have public order books, so their edges are "
        'walked down the books. Predict.fun is priced from its last trades, which can be weeks old; '
        'the largest of those edges are confirmed with Kairos fee quotes, which walk the live '
        'Predict.fun book.',
        '',
        '| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |',
        '|---|---|---|---|---|---|---|---|',
    ]
    for d in ALL_GROUPS:
        live = divs[d]['live']
        if not live['pairs']:
            continue
        lines.append(
            f"| {divs[d]['name']} | {live['live_quotes']:,} | {live['live_edge_after_fees']:,} "
            f"| {live['live_edge_after_books']:,} | {live['last_trade_prices']:,} "
            f"| {live['last_trade_edge_after_fees']:,} | {live['fee_quotes_checked']:,} "
            f"| {live['fee_quote_edge']:,} |"
        )
    if not data.get('with_key'):
        lines += [
            '',
            'This run had no Kairos API key, so no last-trade edge was checked with a fee quote.',
        ]
    if scan['not_priced']:
        reasons = '; '.join(f'{cell(r)} {n:,}' for r, n in scan['not_priced'].items())
        lines += ['', f'Not priced: {reasons}.']
    if scan['opportunities']:
        lines += [
            '',
            '| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with |',
            '|---|---|---|---|---|---|---|---|',
        ]
        for o in scan['opportunities']:
            lines.append(
                f"| {o['division']} | {o['venues']} | {cell(o['market_a'])} | {cell(o['market_b'])} "
                f"| {cell(o['basket'])} | {o['contracts']} | ${(o['net_edge'] or 0):.4f} | {o['checked_with']} |"
            )
    lines += [
        '',
        'Most edges at the top of the book disappear after fees, in the order books, or once a stale '
        'last trade meets the live book.',
        '',
        '## Price agreement, last 24 hours',
        '',
        "For every pair, both venues' last trades in each hour of the last 24 hours, up to the "
        "event's start (a game under way is compared on its pre-game prices only).",
        '',
    ]
    if drawn.get('recent'):
        lines += [
            *(['![Gap by division](img/gap-by-division.png)', ''] if charts else []),
            '| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |',
            '|---|---|---|---|---|---|',
        ]
        for d in ALL_GROUPS:
            g = divs[d]['recent']
            if not g['minutes']:
                continue
            lines.append(
                f"| {divs[d]['name']} | {g['pairs_with_overlap']:,} | {g['minutes']:,} "
                f"| {cents(g['median_abs_gap'])} | {cents(g['p90_abs_gap'])} | {percent(g['share_wide'])} |"
            )
        lines += ['', '| Division | Venues | Pairs compared | Median gap | 90th percentile |', '|---|---|---|---|---|']
        for d in ALL_GROUPS:
            for venues, g in divs[d]['recent']['by_venues'].items():
                if g['minutes']:
                    lines.append(
                        f"| {divs[d]['name']} | {venues} | {g['pairs_with_overlap']:,} "
                        f"| {cents(g['median_abs_gap'])} | {cents(g['p90_abs_gap'])} |"
                    )
        wide = [w for d in ALL_GROUPS for w in divs[d]['recent']['widest']]
        if wide:
            lines += [
                '',
                f'| Most persistent gaps (at least {WIDEST_MIN_HOURS} hours compared) | Division | Venues | Median gap | Hours |',
                '|---|---|---|---|---|',
            ]
            for w in sorted(wide, key=lambda w: w['median_abs_gap'] or 0, reverse=True)[:8]:
                lines.append(
                    f"| {cell(w['market_b'])} | {w['division']} | {w['venues']} "
                    f"| {cents(w['median_abs_gap'])} | {w['minutes']} |"
                )
    else:
        lines.append('No pair traded on both venues in the same hour.')

    hist = data['around_start']
    lines += ['', '## Sports around game time', '']
    if hist['minutes']:
        lines += [
            f"Games that started 6 to 30 hours ago: {hist['pairs_with_overlap']:,} of {hist['pairs']:,} "
            f"pairs traded on both venues in the same minute, {hist['minutes']:,} minutes in all. The "
            f"median gap between the two last trades was {cents(hist['median_abs_gap'])} and the 90th "
            f"percentile {cents(hist['p90_abs_gap'])}; before the start the 90th percentile was "
            f"{cents(hist['before_start']['p90_abs_gap'])}.",
            '',
            *(['![Gap around game time](img/gap-by-minute.png)', ''] if charts else []),
            '| Venues | Pairs compared | Minutes | Median gap | 90th percentile |',
            '|---|---|---|---|---|',
            *[
                f"| {v} | {g['pairs_with_overlap']:,} | {g['minutes']:,} | {cents(g['median_abs_gap'])} | {cents(g['p90_abs_gap'])} |"
                for v, g in hist['by_venues'].items()
                if g['minutes']
            ],
        ]
        if hist['widest']:
            lines += [
                '',
                f'| Most persistent gaps (at least {WIDEST_MIN_MINUTES} minutes compared) | Venues | Median gap | Largest | Minutes |',
                '|---|---|---|---|---|',
                *[
                    f"| {cell(w['market_b'])} | {w['venues']} | {cents(w['median_abs_gap'])} "
                    f"| {cents(w['max_abs_gap'])} | {w['minutes']} |"
                    for w in hist['widest']
                ],
            ]
        lines += [
            '',
            'These are trade prices up to a minute apart, not quotes: a gap shows the venues '
            'disagreeing, not an arbitrage that could have been executed.',
        ]
    else:
        lines.append('No archived games started 6 to 30 hours ago yet; the archive is still filling.')

    lines += [
        '',
        '## Trading activity',
        '',
        f'24-hour volume from Kairos trade metrics for up to {data.get("activity_sample", ACTIVITY_SAMPLE)} '
        'pairs per division, chosen at random each day.',
        '',
        '| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |',
        '|---|---|---|---|---|',
    ]
    for d in ALL_GROUPS:
        for venue, row in divs[d]['activity']['venues'].items():
            lines.append(
                f"| {divs[d]['name']} | {venue} | {row['markets']:,} | {of(row['traded'], row['markets'])} "
                f"| {dollars(row['median_volume_usd'])} |"
            )

    sett = data['settlement']
    lines += ['', '## Settlement', '']
    if sett['checked']:
        lines += [
            f"Events that started in the last seven days: {sett['settled']:,} pairs have settled on both "
            f"venues and {sett['agree']:,} settled the same way ({percent(sett['agreement_rate'])}); "
            f"{sett['pending']:,} are still settling or have no result from Kairos.",
            '',
            '| Division | Settled on both venues | Same way | Still settling |',
            '|---|---|---|---|',
            *[
                f"| {divs[d]['name']} | {s['settled']:,} | {s['agree']:,} | {s['pending']:,} |"
                for d in ALL_GROUPS
                if (s := divs[d]['settlement'])['checked']
            ],
            '',
            '| Venue | Markets looked up | Resolved |',
            '|---|---|---|',
            *[f"| {v} | {r['asked']:,} | {r['resolved']:,} |" for v, r in sett['by_venue'].items()],
        ]
        if sett['mismatches']:
            lines += [
                '',
                '| Market A | Market B | Venues | A first outcome paid | B first outcome paid |',
                '|---|---|---|---|---|',
                *[
                    f"| {cell(m['market_a'])} | {cell(m['market_b'])} | {m['venues']} "
                    f"| {m['a_first_outcome_paid']} | {m['b_first_outcome_paid']} |"
                    for m in sett['mismatches']
                ],
            ]
    else:
        lines.append('No archived pairs have reached settlement yet; the archive is still filling.')

    lines += ['', '## Notes for Kairos', '']
    lines += [f'- {note}' for note in data['notes']] or ['- Nothing new today.']
    lines += [
        '',
        '## Method',
        '',
        '- Pairs come from Kairos `/matched-markets`; [oracle3-extras]'
        '(https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and '
        "decides which outcome of market B pays when market A's first outcome pays.",
        "- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and "
        'Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two '
        'sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & '
        'Politics, Tech & Science and Crypto.',
        "- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket "
        'order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.',
        '- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; '
        'trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.',
        '- Only aggregates and a few example rows are published here.',
        '',
    ]
    return '\n'.join(lines)


def readme_block(data: dict[str, Any], day: str) -> str:
    cat = data['catalog']
    rows = [
        f'**Latest report: [{day}](reports/latest.md)**: {cat["aligned"]:,} of {cat["pairs"]:,} '
        'Kairos pairs lined up across Kalshi, Polymarket, Predict.fun and Hyperliquid.',
        '',
        *overview_rows(data),
        '',
        '![Pairs by division](reports/img/pairs-by-division.png)',
    ]
    return '\n'.join(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--out', type=Path, default=Path('reports'))
    parser.add_argument('--readme', type=Path, default=Path('README.md'))
    parser.add_argument(
        '--sample',
        type=int,
        default=ACTIVITY_SAMPLE,
        help='pairs per division whose 24-hour volume is looked up',
    )
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    day = now.date().isoformat()
    data = asyncio.run(collect(args.archive, now, sample=args.sample))
    data['activity_sample'] = args.sample

    args.out.mkdir(parents=True, exist_ok=True)
    drawn = draw(data, args.out / 'img')
    # Dated reports keep the numbers; only the latest report carries charts,
    # so the repository does not grow by three images a day.
    (args.out / f'{day}.md').write_text(markdown(data, day, drawn, charts=False))
    (args.out / 'latest.md').write_text(markdown(data, day, drawn))
    summaries = args.out / 'data'
    summaries.mkdir(exist_ok=True)
    (summaries / f'{day}.json').write_text(json.dumps(data, indent=2, default=str))

    if args.readme.exists():
        readme = args.readme.read_text()
        if README_START in readme and README_END in readme:
            head, rest = readme.split(README_START, 1)
            _, tail = rest.split(README_END, 1)
            args.readme.write_text(
                f'{head}{README_START}\n{readme_block(data, day)}\n{README_END}{tail}'
            )
    print(
        json.dumps(
            {
                'day': day,
                'pairs': data['catalog']['pairs'],
                'aligned': data['catalog']['aligned'],
                'confirmed': data['scan']['live_edge_after_books'] + data['scan']['fee_quote_edge'],
                'recent_pairs': sum(
                    data['divisions'][d]['recent']['pairs_with_overlap'] for d in ALL_GROUPS
                ),
                'around_minutes': data['around_start']['minutes'],
                'settled': data['settlement']['settled'],
                'agree': data['settlement']['agree'],
            }
        )
    )


if __name__ == '__main__':
    main()
