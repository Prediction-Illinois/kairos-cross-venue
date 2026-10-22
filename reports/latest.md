# Kairos cross-venue report, 2026-10-22

Generated 2026-10-22 16:43 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 462 | 462 | 2 of 213 | 0.9¢ (63 pairs) | 2 of 2 |
| Sports | 14,003 | 13,828 | 2 of 4,190 | 1.0¢ (1,102 pairs) | 14,921 of 14,979 |
| Crypto | 392 | 392 | 0 of 285 | 1.7¢ (63 pairs) | 69 of 69 |
| Economics & Finance | 284 | 284 | 0 of 199 | 0.9¢ (57 pairs) | 1 of 1 |
| Tech & Science | 138 | 138 | 0 of 65 | 2.0¢ (23 pairs) | 10 of 10 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 112 pairs fall outside the six divisions (Culture 112).

## Pairs

Kairos listed 15,391 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 15,216 (99%), 72 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 462 of 462 |
| Sports | Polymarket–Predict.fun | 10,584 of 10,589 |
| Sports | Kalshi–Polymarket | 2,794 of 2,862 |
| Sports | Kalshi–Predict.fun | 370 of 372 |
| Sports | Kalshi–Hyperliquid | 30 of 86 |
| Sports | Polymarket–Hyperliquid | 23 of 66 |
| Sports | Predict.fun–Hyperliquid | 27 of 28 |
| Crypto | Polymarket–Predict.fun | 392 of 392 |
| Economics & Finance | Polymarket–Predict.fun | 284 of 284 |
| Tech & Science | Polymarket–Predict.fun | 138 of 138 |
| Other | Polymarket–Predict.fun | 112 of 112 |

| Not lined up | Pairs |
|---|---|
| different dates | 156 |
| could not confirm both markets ask about the same team | 8 |
| different events | 5 |
| different start times | 3 |
| could not tell which outcome is the Kalshi YES outcome | 2 |
| could not line up the outcomes | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 213 | 146 | 15 | 2 |
| Sports | 2,794 | 8 | 2 | 1,396 | 477 | 12 | 0 |
| Crypto | 0 | 0 | 0 | 285 | 160 | 6 | 0 |
| Economics & Finance | 0 | 0 | 0 | 199 | 144 | 10 | 0 |
| Tech & Science | 0 | 0 | 0 | 65 | 52 | 5 | 0 |
| Other | 0 | 0 | 0 | 27 | 19 | 2 | 0 |

Not priced: no Predict.fun trades yet 10,157; no live quotes for Hyperliquid yet 80.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | Will John Fetterman win the 2028 Democratic presidential nomination? | Will John Fetterman win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2400 | Kairos fee quotes | 2028-11-08 |
| Elections & Politics | Polymarket–Predict.fun | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2400 | Kairos fee quotes | 2028-11-08 |
| Sports | Kalshi–Polymarket | Los Angeles C wins | Clippers vs. Thunder | YES on A + NO on B | 9.32 | $0.0055 | order books | 2026-10-25 |
| Sports | Kalshi–Polymarket | Buffalo wins | Sabres vs. Capitals | NO on A + YES on B | 0.05 | $0.0005 | order books | 2026-10-24 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 63 | 212 | 0.9¢ | 2.1¢ | 18% |
| Sports | 1,102 | 5,205 | 1.0¢ | 2.0¢ | 14% |
| Crypto | 63 | 104 | 1.7¢ | 7.3¢ | 49% |
| Economics & Finance | 57 | 163 | 0.9¢ | 5.9¢ | 29% |
| Tech & Science | 23 | 72 | 2.0¢ | 44¢ | 57% |
| Other | 10 | 41 | 0.9¢ | 2.0¢ | 20% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 63 | 0.9¢ | 2.1¢ |
| Sports | Kalshi–Polymarket | 446 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 89 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Predict.fun | 567 | 0.9¢ | 2.0¢ |
| Crypto | Polymarket–Predict.fun | 63 | 1.7¢ | 7.3¢ |
| Economics & Finance | Polymarket–Predict.fun | 57 | 0.9¢ | 5.9¢ |
| Tech & Science | Polymarket–Predict.fun | 23 | 2.0¢ | 44¢ |
| Other | Polymarket–Predict.fun | 10 | 0.9¢ | 2.0¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Tesla and SpaceX merger officially announced by December 31? | Tech & Science | Polymarket–Predict.fun | 48¢ | 7 |
| Counter-Strike: Imperial vs Turma do Pagode (BO3) - Circuit X Curitiba Group B | Sports | Kalshi–Predict.fun | 7.0¢ | 5 |
| Will Anthropic have the highest IPO Market Cap 2026? | Economics & Finance | Polymarket–Predict.fun | 5.9¢ | 5 |
| Will Theo launch a token by December 31 2026? | Crypto | Polymarket–Predict.fun | 4.7¢ | 3 |
| Counter-Strike: Quintessence vs Ryvex (BO3) - CCT Europe Challengers Series Playoffs | Sports | Kalshi–Predict.fun | 4.0¢ | 3 |
| Counter-Strike: Lavked vs HAVU (BO3) - CCT Europe Series #12 Group Stage | Sports | Kalshi–Predict.fun | 4.0¢ | 3 |
| Tesla and SpaceX merger officially announced by December 31? | Tech & Science | Polymarket–Predict.fun | 3.0¢ | 8 |
| Will Gold (XAUUSD) hit (HIGH) $4,300 in October? | Economics & Finance | Polymarket–Predict.fun | 2.9¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 1,078 of 1,808 pairs traded on both venues in the same minute, 32,451 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 4.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 522 | 21,384 | 1.0¢ | 4.0¢ |
| Polymarket–Predict.fun | 556 | 11,067 | 1.0¢ | 3.9¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Counter-Strike: Lavked vs Spirit Academy - Map 1 Winner | Polymarket–Predict.fun | 4.9¢ | 19¢ | 35 |
| Timberwolves vs. Heat: O/U 235.5 | Polymarket–Predict.fun | 4.7¢ | 13¢ | 15 |
| Warriors vs. Lakers: O/U 237.5 | Polymarket–Predict.fun | 4.0¢ | 7.0¢ | 12 |
| New Mexico State vs. Sam Houston: O/U 49.5 | Kalshi–Polymarket | 4.0¢ | 10¢ | 12 |
| Pacers vs. Pelicans: O/U 239.5 | Polymarket–Predict.fun | 4.0¢ | 9.6¢ | 13 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 31 of 40 | $1,188 |
| Elections & Politics | Predict.fun | 40 | 8 of 40 | $98.88 |
| Sports | Kalshi | 15 | 5 of 15 | $586 |
| Sports | Polymarket | 39 | 12 of 39 | $385 |
| Sports | Predict.fun | 26 | 2 of 26 | $621 |
| Crypto | Polymarket | 40 | 25 of 40 | $451 |
| Crypto | Predict.fun | 40 | 15 of 40 | $4.15 |
| Economics & Finance | Polymarket | 40 | 31 of 40 | $565 |
| Economics & Finance | Predict.fun | 40 | 8 of 40 | $33.70 |
| Tech & Science | Polymarket | 40 | 21 of 40 | $1,871 |
| Tech & Science | Predict.fun | 40 | 8 of 40 | $97.48 |
| Other | Polymarket | 40 | 31 of 40 | $52.00 |
| Other | Predict.fun | 40 | 5 of 40 | $1,081 |

