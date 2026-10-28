# Kairos cross-venue report, 2026-10-28

Generated 2026-10-28 17:57 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 489 | 489 | 0 of 224 | 1.0¢ (51 pairs) | 17 of 17 |
| Sports | 12,079 | 11,927 | 7 of 3,782 | 1.0¢ (996 pairs) | 16,943 of 17,000 |
| Crypto | 393 | 393 | 0 of 294 | 1.8¢ (43 pairs) | – |
| Economics & Finance | 303 | 303 | 0 of 216 | 0.5¢ (36 pairs) | – |
| Tech & Science | 134 | 134 | 0 of 63 | 1.6¢ (22 pairs) | 4 of 4 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 93 pairs fall outside the six divisions (Culture 93).

## Pairs

Kairos listed 13,491 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 13,339 (99%), 77 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 489 of 489 |
| Sports | Polymarket–Predict.fun | 9,040 of 9,044 |
| Sports | Kalshi–Polymarket | 2,493 of 2,553 |
| Sports | Kalshi–Predict.fun | 347 of 352 |
| Sports | Kalshi–Hyperliquid | 12 of 56 |
| Sports | Polymarket–Hyperliquid | 14 of 51 |
| Sports | Predict.fun–Hyperliquid | 21 of 23 |
| Crypto | Polymarket–Predict.fun | 393 of 393 |
| Economics & Finance | Polymarket–Predict.fun | 303 of 303 |
| Tech & Science | Polymarket–Predict.fun | 134 of 134 |
| Other | Polymarket–Predict.fun | 93 of 93 |

| Not lined up | Pairs |
|---|---|
| different dates | 127 |
| could not confirm both markets ask about the same team | 7 |
| different start times | 4 |
| could not tell which outcome is the Kalshi YES outcome | 4 |
| different events | 4 |
| Kalshi market is inactive | 3 |
| could not line up the outcomes | 2 |
| Kalshi market is determined | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 224 | 170 | 8 | 0 |
| Sports | 2,493 | 17 | 7 | 1,289 | 546 | 17 | 0 |
| Crypto | 0 | 0 | 0 | 294 | 159 | 4 | 0 |
| Economics & Finance | 0 | 0 | 0 | 216 | 155 | 10 | 0 |
| Tech & Science | 0 | 0 | 0 | 63 | 48 | 5 | 0 |
| Other | 0 | 0 | 0 | 28 | 19 | 6 | 0 |

