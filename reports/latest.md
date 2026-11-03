# Kairos cross-venue report, 2026-11-03

Generated 2026-11-03 19:09 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 486 | 486 | 0 of 254 | 0.9¢ (86 pairs) | 5 of 5 |
| Sports | 13,634 | 13,527 | 22 of 3,718 | 1.0¢ (943 pairs) | 16,179 of 16,222 |
| Crypto | 394 | 394 | 0 of 254 | 2.0¢ (31 pairs) | 64 of 64 |
| Economics & Finance | 233 | 233 | 0 of 181 | 1.0¢ (23 pairs) | 62 of 62 |
| Tech & Science | 76 | 76 | 0 of 48 | 2.9¢ (1 pairs) | 58 of 58 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 93 pairs fall outside the six divisions (Culture 93).

## Pairs

Kairos listed 14,916 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 14,809 (99%), 83 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 486 of 486 |
| Sports | Polymarket–Predict.fun | 10,608 of 10,608 |
| Sports | Kalshi–Polymarket | 2,539 of 2,565 |
| Sports | Kalshi–Predict.fun | 367 of 372 |
| Sports | Polymarket–Hyperliquid | 0 of 43 |
| Sports | Kalshi–Hyperliquid | 0 of 33 |
| Sports | Predict.fun–Hyperliquid | 13 of 13 |
| Crypto | Polymarket–Predict.fun | 394 of 394 |
| Economics & Finance | Polymarket–Predict.fun | 233 of 233 |
| Tech & Science | Polymarket–Predict.fun | 76 of 76 |
| Other | Polymarket–Predict.fun | 93 of 93 |

| Not lined up | Pairs |
|---|---|
| different dates | 91 |
| different start times | 7 |
| could not confirm both markets ask about the same team | 5 |
| Kalshi market is inactive | 2 |
| could not tell which outcome is the Kalshi YES outcome | 1 |
| name and team-code checks point to different outcomes | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 254 | 162 | 10 | 0 |
| Sports | 2,539 | 31 | 22 | 1,179 | 531 | 15 | 0 |
| Crypto | 0 | 0 | 0 | 254 | 136 | 3 | 0 |
| Economics & Finance | 0 | 0 | 0 | 181 | 116 | 14 | 0 |
| Tech & Science | 0 | 0 | 0 | 48 | 34 | 2 | 0 |
| Other | 0 | 0 | 0 | 28 | 20 | 6 | 0 |

