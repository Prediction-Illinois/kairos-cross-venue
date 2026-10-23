# Kairos cross-venue report, 2026-10-23

Generated 2026-10-23 16:34 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 462 | 462 | 1 of 223 | 0.9¢ (49 pairs) | 2 of 2 |
| Sports | 12,065 | 11,887 | 4 of 4,153 | 1.0¢ (1,220 pairs) | 15,938 of 16,006 |
| Crypto | 392 | 392 | 0 of 286 | 2.0¢ (53 pairs) | 3 of 3 |
| Economics & Finance | 282 | 282 | 0 of 202 | 0.7¢ (43 pairs) | – |
| Tech & Science | 137 | 137 | 0 of 64 | 2.2¢ (30 pairs) | 5 of 5 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 112 pairs fall outside the six divisions (Culture 112).

## Pairs

Kairos listed 13,450 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 13,272 (99%), 65 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 462 of 462 |
| Sports | Polymarket–Predict.fun | 8,725 of 8,731 |
| Sports | Kalshi–Polymarket | 2,752 of 2,821 |
| Sports | Kalshi–Predict.fun | 353 of 355 |
| Sports | Kalshi–Hyperliquid | 16 of 73 |
| Sports | Polymarket–Hyperliquid | 16 of 59 |
| Sports | Predict.fun–Hyperliquid | 25 of 26 |
| Crypto | Polymarket–Predict.fun | 392 of 392 |
| Economics & Finance | Polymarket–Predict.fun | 282 of 282 |
| Tech & Science | Polymarket–Predict.fun | 137 of 137 |
| Other | Polymarket–Predict.fun | 112 of 112 |

| Not lined up | Pairs |
|---|---|
| different dates | 157 |
| could not confirm both markets ask about the same team | 8 |
| different events | 6 |
| different start times | 4 |
| could not tell which outcome is the Kalshi YES outcome | 2 |
| could not line up the outcomes | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 223 | 161 | 17 | 1 |
| Sports | 2,752 | 5 | 4 | 1,401 | 499 | 11 | 0 |
| Crypto | 0 | 0 | 0 | 286 | 148 | 4 | 0 |
| Economics & Finance | 0 | 0 | 0 | 202 | 141 | 11 | 0 |
| Tech & Science | 0 | 0 | 0 | 64 | 47 | 5 | 0 |
| Other | 0 | 0 | 0 | 31 | 19 | 2 | 0 |

Not priced: no Predict.fun trades yet 8,256; no live quotes for Hyperliquid yet 57.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2400 | Kairos fee quotes | 2028-11-08 |
| Sports | Kalshi–Polymarket | Philadelphia wins | Flyers vs. Capitals | NO on A + YES on B | 5.09 | $0.0183 | order books | 2026-10-28 |
| Sports | Kalshi–Polymarket | Memphis wins | Grizzlies vs. Kings | NO on A + YES on B | 5.05 | $0.0127 | order books | 2026-10-26 |
| Sports | Kalshi–Polymarket | OldBoys wins | Counter-Strike: OldBoys vs Hermine Esports Club (BO1) - ESEA Advanced Europe Regular Season | NO on A + YES on B | 100.0 | $0.0117 | order books | 2026-10-24 |
| Sports | Kalshi–Polymarket | Tie is the result | Will FC Juárez vs. Querétaro FC end in a draw? | YES on A + NO on B | 0.01 | $0.0006 | order books | 2026-10-31 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 49 | 190 | 0.9¢ | 2.0¢ | 18% |
| Sports | 1,220 | 5,844 | 1.0¢ | 2.0¢ | 15% |
| Crypto | 53 | 86 | 2.0¢ | 8.1¢ | 58% |
| Economics & Finance | 43 | 165 | 0.7¢ | 4.2¢ | 29% |
| Tech & Science | 30 | 65 | 2.2¢ | 6.0¢ | 58% |
| Other | 9 | 39 | 1.0¢ | 2.8¢ | 26% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 49 | 0.9¢ | 2.0¢ |
| Sports | Kalshi–Hyperliquid | 6 | 1.0¢ | 1.5¢ |
| Sports | Kalshi–Polymarket | 528 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 98 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Hyperliquid | 5 | 0.5¢ | 1.1¢ |
| Sports | Polymarket–Predict.fun | 570 | 0.9¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 13 | 0.7¢ | 1.5¢ |
| Crypto | Polymarket–Predict.fun | 53 | 2.0¢ | 8.1¢ |
| Economics & Finance | Polymarket–Predict.fun | 43 | 0.7¢ | 4.2¢ |
| Tech & Science | Polymarket–Predict.fun | 30 | 2.2¢ | 6.0¢ |
| Other | Polymarket–Predict.fun | 9 | 1.0¢ | 2.8¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Will Gold (XAUUSD) hit (LOW) $3,900 in October? | Economics & Finance | Polymarket–Predict.fun | 8.9¢ | 3 |
| Will Solana hit $60 or $140 first? | Crypto | Polymarket–Predict.fun | 5.1¢ | 7 |
| Will Moonshot have the best Chinese AI model at the end of October 2026? | Tech & Science | Polymarket–Predict.fun | 5.0¢ | 3 |
| Tesla and SpaceX merger officially announced by December 31, 2027? | Tech & Science | Polymarket–Predict.fun | 4.5¢ | 5 |
| Will Apple be the largest company in the world by market cap on December 31? | Economics & Finance | Polymarket–Predict.fun | 4.2¢ | 5 |
| Pelicans vs. Nuggets | Sports | Kalshi–Predict.fun | 4.0¢ | 3 |
| Yokohama BayStars vs. Fukuoka SoftBank Hawks | Sports | Kalshi–Polymarket | 4.0¢ | 8 |
| Pelicans vs. Nuggets | Sports | Polymarket–Predict.fun | 4.0¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 989 of 3,276 pairs traded on both venues in the same minute, 28,183 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 414 | 18,039 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 575 | 10,144 | 1.0¢ | 3.6¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| KHL: HC Sochi vs. Dinamo Minsk | Kalshi–Polymarket | 9.0¢ | 43¢ | 14 |
| Valorant: Nova Esports vs Any Questions Gaming - Map 1 Winner | Polymarket–Predict.fun | 5.5¢ | 24¢ | 19 |
| Counter-Strike: Banger Gang vs Privateer Gaming (BO1) - ESEA Advanced Europe Regular Season | Kalshi–Polymarket | 5.0¢ | 12¢ | 14 |
| Valorant: TEC Esports vs Unsettled Resentment - Map 1 Winner | Polymarket–Predict.fun | 5.0¢ | 9.4¢ | 11 |
| Valorant: TEC Esports vs Unsettled Resentment - Map 2 Winner | Polymarket–Predict.fun | 5.0¢ | 37¢ | 28 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 29 of 40 | $1,117 |
| Elections & Politics | Predict.fun | 40 | 8 of 40 | $73.15 |
| Sports | Kalshi | 7 | 4 of 7 | $746 |
| Sports | Polymarket | 38 | 12 of 38 | $87.83 |
| Sports | Predict.fun | 35 | 7 of 35 | $111 |
| Crypto | Polymarket | 40 | 17 of 40 | $182 |
| Crypto | Predict.fun | 40 | 5 of 40 | $251 |
| Economics & Finance | Polymarket | 40 | 23 of 40 | $509 |
| Economics & Finance | Predict.fun | 40 | 8 of 40 | $168 |
| Tech & Science | Polymarket | 40 | 24 of 40 | $289 |
| Tech & Science | Predict.fun | 40 | 13 of 40 | $209 |
| Other | Polymarket | 40 | 28 of 40 | $1,223 |
| Other | Predict.fun | 40 | 4 of 40 | $20,342 |