Not priced: no Predict.fun trades yet 8,685; no live quotes for Hyperliquid yet 47.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Army wins | Army Black Knights vs. Duke Blue Devils | YES on A + NO on B | 27.91 | $0.2324 | order books | 2026-11-02 |
| Sports | Kalshi–Polymarket | Oakland wins | Oakland Golden Grizzlies vs. Michigan Wolverines | YES on A + NO on B | 5.05 | $0.0249 | order books | 2026-11-02 |
| Sports | Kalshi–Polymarket | Grigory Shebekin wins | M15 Fergana: Grigory Shebekin vs Akhmadjon Toshmukhamedov | NO on A + YES on B | 0.49 | $0.0225 | order books | 2026-11-05 |
| Sports | Kalshi–Polymarket | NJIT wins | NJIT Highlanders vs. Dayton Flyers | YES on A + NO on B | 3.25 | $0.0196 | order books | 2026-11-03 |
| Sports | Kalshi–Polymarket | Campbell wins | Campbell Fighting Camels vs. North Carolina State Wolfpack | YES on A + NO on B | 5.05 | $0.0195 | order books | 2026-11-03 |
| Sports | Kalshi–Polymarket | Fiorentina wins | Will ACF Fiorentina win on 2026-11-08? | YES on A + NO on B | 0.01 | $0.0001 | order books | 2026-11-08 |
| Sports | Kalshi–Polymarket | Tie is the result | Will ACF Fiorentina vs. Juventus FC end in a draw? | YES on A + NO on B | 0.01 | $0.0001 | order books | 2026-11-08 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 51 | 190 | 1.0¢ | 2.0¢ | 17% |
| Sports | 996 | 5,048 | 1.0¢ | 2.0¢ | 15% |
| Crypto | 43 | 66 | 1.8¢ | 5.1¢ | 45% |
| Economics & Finance | 36 | 185 | 0.5¢ | 3.0¢ | 19% |
| Tech & Science | 22 | 33 | 1.6¢ | 19¢ | 42% |
| Other | 5 | 32 | 0.5¢ | 1.8¢ | 9% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 51 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Hyperliquid | 11 | 1.1¢ | 2.2¢ |
| Sports | Kalshi–Polymarket | 451 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 61 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Hyperliquid | 8 | 0.7¢ | 1.3¢ |
| Sports | Polymarket–Predict.fun | 458 | 1.0¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 7 | 0.8¢ | 1.5¢ |
| Crypto | Polymarket–Predict.fun | 43 | 1.8¢ | 5.1¢ |
| Economics & Finance | Polymarket–Predict.fun | 36 | 0.5¢ | 3.0¢ |
| Tech & Science | Polymarket–Predict.fun | 22 | 1.6¢ | 19¢ |
| Other | Polymarket–Predict.fun | 5 | 0.5¢ | 1.8¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Swiss Indoors Basel: Ben Shelton vs Jerome Kym | Sports | Polymarket–Predict.fun | 13¢ | 3 |
| Counter-Strike: Luminosity vs Envy (BO3) - Tesla Cup Group B | Sports | Kalshi–Predict.fun | 4.0¢ | 4 |
| Will NVIDIA be the largest company in the world by market cap on December 31? | Economics & Finance | Polymarket–Predict.fun | 4.0¢ | 3 |
| Will Goldman Sachs or any of its underwriting affiliates serve as the lead underwriter in Anthropic's initial public offering? | Economics & Finance | Polymarket–Predict.fun | 3.8¢ | 3 |
| Will Delcy Rodríguez be the leader of Venezuela end of 2026? | Elections & Politics | Polymarket–Predict.fun | 3.0¢ | 6 |
| Counter-Strike: Aurora Young Blood vs DimoniX Esports (BO3) - CCT Europe Contenders #10 Playoffs | Sports | Kalshi–Polymarket | 3.0¢ | 4 |
| Will Dreamcash launch a token by December 31, 2026? | Crypto | Polymarket–Predict.fun | 2.7¢ | 3 |
| Puffpaw FDV above $300M one day after launch? | Crypto | Polymarket–Predict.fun | 2.5¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 991 of 1,538 pairs traded on both venues in the same minute, 30,612 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 653 | 22,421 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 338 | 8,191 | 1.0¢ | 3.4¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| LoL: Vitality Rising Bees vs Mental Rush - Game 2 Winner | Polymarket–Predict.fun | 7.0¢ | 21¢ | 18 |
| Counter-Strike: DNK vs Dark Moon (BO3) - Exort Fiesta Group Stage | Polymarket–Predict.fun | 6.0¢ | 16¢ | 33 |
| Counter-Strike: Wingman vs Revise (BO3) - Exort Fiesta Group Stage | Polymarket–Predict.fun | 5.9¢ | 64¢ | 15 |
| Counter-Strike: Inner Circle Academy vs Lavked - Map 2 Winner | Polymarket–Predict.fun | 5.0¢ | 8.0¢ | 11 |
| Valorant: Any Questions Gaming vs Rare Atom - Map 1 Winner | Polymarket–Predict.fun | 4.7¢ | 11¢ | 10 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 32 of 40 | $691 |
| Elections & Politics | Predict.fun | 40 | 7 of 40 | $20.92 |
| Sports | Kalshi | 9 | 4 of 9 | $855 |
| Sports | Polymarket | 38 | 11 of 38 | $463 |
| Sports | Predict.fun | 33 | 6 of 33 | $1,097 |
| Crypto | Polymarket | 40 | 24 of 40 | $202 |
| Crypto | Predict.fun | 40 | 8 of 40 | $181 |
| Economics & Finance | Polymarket | 40 | 23 of 40 | $1,803 |
| Economics & Finance | Predict.fun | 40 | 10 of 40 | $172 |
| Tech & Science | Polymarket | 40 | 27 of 40 | $2,121 |
| Tech & Science | Predict.fun | 40 | 11 of 40 | $37.65 |
| Other | Polymarket | 40 | 24 of 40 | $148 |
| Other | Predict.fun | 40 | 3 of 40 | $131 |