## Settlement

Events that started in the last seven days: 15,061 pairs have settled on both venues and 15,003 settled the same way (100%); 333 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 2 | 2 | 0 |
| Sports | 14,979 | 14,921 | 333 |
| Crypto | 69 | 69 | 0 |
| Economics & Finance | 1 | 1 | 0 |
| Tech & Science | 10 | 10 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,317 | 5,279 |
| Polymarket | 14,798 | 14,726 |
| Predict.fun | 10,424 | 10,402 |
| Hyperliquid | 249 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs RoundsGG (BO3) - European Pro League Regular Playoffs | kalshi + polymarket | 0.59 | 0.5 |
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs RoundsGG (BO3) - European Pro League Regular Playoffs | kalshi + predictfun | 0.59 | 0.5 |
| STATE wins | Counter-Strike: STATE vs TheChampionGG (BO3) - United21 Group B | kalshi + polymarket | 0.58 | 0.5 |
| STATE wins | Counter-Strike: STATE vs TheChampionGG (BO3) - United21 Group B | kalshi + predictfun | 0.58 | 0.5 |
| RED Canids Academy wins | Counter-Strike: RED Canids Academy vs realgotis22 (BO3) - CCT South America Series 7 Group Stage | kalshi + polymarket | 0.67 | 0.5 |
| RED Canids Academy wins | Counter-Strike: RED Canids Academy vs realgotis22 (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.67 | 0.5 |
| Yellow Submarine wins | Dota 2: Yellow Submarine vs The Warriors (BO3) - EPL Masters Play-In Group B | kalshi + polymarket | 0.56 | 0.5 |
| Yellow Submarine wins | Dota 2: Yellow Submarine vs The Warriors (BO3) - EPL Masters Play-In Group B | kalshi + predictfun | 0.56 | 0.5 |
| Jerome Kym wins | Roanne: Jerome Kym vs Dominic Stephan Stricker | kalshi + polymarket | 0.55 | 0.5 |
| Elite Klan wins | Counter-Strike: Elite Klan vs Passion Academy (BO3) - United21 Group D | kalshi + polymarket | 0.46 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (3,320) is Sports.
- Every Hyperliquid pair (180) is Sports.
- 249 pairs carry a different category on each side (113 of them point to different divisions); for example "Oscar Jose Gutierrez wins" is Sports on Kalshi and Culture on Polymarket; "Duru Soke wins" is Sports on Kalshi and Crypto on Polymarket; "Will JD Gaming win the OU Gaming vs. JD Gaming Overwatch match?" is Sports on Kalshi and World on Polymarket.
- 2,401 pairs have a category on one side only (side without one: Polymarket 2,401).
- 57 Kalshi–Polymarket pairs are matched across different dates; for example "Troyes wins" and "Will ES Troyes AC win on 2026-10-24?" (Kalshi 2026-10-24, Polymarket starts 2026-10-25 16:15Z).
- 56 Kalshi–Hyperliquid pairs are matched across different dates; for example "Dortmund wins" and "Bundesliga Matchday 7: Borussia Dortmund v Eintracht Frankfurt: Borussia Dortmund" (Kalshi 2026-10-24, Hyperliquid 2026-10-31).
- 43 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Ipswich Town FC win on 2026-10-23?" and "English Premier League Matchday 8: Ipswich Town v Nottingham Forest: Ipswich Town" (Polymarket 2026-10-23, Hyperliquid 2026-10-30).
- 11 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 10,157 of 12,369 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (249 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