Not priced: no Predict.fun trades yet 10,313; no live quotes for Hyperliquid yet 13.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Tie is the result | Will Abha Saudi Club vs. Al Shabab Saudi Club end in a draw? | YES on A + NO on B | 7661.22 | $3643.2410 | order books | 2026-11-05 |
| Sports | Kalshi–Polymarket | Tie is the result | Will Al Qadisiyah Saudi Club vs. Al Fayha Saudi Club end in a draw? | YES on A + NO on B | 9277.28 | $2743.2639 | order books | 2026-11-05 |
| Sports | Kalshi–Polymarket | Al Qadsiah wins | Will Al Qadisiyah Saudi Club win on 2026-11-05? | NO on A + YES on B | 4346.94 | $1839.4174 | order books | 2026-11-05 |
| Sports | Kalshi–Polymarket | Tie is the result | Will Al Faisaly Saudi Club vs. Al Diraiyah Saudi Club end in a draw? | YES on A + NO on B | 3207.18 | $1025.7314 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Al-Shabab wins | Will Al Shabab Saudi Club win on 2026-11-05? | NO on A + YES on B | 3898.63 | $997.8252 | order books | 2026-11-05 |
| Sports | Kalshi–Polymarket | Tie is the result | Will Al Fateh Saudi Club vs. Al Riyadh Saudi Club end in a draw? | YES on A + NO on B | 4040.59 | $705.1866 | order books | 2026-11-06 |
| Sports | Kalshi–Polymarket | Will over 5.5 goals be scored? | Abha Saudi Club vs. Al Shabab Saudi Club: O/U 5.5 | YES on A + NO on B | 1429.29 | $250.5788 | order books | 2026-11-05 |
| Sports | Kalshi–Polymarket | Abha wins | Will Abha Saudi Club win on 2026-11-05? | NO on A + YES on B | 4678.06 | $162.1296 | order books | 2026-11-05 |
| Sports | Kalshi–Polymarket | Al-Fateh wins | Will Al Fateh Saudi Club win on 2026-11-06? | NO on A + YES on B | 3049.14 | $126.6872 | order books | 2026-11-06 |
| Sports | Kalshi–Polymarket | Diriyah Club wins | Will Al Diraiyah Saudi Club win on 2026-11-07? | NO on A + YES on B | 820.86 | $41.1016 | order books | 2026-11-07 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 86 | 431 | 0.9¢ | 2.0¢ | 13% |
| Sports | 943 | 4,846 | 1.0¢ | 3.0¢ | 20% |
| Crypto | 31 | 40 | 2.0¢ | 5.9¢ | 52% |
| Economics & Finance | 23 | 55 | 1.0¢ | 9.1¢ | 33% |
| Tech & Science | 1 | 2 | 2.9¢ | 5.5¢ | 100% |
| Other | 3 | 27 | 1.1¢ | 1.9¢ | 7% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 86 | 0.9¢ | 2.0¢ |
| Sports | Kalshi–Polymarket | 370 | 1.0¢ | 3.0¢ |
| Sports | Kalshi–Predict.fun | 61 | 1.0¢ | 5.0¢ |
| Sports | Polymarket–Predict.fun | 501 | 0.6¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 11 | 0.6¢ | 1.1¢ |
| Crypto | Polymarket–Predict.fun | 31 | 2.0¢ | 5.9¢ |
| Economics & Finance | Polymarket–Predict.fun | 23 | 1.0¢ | 9.1¢ |
| Tech & Science | Polymarket–Predict.fun | 1 | 2.9¢ | 5.5¢ |
| Other | Polymarket–Predict.fun | 3 | 1.1¢ | 1.9¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Will Al Qadisiyah Saudi Club vs. Al Fayha Saudi Club end in a draw? | Sports | Kalshi–Polymarket | 71¢ | 7 |
| Will Abha Saudi Club vs. Al Shabab Saudi Club end in a draw? | Sports | Kalshi–Polymarket | 62¢ | 9 |
| Will Al Faisaly Saudi Club vs. Al Diraiyah Saudi Club end in a draw? | Sports | Kalshi–Polymarket | 54¢ | 7 |
| Will Anthropic's market cap be less than $1.25T at market close on IPO day? | Economics & Finance | Polymarket–Predict.fun | 4.8¢ | 5 |
| Will Nicolás Maduro be the leader of Venezuela end of 2026? | Elections & Politics | Polymarket–Predict.fun | 3.3¢ | 3 |
| Extended FDV above $300M one day after launch? | Crypto | Polymarket–Predict.fun | 2.2¢ | 4 |
| Will an independent win the Nebraska Senate race in 2026? | Elections & Politics | Polymarket–Predict.fun | 2.0¢ | 3 |
| GTA 6 launch postponed again? | Other | Polymarket–Predict.fun | 1.9¢ | 6 |

## Sports around game time

Games that started 6 to 30 hours ago: 1,070 of 2,213 pairs traded on both venues in the same minute, 28,701 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.9¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 623 | 20,445 | 1.0¢ | 4.0¢ |
| Polymarket–Hyperliquid | 1 | 22 | 1.3¢ | 4.1¢ |
| Polymarket–Predict.fun | 446 | 8,234 | 1.0¢ | 3.5¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Counter-Strike: HAVU vs Nordic Valor - Map 2 Winner | Polymarket–Predict.fun | 7.2¢ | 18¢ | 16 |
| FK Radnicki Nis vs. FK Zeleznicar Pancevo: O/U 0.5 | Kalshi–Polymarket | 7.0¢ | 23¢ | 12 |
| Will FK Radnicki Nis vs. FK Zeleznicar Pancevo end in a draw? | Kalshi–Polymarket | 6.0¢ | 78¢ | 54 |
| Bucks vs. Timberwolves: O/U 207.5 | Kalshi–Polymarket | 5.0¢ | 40¢ | 13 |
| Pelicans vs. Grizzlies: O/U 241.5 | Kalshi–Polymarket | 5.0¢ | 10¢ | 11 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 28 of 40 | $1,221 |
| Elections & Politics | Predict.fun | 40 | 8 of 40 | $971 |
| Sports | Kalshi | 9 | 5 of 9 | $1,874 |
| Sports | Polymarket | 39 | 10 of 39 | $118 |
| Sports | Predict.fun | 32 | 4 of 32 | $283 |
| Crypto | Polymarket | 40 | 19 of 40 | $475 |
| Crypto | Predict.fun | 40 | 4 of 40 | $144 |
| Economics & Finance | Polymarket | 40 | 20 of 40 | $1,507 |
| Economics & Finance | Predict.fun | 40 | 9 of 40 | $59.80 |
| Tech & Science | Polymarket | 40 | 24 of 40 | $257 |
| Tech & Science | Predict.fun | 40 | 3 of 40 | $228 |
| Other | Polymarket | 40 | 14 of 40 | $680 |
| Other | Predict.fun | 40 | 1 of 40 | $99.96 |