## Settlement

Events that started in the last seven days: 17,021 pairs have settled on both venues and 16,964 settled the same way (100%); 493 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 17 | 17 | 12 |
| Sports | 17,000 | 16,943 | 481 |
| Tech & Science | 4 | 4 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,942 | 5,636 |
| Polymarket | 16,764 | 16,681 |
| Predict.fun | 12,211 | 12,155 |
| Hyperliquid | 111 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Ann Li wins | Wuhan Tennis Open: Ann Li vs Qinwen Zheng | kalshi + predictfun | 0.29 | 0.5 |
| Belinda Bencic wins | Wuhan Tennis Open: Belinda Bencic vs Shuai Zhang | kalshi + predictfun | 0.82 | 0.5 |
| Iva Jovic wins | Wuhan Tennis Open: Iva Jovic vs Mia Pohankova | kalshi + predictfun | 0.85 | 0.5 |
| Diane Parry wins | Wuhan Tennis Open: Diane Parry vs Anna Kalinskaya | kalshi + predictfun | 0.35 | 0.5 |
| Janice Tjen wins | Wuhan Tennis Open: Janice Tjen vs Oleksandra Oliynykova | kalshi + predictfun | 0.72 | 0.5 |
| Anna Kalinskaya wins | Wuhan Tennis Open: Anna Kalinskaya vs Shuai Zhang | kalshi + predictfun | 0.68 | 0.5 |
| ENCE Prospects wins | Counter-Strike: ENCE Prospects vs TheChampionGG (BO3) - United21 Group B | kalshi + predictfun | 0.5 | 1.0 |
| Alter Ego wins | Counter-Strike: Alter Ego vs Rare Atom (BO3) - VOID Autumn Cup Playoffs | kalshi + predictfun | 0.59 | 0.5 |
| BENCHPRESS wins | Counter-Strike: BENCHPRESS vs NEW VISION (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.41 | 0.5 |
| MEIA NOITE wins | Counter-Strike: MEIA NOITE vs BESTIA Academy (BO1) - Gamers Club Liga Série A Group B | kalshi + predictfun | 0.53 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,961) is Sports.
- Every Hyperliquid pair (130) is Sports.
- 213 pairs carry a different category on each side (94 of them point to different divisions); for example "Kosuke Shibano wins" is Sports on Kalshi and Crypto on Polymarket; "San Diego wins" is Sports on Kalshi and Culture on Polymarket; "Will Weibo Gaming win the OU Gaming vs. Weibo Gaming Overwatch match?" is Sports on Kalshi and World on Polymarket.
- 1,562 pairs have a category on one side only (side without one: Polymarket 1,562).
- 47 Kalshi–Polymarket pairs are matched across different dates; for example "Lorient wins" and "Will FC Lorient win on 2026-10-31?" (Kalshi 2026-10-31, Polymarket starts 2026-11-02 19:45Z).
- 43 Kalshi–Hyperliquid pairs are matched across different dates; for example "Bayern Munich wins" and "Bundesliga Matchday 8: FC Bayern Munich v Borussia Dortmund: FC Bayern Munich" (Kalshi 2026-10-31, Hyperliquid 2026-11-07).
- 37 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Genoa CFC win on 2026-10-28?" and "Italian Serie A Matchday 9: Genoa v Juventus: Genoa" (Polymarket 2026-10-28, Hyperliquid 2026-11-04).
- 17 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 8,685 of 10,820 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (111 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
