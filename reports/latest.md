# Kairos cross-venue report, 2026-11-17

Generated 2026-11-17 20:32 UTC from Kairos's catalog of linked markets, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 767 | 424 | 2 of 199 | 0.4¢ (18 pairs) | 10 of 10 |
| Sports | 3,028 | 2,633 | 1 of 1,343 | 1.0¢ (470 pairs) | 12,156 of 12,192 |
| Crypto | 1,198 | 1,196 | 0 of 314 | 1.9¢ (61 pairs) | 1,278 of 1,425 |
| Economics & Finance | 571 | 509 | 0 of 212 | 0.9¢ (44 pairs) | 84 of 87 |
| Tech & Science | 235 | 234 | 1 of 63 | 2.0¢ (16 pairs) | 95 of 95 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 483 pairs fall outside the six divisions (Culture 384, Entertainment 138, Financials 26, Science and Technology 2).

## Pairs

Kairos listed 6,282 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 5,313 (85%), 66 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 424 of 425 |
| Elections & Politics | Kalshi–Polymarket | 0 of 171 |
| Elections & Politics | Kalshi–Predict.fun | 0 of 171 |
| Sports | Polymarket–Predict.fun | 1,243 of 1,243 |
| Sports | Kalshi–Polymarket | 985 of 996 |
| Sports | Kalshi–Predict.fun | 362 of 526 |
| Sports | Polymarket–Hyperliquid | 0 of 88 |
| Sports | Predict.fun–Hyperliquid | 43 of 88 |
| Sports | Kalshi–Hyperliquid | 0 of 87 |
| Crypto | Polymarket–Predict.fun | 1,196 of 1,196 |
| Crypto | Kalshi–Polymarket | 0 of 2 |
| Economics & Finance | Polymarket–Predict.fun | 509 of 509 |
| Economics & Finance | Kalshi–Predict.fun | 0 of 44 |
| Economics & Finance | Kalshi–Polymarket | 0 of 18 |
| Tech & Science | Polymarket–Predict.fun | 234 of 234 |
| Tech & Science | Kalshi–Predict.fun | 0 of 1 |
| Other | Polymarket–Predict.fun | 317 of 317 |
| Other | Kalshi–Polymarket | 0 of 99 |
| Other | Kalshi–Predict.fun | 0 of 67 |

| Not lined up | Pairs |
|---|---|
| not a sports market; questions not compared | 574 |
| different dates | 179 |
| could not confirm both markets ask about the same team | 161 |
| could not line up the outcomes | 46 |
| Kalshi market is inactive | 5 |
| Kalshi market is finalized | 3 |
| different start times | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 199 | 146 | 14 | 2 |
| Sports | 985 | 9 | 1 | 358 | 63 | 2 | 0 |
| Crypto | 0 | 0 | 0 | 314 | 169 | 5 | 0 |
| Economics & Finance | 0 | 0 | 0 | 212 | 158 | 17 | 0 |
| Tech & Science | 0 | 0 | 0 | 63 | 41 | 5 | 1 |
| Other | 0 | 0 | 0 | 63 | 38 | 7 | 0 |

