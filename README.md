# Kairos cross-venue monitor

A daily look at how prediction markets price the same events on different venues, built on [Kairos](https://kairos.trade)'s matched-market catalog. Kairos finds the same market on Kalshi, Polymarket, Predict.fun and Hyperliquid; this repository checks every pair it lists and reports by [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions: Elections & Politics, Sports, Crypto, Economics & Finance, Tech & Science, and Climate & Weather.

<!-- report:start -->
**Latest report: [2026-10-07](reports/latest.md)**

The first report with every venue and division is built by the next scheduled run.
<!-- report:end -->

## What it measures

| Part | Question | Data |
|---|---|---|
| Pairs | Which markets on two venues are the same event, and which outcome of one pays when the other's pays? | Kairos `/matched-markets`, checked on both venues by [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) |
| Live check | Do any prices break P(A) = P(B) after both venues' fees, and for how many contracts? | Kalshi and Polymarket order books; Kairos marks and fee quotes for Predict.fun |
| Price agreement | How far apart do the two venues trade over the last day, before each event starts? | Kairos hourly candles |
| Sports around game time | How far apart do they trade before and during a game? | Kairos one-minute candles |
| Trading activity | Where is the volume, by division and venue? | Kairos `/v1/trades/metrics`, for a daily sample of pairs |
| Settlement | Did both venues pay out the same way? | Kairos `/v1/resolutions` |
| Notes for Kairos | Which divisions and venues the catalog covers, and what does not line up | All of the above |

Pairs go to a division by Kairos's own categories (Politics and World to Elections & Politics, Sports and Esports to Sports, Finance to Economics & Finance, Tech and Science to Tech & Science). When the two sides of a pair carry different categories, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto: Kairos tags some tennis matches Crypto and some Fed-rate markets Politics.

Each day's numbers are in [`reports/`](reports/); [`reports/latest.md`](reports/latest.md) is the newest, and [`reports/data/`](reports/data/) holds the same numbers as JSON.

## How it works

```text
Kairos Data API             oracle3-extras                          this repository
/matched-markets    --->    line up outcomes on both venues   --->  three times a day: archive the pairs
                            scan after fees, walk order books        daily at 12:00 UTC: report by division
Kairos Market Data API -->  marks, candles, trade metrics,           reports/, README
Kairos fee quotes           settlement checks
```

[`.github/workflows/monitor.yml`](.github/workflows/monitor.yml) adds the current pairs to an archive at 00:00, 06:00 and 18:00 UTC, because Kairos drops a pair from its catalog once the markets expire. The 12:00 UTC run also builds the report with [`report.py`](report.py) and commits it.

## Run it yourself

```bash
pip install -r requirements.txt
oracle3-extras kairos snapshot --archive archive/pairs.jsonl.gz   # a few times a day
python report.py --archive archive/pairs.jsonl.gz --out reports
```

No account is needed, but a Kairos API key makes the report faster and more complete: set `KAIROS_CLIENT_ID`, `KAIROS_API_KEY` and `KAIROS_API_SECRET` (a read-only key is enough; nothing here trades). The key raises the rate limits tenfold and is needed for the fee quotes that confirm Predict.fun prices. In GitHub Actions, add them as repository secrets.

## Reading the numbers

- **Live check** counts pairs whose prices break the bound after fees on both legs. Kalshi and Polymarket edges are walked down the order books. Predict.fun is priced from its last trades, which can be weeks old, so its edges count only once a Kairos fee quote confirms them on the live book.
- **Price agreement** and **sports around game time** compare the last trades on each venue in the same hour or minute. They show the venues disagreeing, not an arbitrage that could have been executed: two trades in one bucket can be up to a bucket apart.
- **Settlement** compares how each venue paid out. A disagreement means the two contracts were not the same bet after all, which is the main risk in cross-venue trading.

## Data and attribution

Data: Kairos Data API, Market Data API and Execution API fee quotes; Kalshi and Polymarket public APIs. This repository publishes aggregate statistics, charts and a few example rows; the archive of pairs stays in the workflow cache. Kairos, Kalshi, Polymarket, Predict.fun and Hyperliquid are trademarks of their owners; this project is not affiliated with or endorsed by them.

## License

Apache 2.0; see [LICENSE](LICENSE).
