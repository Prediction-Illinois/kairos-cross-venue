# Kairos cross-venue report, 2026-10-25

Generated 2026-10-25 15:39 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 462 | 462 | 1 of 227 | 1.0¢ (44 pairs) | – |
| Sports | 11,312 | 11,124 | 1 of 3,552 | 0.8¢ (1,326 pairs) | 15,455 of 15,515 |
| Crypto | 389 | 389 | 0 of 290 | 2.0¢ (40 pairs) | – |
| Economics & Finance | 282 | 282 | 0 of 203 | 0.4¢ (36 pairs) | – |
| Tech & Science | 135 | 135 | 0 of 63 | 1.3¢ (18 pairs) | 4 of 4 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 112 pairs fall outside the six divisions (Culture 112).

## Pairs

Kairos listed 12,692 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 12,504 (99%), 86 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 462 of 462 |
| Sports | Polymarket–Predict.fun | 8,734 of 8,744 |
| Sports | Kalshi–Polymarket | 2,015 of 2,087 |
| Sports | Kalshi–Predict.fun | 328 of 351 |
| Sports | Kalshi–Hyperliquid | 13 of 62 |
| Sports | Polymarket–Hyperliquid | 13 of 46 |
| Sports | Predict.fun–Hyperliquid | 21 of 22 |
| Crypto | Polymarket–Predict.fun | 389 of 389 |
| Economics & Finance | Polymarket–Predict.fun | 282 of 282 |
| Tech & Science | Polymarket–Predict.fun | 135 of 135 |
| Other | Polymarket–Predict.fun | 112 of 112 |

| Not lined up | Pairs |
|---|---|
| different dates | 163 |
| different events | 10 |
| could not confirm both markets ask about the same team | 7 |
| different start times | 6 |
| Kalshi market is inactive | 1 |
| could not line up the outcomes | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 227 | 168 | 10 | 1 |
| Sports | 2,015 | 6 | 1 | 1,537 | 735 | 16 | 0 |
| Crypto | 0 | 0 | 0 | 290 | 156 | 3 | 0 |
| Economics & Finance | 0 | 0 | 0 | 203 | 129 | 10 | 0 |
| Tech & Science | 0 | 0 | 0 | 63 | 52 | 5 | 0 |
| Other | 0 | 0 | 0 | 35 | 22 | 6 | 0 |

Not priced: no Predict.fun trades yet 8,087; no live quotes for Hyperliquid yet 47.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2400 | Kairos fee quotes | 2028-11-08 |
| Sports | Kalshi–Polymarket | Filip Misolic wins | Guayaquil: Filip Misolic vs Martin Baquero | YES on A + NO on B | 15.38 | $0.0268 | order books | 2026-11-01 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 44 | 204 | 1.0¢ | 3.3¢ | 24% |
| Sports | 1,326 | 6,454 | 0.8¢ | 2.0¢ | 12% |
| Crypto | 40 | 76 | 2.0¢ | 8.0¢ | 51% |
| Economics & Finance | 36 | 135 | 0.4¢ | 2.0¢ | 13% |
| Tech & Science | 18 | 26 | 1.3¢ | 5.0¢ | 35% |
| Other | 10 | 44 | 0.6¢ | 4.0¢ | 27% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 44 | 1.0¢ | 3.3¢ |
| Sports | Kalshi–Hyperliquid | 13 | 0.5¢ | 1.4¢ |
| Sports | Kalshi–Polymarket | 476 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 73 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Hyperliquid | 13 | 0.5¢ | 1.3¢ |
| Sports | Polymarket–Predict.fun | 734 | 0.5¢ | 1.9¢ |
| Sports | Predict.fun–Hyperliquid | 17 | 0.5¢ | 1.5¢ |
| Crypto | Polymarket–Predict.fun | 40 | 2.0¢ | 8.0¢ |
| Economics & Finance | Polymarket–Predict.fun | 36 | 0.4¢ | 2.0¢ |
| Tech & Science | Polymarket–Predict.fun | 18 | 1.3¢ | 5.0¢ |
| Other | Polymarket–Predict.fun | 10 | 0.6¢ | 4.0¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Counter-Strike: Quintessence vs TitanFlow (BO3) - CCT Europe Challengers Series Playoffs | Sports | Kalshi–Predict.fun | 17¢ | 3 |
| KBO Playoff: Kia Tigers vs. Samsung Lions | Sports | Kalshi–Polymarket | 12¢ | 5 |
| Dota 2: Nemiga Gaming vs Inner Circle (BO3) - EPL Masters Group A | Sports | Kalshi–Predict.fun | 9.0¢ | 3 |
| Tori FDV above $100M one day after launch? | Crypto | Polymarket–Predict.fun | 5.5¢ | 3 |
| Will Ilija Srdanović be the next prime minister of Serbia? | Elections & Politics | Polymarket–Predict.fun | 5.3¢ | 5 |
| Will You Can See Everything win Best Picture at the 99th Academy Awards? | Other | Polymarket–Predict.fun | 4.4¢ | 3 |
| Will Dune: Part Three win Best Picture at the 99th Academy Awards? | Other | Polymarket–Predict.fun | 3.4¢ | 3 |
| Will Aleksandar Vučić be the next Prime Minister of Serbia? | Elections & Politics | Polymarket–Predict.fun | 3.2¢ | 4 |

## Sports around game time

