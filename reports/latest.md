# Kairos cross-venue report, 2026-11-09

Generated 2026-11-09 21:59 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 372 | 372 | 0 of 179 | 1.6¢ (17 pairs) | 116 of 116 |
| Sports | 9,808 | 9,650 | 4 of 2,841 | 1.0¢ (641 pairs) | 18,650 of 18,727 |
| Crypto | 379 | 379 | 0 of 267 | 2.0¢ (22 pairs) | – |
| Economics & Finance | 290 | 290 | 0 of 190 | 1.2¢ (34 pairs) | – |
| Tech & Science | 117 | 117 | 0 of 48 | 1.4¢ (7 pairs) | – |
| Climate & Weather | 0 | 0 | – | – | – |

Another 172 pairs fall outside the six divisions (Culture 172).

## Pairs

Kairos listed 11,138 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 10,980 (99%), 92 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 372 of 372 |
| Sports | Polymarket–Predict.fun | 7,222 of 7,222 |
| Sports | Kalshi–Polymarket | 2,106 of 2,118 |
| Sports | Kalshi–Predict.fun | 306 of 309 |
| Sports | Kalshi–Hyperliquid | 0 of 95 |
| Sports | Polymarket–Hyperliquid | 0 of 48 |
| Sports | Predict.fun–Hyperliquid | 16 of 16 |
| Crypto | Polymarket–Predict.fun | 379 of 379 |
| Economics & Finance | Polymarket–Predict.fun | 290 of 290 |
| Tech & Science | Polymarket–Predict.fun | 117 of 117 |
| Other | Polymarket–Predict.fun | 172 of 172 |

| Not lined up | Pairs |
|---|---|
| different dates | 143 |
| different start times | 7 |
| could not confirm both markets ask about the same team | 4 |
| Kalshi market is inactive | 2 |
| could not tell which outcome is the Kalshi YES outcome | 2 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 179 | 137 | 12 | 0 |
| Sports | 2,106 | 8 | 4 | 735 | 377 | 10 | 0 |
| Crypto | 0 | 0 | 0 | 267 | 141 | 4 | 0 |
| Economics & Finance | 0 | 0 | 0 | 190 | 139 | 14 | 0 |
| Tech & Science | 0 | 0 | 0 | 48 | 35 | 3 | 0 |
| Other | 0 | 0 | 0 | 44 | 28 | 7 | 0 |

Not priced: no Predict.fun trades yet 7,395; no live quotes for Hyperliquid yet 16.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Fabio Manuel Zavalaga Uculmana wins | Lima: Fabio Zavalaga vs Alex Barrena | NO on A + YES on B | 15.24 | $0.1703 | order books | 2026-11-16 |
| Sports | Kalshi–Polymarket | Emilia Carlotta Brune wins | W15 Monastir: Emilia Carlotta Brune vs Yoana Moneva | NO on A + YES on B | 5.0 | $0.0192 | order books | 2026-11-17 |
| Sports | Kalshi–Polymarket | Ema Harajda wins | W15 Sharm ElSheikh: Ema Harajda vs Alexandra Chapurina | YES on A + NO on B | 0.5 | $0.0077 | order books | 2026-11-17 |
| Sports | Kalshi–Polymarket | Kangyuan Shi wins | M15 Maanshan: Kangyuan Shi vs jintao Lan | YES on A + NO on B | 28.3 | $0.0012 | order books | 2026-11-17 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 17 | 27 | 1.6¢ | 3.2¢ | 33% |
| Sports | 641 | 3,196 | 1.0¢ | 3.0¢ | 23% |
| Crypto | 22 | 30 | 2.0¢ | 6.9¢ | 53% |
| Economics & Finance | 34 | 67 | 1.2¢ | 6.0¢ | 37% |
| Tech & Science | 7 | 9 | 1.4¢ | 5.0¢ | 33% |
| Other | 11 | 41 | 0.4¢ | 4.0¢ | 29% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 17 | 1.6¢ | 3.2¢ |
| Sports | Kalshi–Polymarket | 407 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 47 | 1.0¢ | 3.0¢ |
| Sports | Polymarket–Predict.fun | 180 | 1.0¢ | 3.5¢ |
| Sports | Predict.fun–Hyperliquid | 7 | 0.9¢ | 2.0¢ |
| Crypto | Polymarket–Predict.fun | 22 | 2.0¢ | 6.9¢ |
| Economics & Finance | Polymarket–Predict.fun | 34 | 1.2¢ | 6.0¢ |
| Tech & Science | Polymarket–Predict.fun | 7 | 1.4¢ | 5.0¢ |
| Other | Polymarket–Predict.fun | 11 | 0.4¢ | 4.0¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Will France win on 2026-11-15? | Sports | Kalshi–Polymarket | 9.0¢ | 3 |
| Will Kiin win Worlds 2026 Finals MVP? | Sports | Polymarket–Predict.fun | 8.3¢ | 8 |
| Will Vietnam win on 2026-11-11? | Sports | Polymarket–Predict.fun | 6.0¢ | 8 |
| Will Dani win the GMGN GGC Season 1 Grand Final? | Other | Polymarket–Predict.fun | 5.2¢ | 3 |
| Jensen Huang announced resignation or removal by December 31? | Economics & Finance | Polymarket–Predict.fun | 2.7¢ | 3 |
| Will there be no change in Fed interest rates after the December 2026 meeting? | Economics & Finance | Polymarket–Predict.fun | 2.6¢ | 3 |
| Will Ethereum reach $2,500 in November? | Crypto | Polymarket–Predict.fun | 2.2¢ | 4 |
| Will Anthropic IPO by November 20, 2026? | Economics & Finance | Polymarket–Predict.fun | 2.0¢ | 4 |