## Settlement

Events that started in the last seven days: 16,016 pairs have settled on both venues and 15,948 settled the same way (100%); 296 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 2 | 2 | 0 |
| Sports | 16,006 | 15,938 | 296 |
| Crypto | 3 | 3 | 0 |
| Tech & Science | 5 | 5 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,384 | 5,374 |
| Polymarket | 15,675 | 15,641 |
| Predict.fun | 11,321 | 11,291 |
| Hyperliquid | 244 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs RoundsGG (BO3) - European Pro League Regular Playoffs | kalshi + predictfun | 0.59 | 0.5 |
| STATE wins | Counter-Strike: STATE vs TheChampionGG (BO3) - United21 Group B | kalshi + predictfun | 0.58 | 0.5 |
| RED Canids Academy wins | Counter-Strike: RED Canids Academy vs realgotis22 (BO3) - CCT South America Series 7 Group Stage | kalshi + polymarket | 0.67 | 0.5 |
| RED Canids Academy wins | Counter-Strike: RED Canids Academy vs realgotis22 (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.67 | 0.5 |
| Yellow Submarine wins | Dota 2: Yellow Submarine vs The Warriors (BO3) - EPL Masters Play-In Group B | kalshi + predictfun | 0.56 | 0.5 |
| Elite Klan wins | Counter-Strike: Elite Klan vs Passion Academy (BO3) - United21 Group D | kalshi + polymarket | 0.46 | 0.5 |
| Elite Klan wins | Counter-Strike: Elite Klan vs Passion Academy (BO3) - United21 Group D | kalshi + predictfun | 0.46 | 0.5 |
| Bushido Wildcats wins | Counter-Strike: Bushido Wildcats vs ex-RUSTEC (BO3) - NODWIN Clutch Series Group Stage | kalshi + predictfun | 0.41 | 0.5 |
| Bushido Wildcats wins | Counter-Strike: Bushido Wildcats vs Gothic (BO3) - CCT Europe Series #11 Group Stage | kalshi + polymarket | 0.56 | 0.5 |
| Bushido Wildcats wins | Counter-Strike: Bushido Wildcats vs Gothic (BO3) - CCT Europe Series #11 Group Stage | kalshi + predictfun | 0.56 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (3,249) is Sports.
- Every Hyperliquid pair (158) is Sports.
- 240 pairs carry a different category on each side (111 of them point to different divisions); for example "Oscar Jose Gutierrez wins" is Sports on Kalshi and Culture on Polymarket; "Madison Brengle wins" is Sports on Kalshi and Crypto on Polymarket; "Will JD Gaming win the OU Gaming vs. JD Gaming Overwatch match?" is Sports on Kalshi and World on Polymarket.
- 1,628 pairs have a category on one side only (side without one: Polymarket 1,628).
- 57 Kalshi–Hyperliquid pairs are matched across different dates; for example "Dortmund wins" and "Bundesliga Matchday 7: Borussia Dortmund v Eintracht Frankfurt: Borussia Dortmund" (Kalshi 2026-10-24, Hyperliquid 2026-10-31).
- 57 Kalshi–Polymarket pairs are matched across different dates; for example "Troyes wins" and "Will ES Troyes AC win on 2026-10-24?" (Kalshi 2026-10-24, Polymarket starts 2026-10-25 16:15Z).
- 43 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Ipswich Town FC win on 2026-10-23?" and "English Premier League Matchday 8: Ipswich Town v Nottingham Forest: Ipswich Town" (Polymarket 2026-10-23, Hyperliquid 2026-10-30).
- 11 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 8,256 of 10,488 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (244 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