Games that started 6 to 30 hours ago: 1,976 of 4,562 pairs traded on both venues in the same minute, 46,657 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 1,063 | 28,927 | 1.0¢ | 3.0¢ |
| Polymarket–Hyperliquid | 3 | 48 | 0.4¢ | 3.0¢ |
| Polymarket–Predict.fun | 910 | 17,682 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Overwatch: Poker Face vs ZANSIDE GAMING (BO5) - OCS Korea Stage 3 Regular Season | Kalshi–Polymarket | 10¢ | 33¢ | 10 |
| Counter-Strike: XI Esport vs Wingman (BO3) - Exort Fiesta Closed Qualifier: Series #3 Play-In | Polymarket–Predict.fun | 7.3¢ | 15¢ | 11 |
| Overwatch: Virtus.pro vs Twisted Minds (BO5) - OCS EMEA Stage 3 Group Stage | Kalshi–Polymarket | 6.2¢ | 29¢ | 17 |
| Wizards vs. Bulls: O/U 238.5 | Polymarket–Predict.fun | 6.0¢ | 29¢ | 10 |
| Counter-Strike: Donstu Esports vs Quintessence - Map 1 Winner | Polymarket–Predict.fun | 5.0¢ | 9.8¢ | 13 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 28 of 40 | $1,192 |
| Elections & Politics | Predict.fun | 40 | 4 of 40 | $38,727 |
| Sports | Kalshi | 10 | 7 of 10 | $144 |
| Sports | Polymarket | 39 | 13 of 39 | $800 |
| Sports | Predict.fun | 31 | 5 of 31 | $986 |
| Crypto | Polymarket | 40 | 20 of 40 | $366 |
| Crypto | Predict.fun | 40 | 12 of 40 | $170 |
| Economics & Finance | Polymarket | 40 | 17 of 40 | $200 |
| Economics & Finance | Predict.fun | 40 | 6 of 40 | $394 |
| Tech & Science | Polymarket | 40 | 23 of 40 | $293 |
| Tech & Science | Predict.fun | 40 | 7 of 40 | $280 |
| Other | Polymarket | 40 | 17 of 40 | $838 |
| Other | Predict.fun | 40 | 4 of 40 | $2,253 |

## Settlement

Events that started in the last seven days: 15,519 pairs have settled on both venues and 15,459 settled the same way (100%); 509 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Sports | 15,515 | 15,455 | 509 |
| Tech & Science | 4 | 4 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,379 | 5,127 |
| Polymarket | 15,333 | 15,267 |
| Predict.fun | 11,150 | 11,114 |
| Hyperliquid | 194 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| RED Canids Academy wins | Counter-Strike: RED Canids Academy vs realgotis22 (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.67 | 0.5 |
| Yellow Submarine wins | Dota 2: Yellow Submarine vs The Warriors (BO3) - EPL Masters Play-In Group B | kalshi + predictfun | 0.56 | 0.5 |
| Elite Klan wins | Counter-Strike: Elite Klan vs Passion Academy (BO3) - United21 Group D | kalshi + predictfun | 0.46 | 0.5 |
| Bushido Wildcats wins | Counter-Strike: Bushido Wildcats vs Gothic (BO3) - CCT Europe Series #11 Group Stage | kalshi + predictfun | 0.56 | 0.5 |
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs Sökerorg (BO3) - European Pro League Regular Playoffs | kalshi + predictfun | 0.62 | 0.5 |
| Stray Team wins | Dota 2: Stray Team vs Korb3n Team (BO3) - 1win Streamers League #3 Playoffs | kalshi + predictfun | 0.45 | 0.5 |
| Hacha Esports wins | Counter-Strike: Hacha Esports vs Los Niños (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.34 | 0.5 |
| Holger Rune wins | European Open: Holger Rune vs Raphael Collignon | kalshi + polymarket | 0.6 | 0.5 |
| Botic Van de Zandschulp wins | European Open: Botic van de Zandschulp vs Kamil Majchrzak | kalshi + polymarket | 0.62 | 0.5 |
| Gremio Esports wins | Counter-Strike: Grêmio Esports vs SUKEBAN (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.55 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,500) is Sports.
- Every Hyperliquid pair (130) is Sports.
- 218 pairs carry a different category on each side (92 of them point to different divisions); for example "Kilian Dallapiazza wins" is Sports on Kalshi and Crypto on Polymarket; "Drake wins" is Sports on Kalshi and Culture on Polymarket; "Will a team from LPL (China) win LoL Worlds 2026?" is World on Polymarket and Esports on Predict.fun.
- 1,379 pairs have a category on one side only (side without one: Polymarket 1,379).
- 58 Kalshi–Polymarket pairs are matched across different dates; for example "Alibek Kachmazov wins" and "Seoul: Alibek Kachmazov vs Woobin Shin" (Kalshi 2026-10-25, Polymarket starts 2026-10-27 04:00Z).
- 49 Kalshi–Hyperliquid pairs are matched across different dates; for example "Bayern Munich wins" and "Bundesliga Matchday 7: SC Freiburg v FC Bayern Munich: FC Bayern Munich" (Kalshi 2026-10-25, Hyperliquid 2026-11-01).
- 33 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Crystal Palace FC win on 2026-10-25?" and "English Premier League Matchday 8: Crystal Palace v Newcastle United: Crystal Palace" (Polymarket 2026-10-25, Hyperliquid 2026-11-01).
- 9 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 8,087 of 10,463 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (194 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