## Sports around game time

Games that started 6 to 30 hours ago: 1,046 of 2,269 pairs traded on both venues in the same minute, 33,389 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 1.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 589 | 23,850 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 457 | 9,539 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Pelicans vs. Clippers: O/U 255.5 | Kalshi–Polymarket | 5.0¢ | 22¢ | 14 |
| Counter-Strike: Alliance vs PRIVATE - Map 2 Winner | Polymarket–Predict.fun | 4.0¢ | 16¢ | 12 |
| Dota 2: Nemiga Gaming vs Zenith - Game 2 Winner | Polymarket–Predict.fun | 4.0¢ | 24¢ | 10 |
| Dota 2: angry birds vs Ka4kanarskie cyxariki (BO3) - 1win Essence Play-in Group A | Polymarket–Predict.fun | 2.9¢ | 24¢ | 10 |
| Counter-Strike: Alliance vs PRIVATE - Map 1 Winner | Polymarket–Predict.fun | 3.7¢ | 11¢ | 10 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 32 of 40 | $1,023 |
| Elections & Politics | Predict.fun | 40 | 3 of 40 | $1,279 |
| Sports | Kalshi | 7 | 4 of 7 | $59.39 |
| Sports | Polymarket | 40 | 3 of 40 | $974 |
| Sports | Predict.fun | 33 | 2 of 33 | $293 |
| Crypto | Polymarket | 40 | 14 of 40 | $620 |
| Crypto | Predict.fun | 40 | 4 of 40 | $53.44 |
| Economics & Finance | Polymarket | 40 | 29 of 40 | $764 |
| Economics & Finance | Predict.fun | 40 | 7 of 40 | $21.54 |
| Tech & Science | Polymarket | 40 | 28 of 40 | $355 |
| Tech & Science | Predict.fun | 40 | 5 of 40 | $43.39 |
| Other | Polymarket | 40 | 25 of 40 | $60.00 |
| Other | Predict.fun | 40 | 3 of 40 | $144 |

## Settlement

Events that started in the last seven days: 18,845 pairs have settled on both venues and 18,768 settled the same way (100%); 402 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 116 | 116 | 15 |
| Sports | 18,727 | 18,650 | 387 |
| Other | 2 | 2 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 6,154 | 6,082 |
| Polymarket | 18,633 | 18,327 |
| Predict.fun | 13,686 | 13,404 |
| Hyperliquid | 21 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Katarzyna Kawa wins | Ningbo Open: Katarzyna Kawa vs Maja Chwalinska | kalshi + predictfun | 0.26 | 0.5 |
| Alexander Bublik wins | Almaty Open: Alexander Bublik vs Fabian Marozsan | kalshi + predictfun | 0.72 | 0.5 |
| Andre Petroski wins | UFC Fight Night: Andre Petroski vs. Azamat Bekoev (Middleweight, Prelims) | kalshi + predictfun | 0.4 | 0.5 |
| Alejandro Davidovich Fokina wins | Rolex Paris Masters: Alejandro Davidovich Fokina vs Moise Kouame | kalshi + polymarket | 0.74 | 0.5 |
| Stefanos Tsitsipas wins | Rolex Paris Masters: Stefanos Tsitsipas vs Learner Tien | kalshi + polymarket | 0.45 | 0.5 |
| Abha wins | Will Abha Saudi Club win on 2026-11-05? | kalshi + polymarket | 0.19 | 0.0 |
| Al-Shabab wins | Will Al Shabab Saudi Club win on 2026-11-05? | kalshi + polymarket | 0.59 | 0.0 |
| Tie is the result | Will Abha Saudi Club vs. Al Shabab Saudi Club end in a draw? | kalshi + polymarket | 0.22 | 1.0 |
| Tie is the result | Will Abha Saudi Club vs. Al Shabab Saudi Club end in a draw? | kalshi + predictfun | 0.22 | 1.0 |
| OLDBOYS- wins | Counter-Strike: OLDBOYS- vs Fire Flux Esports (BO1) - ESEA Advanced Europe Regular Season | kalshi + polymarket | 0.2 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,522) is Sports.
- Every Hyperliquid pair (159) is Sports.
- 546 pairs carry a different category on each side (451 of them point to different divisions); for example "Adam Bajurko wins" is Sports on Kalshi and Crypto on Polymarket; "Manuel Plunger wins" is Sports on Kalshi and Culture on Polymarket; "Israel wins" is Sports on Kalshi and World on Polymarket.
- 4,425 pairs have a category on one side only (side without one: Polymarket 4,425).
- 95 Kalshi–Hyperliquid pairs are matched across different dates; for example "Charlotte wins" and "NBA Regular Season: Charlotte Hornets v Cleveland Cavaliers" (Kalshi 2026-11-09, Hyperliquid 2026-11-16).
- 48 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Türkiye win on 2026-11-12?" and "UEFA Nations League A, Matchday 5: Turkiye v Belgium: Turkiye" (Polymarket 2026-11-12, Hyperliquid 2026-11-19).
- 7 Kalshi–Polymarket pairs are matched across different start times; for example "RED Canids Academy wins" and "Counter-Strike: RED Canids Academy vs Grêmio Esports (BO3) - Gamers Club Liga Série A Playoffs" (Kalshi 2026-11-08 19:00Z, Polymarket 2026-11-09 19:15Z).
- 8 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 7,395 of 8,874 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (21 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
