# Kairos cross-venue report, 2026-10-24

Generated 2026-10-24 15:28 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 462 | 462 | 0 of 226 | 0.9¢ (47 pairs) | 2 of 2 |
| Sports | 12,268 | 12,090 | 0 of 4,183 | 1.0¢ (1,450 pairs) | 15,653 of 15,725 |
| Crypto | 390 | 390 | 0 of 288 | 1.9¢ (67 pairs) | – |
| Economics & Finance | 282 | 282 | 0 of 202 | 0.4¢ (32 pairs) | – |
| Tech & Science | 136 | 136 | 0 of 63 | 1.9¢ (21 pairs) | 4 of 4 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 112 pairs fall outside the six divisions (Culture 112).

## Pairs

Kairos listed 13,650 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 13,472 (99%), 71 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 462 of 462 |
| Sports | Polymarket–Predict.fun | 9,071 of 9,076 |
| Sports | Kalshi–Polymarket | 2,630 of 2,700 |
| Sports | Kalshi–Predict.fun | 332 of 333 |
| Sports | Kalshi–Hyperliquid | 16 of 74 |
| Sports | Polymarket–Hyperliquid | 16 of 59 |
| Sports | Predict.fun–Hyperliquid | 25 of 26 |
| Crypto | Polymarket–Predict.fun | 390 of 390 |
| Economics & Finance | Polymarket–Predict.fun | 282 of 282 |
| Tech & Science | Polymarket–Predict.fun | 136 of 136 |
| Other | Polymarket–Predict.fun | 112 of 112 |

| Not lined up | Pairs |
|---|---|
| different dates | 158 |
| could not confirm both markets ask about the same team | 7 |
| different start times | 6 |
| different events | 5 |
| could not tell which outcome is the Kalshi YES outcome | 1 |
| could not line up the outcomes | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 226 | 159 | 9 | 0 |
| Sports | 2,630 | 1 | 0 | 1,553 | 705 | 15 | 0 |
| Crypto | 0 | 0 | 0 | 288 | 161 | 4 | 0 |
| Economics & Finance | 0 | 0 | 0 | 202 | 134 | 11 | 0 |
| Tech & Science | 0 | 0 | 0 | 63 | 43 | 5 | 0 |
| Other | 0 | 0 | 0 | 35 | 24 | 6 | 0 |

Not priced: no Predict.fun trades yet 8,418; no live quotes for Hyperliquid yet 57.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 47 | 188 | 0.9¢ | 2.0¢ | 14% |
| Sports | 1,450 | 6,571 | 1.0¢ | 2.0¢ | 13% |
| Crypto | 67 | 120 | 1.9¢ | 5.0¢ | 48% |
| Economics & Finance | 32 | 127 | 0.4¢ | 3.0¢ | 18% |
| Tech & Science | 21 | 40 | 1.9¢ | 7.0¢ | 48% |
| Other | 11 | 46 | 0.9¢ | 3.3¢ | 28% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 47 | 0.9¢ | 2.0¢ |
| Sports | Kalshi–Hyperliquid | 15 | 0.7¢ | 1.1¢ |
| Sports | Kalshi–Polymarket | 587 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 110 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Hyperliquid | 11 | 0.6¢ | 1.1¢ |
| Sports | Polymarket–Predict.fun | 714 | 0.6¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 13 | 0.6¢ | 1.5¢ |
| Crypto | Polymarket–Predict.fun | 67 | 1.9¢ | 5.0¢ |
| Economics & Finance | Polymarket–Predict.fun | 32 | 0.4¢ | 3.0¢ |
| Tech & Science | Polymarket–Predict.fun | 21 | 1.9¢ | 7.0¢ |
| Other | Polymarket–Predict.fun | 11 | 0.9¢ | 3.3¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Counter-Strike: TitanFlow vs Phantom Academy (BO3) - CCT Europe Challengers Series Playoffs | Sports | Kalshi–Predict.fun | 18¢ | 3 |
| Grizzlies vs. Kings | Sports | Kalshi–Predict.fun | 8.0¢ | 3 |
| Will Xiaomi have the best Chinese AI model at the end of October 2026? | Tech & Science | Polymarket–Predict.fun | 8.0¢ | 3 |
| Counter-Strike: RED Canids Academy vs Isurus (BO3) - CCT South America Series 7 Playoffs | Sports | Kalshi–Predict.fun | 5.0¢ | 4 |
| Will Phantom launch a token by December 31, 2027? | Crypto | Polymarket–Predict.fun | 5.0¢ | 3 |
| Will Bitcoin dip to $77,500 in October? | Crypto | Polymarket–Predict.fun | 4.0¢ | 7 |
| Will NVIDIA be the largest company in the world by market cap on December 31? | Economics & Finance | Polymarket–Predict.fun | 4.0¢ | 3 |
| Tesla and SpaceX merger officially announced by December 31, 2027? | Tech & Science | Polymarket–Predict.fun | 4.0¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 1,073 of 1,919 pairs traded on both venues in the same minute, 35,348 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.6¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 571 | 23,922 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 502 | 11,426 | 1.0¢ | 4.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Overwatch: Cheeseburger vs ZETA DIVISION (BO5) - OCS Korea Stage 3 Regular Season | Kalshi–Polymarket | 6.0¢ | 22¢ | 25 |
| Valorant: FunPlus Phoenix vs Dragon Ranger Gaming - Map 2 Winner | Polymarket–Predict.fun | 5.6¢ | 20¢ | 15 |
| Valorant: Team Liquid Brazil vs Gentle Mates GC - Map 1 Winner | Polymarket–Predict.fun | 5.5¢ | 22¢ | 11 |
| Valorant: FunPlus Phoenix vs Dragon Ranger Gaming - Map 1 Winner | Polymarket–Predict.fun | 5.0¢ | 19¢ | 27 |
| Counter-Strike: Nuclear TigeRES vs ILLYRIANS - Map 1 Winner | Polymarket–Predict.fun | 4.0¢ | 11¢ | 14 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 27 of 40 | $2,466 |
| Elections & Politics | Predict.fun | 40 | 9 of 40 | $302 |
| Sports | Kalshi | 11 | 3 of 11 | $9,824 |
| Sports | Polymarket | 38 | 8 of 38 | $69.18 |
| Sports | Predict.fun | 31 | 4 of 31 | $175 |
| Crypto | Polymarket | 40 | 21 of 40 | $138 |
| Crypto | Predict.fun | 40 | 8 of 40 | $32.39 |
| Economics & Finance | Polymarket | 40 | 21 of 40 | $1,255 |
| Economics & Finance | Predict.fun | 40 | 11 of 40 | $107 |
| Tech & Science | Polymarket | 40 | 23 of 40 | $851 |
| Tech & Science | Predict.fun | 40 | 10 of 40 | $136 |
| Other | Polymarket | 40 | 21 of 40 | $956 |
| Other | Predict.fun | 40 | 5 of 40 | $84.94 |