## Settlement

Events that started in the last seven days: 16,411 pairs have settled on both venues and 16,368 settled the same way (100%); 119 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 5 | 5 | 0 |
| Sports | 16,222 | 16,179 | 119 |
| Crypto | 64 | 64 | 0 |
| Economics & Finance | 62 | 62 | 0 |
| Tech & Science | 58 | 58 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,856 | 5,851 |
| Polymarket | 15,881 | 15,829 |
| Predict.fun | 11,272 | 11,238 |
| Hyperliquid | 51 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Sara Bejlek wins | Ningbo Open: Sara Bejlek vs Xiyu Wang | kalshi + predictfun | 0.52 | 0.5 |
| Katarzyna Kawa wins | Ningbo Open: Katarzyna Kawa vs Maja Chwalinska | kalshi + predictfun | 0.26 | 0.5 |
| Linx Legacy Esport wins | Counter-Strike: Linx Legacy Esport vs XI Esport (BO1) - Dust2.dk Ligaen Regular Season | kalshi + predictfun | 0.5 | 0.0 |
| Walczaki wins | Counter-Strike: Walczaki vs Wingman (BO3) - Exort Fiesta Group Stage | kalshi + predictfun | 0.6 | 0.5 |
| TTG Esports wins | Counter-Strike: TTG Esports vs Diamant Esports (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.57 | 0.5 |
| Growth Lab Esports wins | Counter-Strike: Growth Lab Esports vs Honvéd (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.63 | 0.5 |
| wnT wins | Counter-Strike: wnT vs maybe (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.64 | 0.0 |
| Andre Petroski wins | UFC Fight Night: Andre Petroski vs. Azamat Bekoev (Middleweight, Prelims) | kalshi + polymarket | 0.4 | 0.5 |
| Andre Petroski wins | UFC Fight Night: Andre Petroski vs. Azamat Bekoev (Middleweight, Prelims) | kalshi + predictfun | 0.4 | 0.5 |
| Daniil Ostapenkov wins | Sioux Falls: Daniil Ostapenkov vs Patrick Maloney | kalshi + polymarket | 0.4 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,970) is Sports.
- Every Hyperliquid pair (89) is Sports.
- 261 pairs carry a different category on each side (125 of them point to different divisions); for example "Rodrigo Alujas wins" is Sports on Kalshi and Crypto on Polymarket; "Oscar Jose Gutierrez wins" is Sports on Kalshi and Culture on Polymarket; "Israel wins" is Sports on Kalshi and World on Polymarket.
- 2,387 pairs have a category on one side only (side without one: Polymarket 2,385, Hyperliquid 2).
- 43 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Galatasaray SK win on 2026-11-03?" and "UEFA Champions League Matchday 4: Galatasaray v VfB Stuttgart: Galatasaray" (Polymarket 2026-11-03, Hyperliquid 2026-11-10).
- 33 Kalshi–Hyperliquid pairs are matched across different dates; for example "Aston Villa wins" and "UEFA Champions League Matchday 4: FC Barcelona v Aston Villa: Aston Villa" (Kalshi 2026-11-03, Hyperliquid 2026-11-10).
- 14 Kalshi–Polymarket pairs are matched across different dates; for example "Central Michigan wins" and "Central Michigan vs. Eastern Michigan" (Kalshi 2026-11-03, Polymarket starts 2026-11-05 00:30Z).
- 9 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 10,313 of 12,270 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (51 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