Not priced: no Predict.fun trades yet 3,076; no live quotes for Hyperliquid yet 43.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Tech & Science | Polymarket–Predict.fun | Tesla and SpaceX merger officially announced by December 31? | Tesla and SpaceX merger officially announced by December 31, 2027? | YES on A + NO on B | 250.0 | $96.5830 | Kairos fee quotes | 2027-01-01 |
| Elections & Politics | Polymarket–Predict.fun | Will Sarah Knafo win the 2027 French presidential election? | Will Sarah Knafo win the 2027 French presidential election? | YES on A + NO on B | 250.0 | $0.2300 | Kairos fee quotes | 2027-04-19 |
| Sports | Kalshi–Polymarket | Ella Haavisto wins | W50 Funchal: Ella Haavisto vs Beatriz Castro | YES on A + NO on B | 8.0 | $0.0859 | order books | 2026-11-25 |
| Elections & Politics | Polymarket–Predict.fun | Will James Talarico win the 2028 US Presidential Election? | Will James Talarico win the 2028 US Presidential Election? | YES on A + NO on B | 10.0 | $0.0397 | Kairos fee quotes | 2028-11-08 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 18 | 41 | 0.4¢ | 2.5¢ | 15% |
| Sports | 470 | 2,812 | 1.0¢ | 2.0¢ | 17% |
| Crypto | 61 | 87 | 1.9¢ | 9.9¢ | 47% |
| Economics & Finance | 44 | 192 | 0.9¢ | 3.4¢ | 23% |
| Tech & Science | 16 | 25 | 2.0¢ | 12¢ | 52% |
| Other | 22 | 63 | 0.3¢ | 4.1¢ | 24% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 18 | 0.4¢ | 2.5¢ |
| Sports | Kalshi–Polymarket | 267 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 55 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Predict.fun | 119 | 1.0¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 29 | 0.9¢ | 2.3¢ |
| Crypto | Polymarket–Predict.fun | 61 | 1.9¢ | 9.9¢ |
| Economics & Finance | Polymarket–Predict.fun | 44 | 0.9¢ | 3.4¢ |
| Tech & Science | Polymarket–Predict.fun | 16 | 2.0¢ | 12¢ |
| Other | Polymarket–Predict.fun | 22 | 0.3¢ | 4.1¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Dota 2: angry birds vs Spirit Academy (BO3) - Asgard Championship Playoffs | Sports | Kalshi–Predict.fun | 10¢ | 5 |
| Will Nvidia (NVDA) beat quarterly earnings? | Economics & Finance | Polymarket–Predict.fun | 5.4¢ | 10 |
| Variational FDV above $2B one day after launch? | Crypto | Polymarket–Predict.fun | 4.6¢ | 4 |
| Jensen Huang rejoins NVIDIA before divorce? | Other | Polymarket–Predict.fun | 4.4¢ | 3 |
| Will Anthropic’s market cap be between 1.2T and 1.5T at market close on IPO day by December 31 2027? | Economics & Finance | Polymarket–Predict.fun | 3.1¢ | 11 |
| Counter-Strike: Grêmio Esports vs Mira (BO3) - Gamers Club Liga Série A Group A | Sports | Kalshi–Polymarket | 2.8¢ | 4 |
| Will Jensen Huang rejoin NVIDIA by December 31, 2027? | Economics & Finance | Polymarket–Predict.fun | 2.4¢ | 11 |
| Base FDV above $2B one day after launch? | Crypto | Polymarket–Predict.fun | 2.3¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 894 of 1,927 pairs traded on both venues in the same minute, 28,247 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 411 | 19,051 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 483 | 9,196 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Counter-Strike: BRUTE SQ vs STATE (BO3) - United21 Playoffs | Kalshi–Polymarket | 7.0¢ | 11¢ | 12 |
| Valorant: XJG vs Hyper Tide Gaming (BO3) - China National Tournament Split Omega: Pro Division Group B | Polymarket–Predict.fun | 5.0¢ | 23¢ | 12 |
| Counter-Strike: Leo Team vs Honvéd (BO3) - CCT Europe Group Stage | Kalshi–Polymarket | 5.0¢ | 11¢ | 18 |
| Counter-Strike: Teletubisie vs NAVI Junior - Map 2 Winner | Polymarket–Predict.fun | 4.3¢ | 15¢ | 12 |
| Counter-Strike: Team Bratishkin vs Team PCH3LK1N - Map 2 Winner | Polymarket–Predict.fun | 4.3¢ | 18¢ | 16 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 29 of 40 | $651 |
| Elections & Politics | Predict.fun | 40 | 2 of 40 | $54.30 |
| Sports | Kalshi | 21 | 16 of 21 | $71.38 |
| Sports | Polymarket | 32 | 9 of 32 | $166 |
| Sports | Predict.fun | 26 | 6 of 26 | $355 |
| Sports | Hyperliquid | 1 | 1 of 1 | $23,797 |
| Crypto | Polymarket | 40 | 5 of 40 | $97.64 |
| Crypto | Predict.fun | 40 | 2 of 40 | $59.12 |
| Economics & Finance | Polymarket | 40 | 31 of 40 | $494 |
| Economics & Finance | Predict.fun | 40 | 5 of 40 | $122 |
| Tech & Science | Polymarket | 40 | 32 of 40 | $1,289 |
| Tech & Science | Predict.fun | 40 | 5 of 40 | $18.89 |
| Other | Polymarket | 40 | 31 of 40 | $22.60 |
| Other | Predict.fun | 40 | 1 of 40 | $44.08 |