## Settlement

Events that started in the last seven days: 15,731 pairs have settled on both venues and 15,659 settled the same way (100%); 301 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 2 | 2 | 0 |
| Sports | 15,725 | 15,653 | 301 |
| Tech & Science | 4 | 4 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,496 | 5,485 |
| Polymarket | 15,343 | 15,298 |
| Predict.fun | 10,990 | 10,952 |
| Hyperliquid | 235 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs RoundsGG (BO3) - European Pro League Regular Playoffs | kalshi + predictfun | 0.59 | 0.5 |
| STATE wins | Counter-Strike: STATE vs TheChampionGG (BO3) - United21 Group B | kalshi + predictfun | 0.58 | 0.5 |
| RED Canids Academy wins | Counter-Strike: RED Canids Academy vs realgotis22 (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.67 | 0.5 |
| Yellow Submarine wins | Dota 2: Yellow Submarine vs The Warriors (BO3) - EPL Masters Play-In Group B | kalshi + predictfun | 0.56 | 0.5 |
| Elite Klan wins | Counter-Strike: Elite Klan vs Passion Academy (BO3) - United21 Group D | kalshi + polymarket | 0.46 | 0.5 |
| Elite Klan wins | Counter-Strike: Elite Klan vs Passion Academy (BO3) - United21 Group D | kalshi + predictfun | 0.46 | 0.5 |
| Bushido Wildcats wins | Counter-Strike: Bushido Wildcats vs ex-RUSTEC (BO3) - NODWIN Clutch Series Group Stage | kalshi + predictfun | 0.41 | 0.5 |
| Bushido Wildcats wins | Counter-Strike: Bushido Wildcats vs Gothic (BO3) - CCT Europe Series #11 Group Stage | kalshi + predictfun | 0.56 | 0.5 |
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs Sökerorg (BO3) - European Pro League Regular Playoffs | kalshi + polymarket | 0.62 | 0.5 |
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs Sökerorg (BO3) - European Pro League Regular Playoffs | kalshi + predictfun | 0.62 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (3,107) is Sports.
- Every Hyperliquid pair (159) is Sports.
- 220 pairs carry a different category on each side (99 of them point to different divisions); for example "Marko Retelj wins" is Sports on Kalshi and Crypto on Polymarket; "Butler wins" is Sports on Kalshi and Culture on Polymarket; "Will a team from LPL (China) win LoL Worlds 2026?" is World on Polymarket and Esports on Predict.fun.
- 1,544 pairs have a category on one side only (side without one: Polymarket 1,544).
- 58 Kalshi–Hyperliquid pairs are matched across different dates; for example "Dortmund wins" and "Bundesliga Matchday 7: Borussia Dortmund v Eintracht Frankfurt: Borussia Dortmund" (Kalshi 2026-10-24, Hyperliquid 2026-10-31).
- 57 Kalshi–Polymarket pairs are matched across different dates; for example "Lyon wins" and "Will Olympique Lyonnais win on 2026-10-25?" (Kalshi 2026-10-25, Polymarket starts 2026-10-26 19:30Z).
- 43 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will SSC Napoli win on 2026-10-24?" and "Italian Serie A Matchday 8: Napoli v AS Roma: Napoli" (Polymarket 2026-10-24, Hyperliquid 2026-10-31).
- 9 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 8,418 of 10,810 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (235 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