## Settlement

Events that started in the last seven days: 13,873 pairs have settled on both venues and 13,687 settled the same way (99%); 233 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 10 | 10 | 2 |
| Sports | 12,192 | 12,156 | 189 |
| Crypto | 1,425 | 1,278 | 0 |
| Economics & Finance | 87 | 84 | 0 |
| Tech & Science | 95 | 95 | 42 |
| Other | 64 | 64 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 3,542 | 3,518 |
| Polymarket | 13,551 | 13,357 |
| Predict.fun | 11,096 | 10,918 |
| Hyperliquid | 23 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Alejandro Davidovich Fokina wins | Rolex Paris Masters: Alejandro Davidovich Fokina vs Moise Kouame | kalshi + predictfun | 0.74 | 0.5 |
| Daniel Merida wins | Rolex Paris Masters: Daniel Merida Aguilar vs Alexander Blockx | kalshi + predictfun | 0.42 | 0.5 |
| Stefanos Tsitsipas wins | Rolex Paris Masters: Stefanos Tsitsipas vs Learner Tien | kalshi + predictfun | 0.45 | 0.5 |
| Nazim Sadykhov wins | UFC 334: Nazim Sadykhov vs. Jefferson Nascimento (Lightweight, Early Prelims) | kalshi + polymarket | 0.7 | 0.5 |
| Adrian Yanez wins | UFC 334: Adrian Yañez vs. Juan Diaz (Bantamweight, Early Prelims) | kalshi + polymarket | 0.53 | 0.5 |
| FORZE Reload wins | Counter-Strike: FORZE Reload vs maybe (BO3) - CCT Europe Group Stage | kalshi + predictfun | 0.64 | 0.5 |
| Braden Shick wins | Knoxville: Braden Shick vs Andres Andrade | kalshi + polymarket | 0.64 | 0.5 |
| Young TigeRES wins | Counter-Strike: Young TigeRES vs DINERO (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.66 | 1.0 |
| James McCabe wins | Brisbane 3: James McCabe vs Jan Kumstat | kalshi + polymarket | 0.35 | 0.5 |
| NAVI Junior wins | Counter-Strike: NAVI Junior vs Sökerorg (BO3) - European Pro League Group C | kalshi + predictfun | 0.63 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Hyperliquid pair (263) is Sports.
- 485 pairs carry a different category on each side (148 of them point to different divisions); for example "Kashiwa wins" is Sports on Kalshi and Crypto on Polymarket; "Will Bitcoin have the best performance in 2026?" is Crypto on Polymarket and Finance on Predict.fun; "Will the Fed cut rates 1 times?" is Economics on Kalshi and Politics on Predict.fun.
- 2,600 pairs have a category on one side only (side without one: Polymarket 2,600).
- 88 Polymarket–Hyperliquid pairs are matched across different dates; for example "UEFA Nations League A, Matchday 6: Denmark v Norway: Norway" and "Will Norway win on 2026-11-17?" (Polymarket 2026-11-17, Hyperliquid 2026-11-24).
- 87 Kalshi–Hyperliquid pairs are matched across different dates; for example "UEFA Nations League A, Matchday 6: Denmark v Norway: Norway" and "Norway wins" (Kalshi 2026-11-17, Hyperliquid 2026-11-24).
- 4 Kalshi–Polymarket pairs are matched across different dates; for example "Alexander Zverev wins" and "ATP World Tour Finals, John McEnroe Group: Alexander Zverev vs Arthur Fils" (Kalshi 2026-11-17, Polymarket starts 2026-11-19 13:00Z).
- 789 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 3,076 of 4,328 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (23 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos's approved links (`/market-links`; `/matched-markets` until 11 November 2026), every two venues of a link making one pair, and outside sports from Kairos's equivalence clusters around every non-sports Predict.fun market; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
