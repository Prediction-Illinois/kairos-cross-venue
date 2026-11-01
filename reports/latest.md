# Kairos cross-venue report, 2026-11-01

Generated 2026-11-01 17:42 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 488 | 488 | 0 of 238 | 1.0¢ (43 pairs) | 20 of 20 |
| Sports | 13,968 | 13,863 | 1 of 3,221 | 1.0¢ (1,003 pairs) | 14,196 of 14,228 |
| Crypto | 330 | 330 | 0 of 252 | 3.2¢ (18 pairs) | 64 of 64 |
| Economics & Finance | 233 | 233 | 0 of 171 | 0.9¢ (21 pairs) | 62 of 62 |
| Tech & Science | 78 | 78 | 0 of 50 | 0.5¢ (5 pairs) | 57 of 57 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 93 pairs fall outside the six divisions (Culture 93).

## Pairs

Kairos listed 15,190 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 15,085 (99%), 98 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 488 of 488 |
| Sports | Polymarket–Predict.fun | 11,392 of 11,392 |
| Sports | Kalshi–Polymarket | 2,084 of 2,097 |
| Sports | Kalshi–Predict.fun | 340 of 342 |
| Sports | Kalshi–Hyperliquid | 11 of 57 |
| Sports | Polymarket–Hyperliquid | 13 of 55 |
| Sports | Predict.fun–Hyperliquid | 23 of 25 |
| Crypto | Polymarket–Predict.fun | 330 of 330 |
| Economics & Finance | Polymarket–Predict.fun | 233 of 233 |
| Tech & Science | Polymarket–Predict.fun | 78 of 78 |
| Other | Polymarket–Predict.fun | 93 of 93 |

| Not lined up | Pairs |
|---|---|
| different dates | 88 |
| could not confirm both markets ask about the same team | 6 |
| Kalshi market is determined | 4 |
| Kalshi market is inactive | 2 |
| could not tell which outcome is the Kalshi YES outcome | 2 |
| could not line up the outcomes | 2 |
| different start times | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 238 | 159 | 11 | 0 |
| Sports | 2,084 | 5 | 1 | 1,137 | 492 | 14 | 0 |
| Crypto | 0 | 0 | 0 | 252 | 140 | 3 | 0 |
| Economics & Finance | 0 | 0 | 0 | 171 | 111 | 14 | 0 |
| Tech & Science | 0 | 0 | 0 | 50 | 32 | 2 | 0 |
| Other | 0 | 0 | 0 | 28 | 18 | 6 | 0 |

Not priced: no Predict.fun trades yet 11,078; no live quotes for Hyperliquid yet 47.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Anri Nagata wins | W35 Hamamatsu: Anri Nagata vs Mua Shigeta | YES on A + NO on B | 0.02 | $0.0006 | order books | 2026-11-09 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 43 | 183 | 1.0¢ | 2.1¢ | 15% |
| Sports | 1,003 | 4,481 | 1.0¢ | 2.0¢ | 16% |
| Crypto | 18 | 25 | 3.2¢ | 5.9¢ | 60% |
| Economics & Finance | 21 | 56 | 0.9¢ | 3.0¢ | 23% |
| Tech & Science | 5 | 9 | 0.5¢ | 22¢ | 33% |
| Other | 3 | 31 | 0.3¢ | 0.8¢ | 0% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 43 | 1.0¢ | 2.1¢ |
| Sports | Kalshi–Hyperliquid | 10 | 0.4¢ | 1.2¢ |
| Sports | Kalshi–Polymarket | 460 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 57 | 1.0¢ | 3.0¢ |
| Sports | Polymarket–Hyperliquid | 10 | 0.4¢ | 1.1¢ |
| Sports | Polymarket–Predict.fun | 452 | 1.0¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 14 | 0.7¢ | 1.2¢ |
| Crypto | Polymarket–Predict.fun | 18 | 3.2¢ | 5.9¢ |
| Economics & Finance | Polymarket–Predict.fun | 21 | 0.9¢ | 3.0¢ |
| Tech & Science | Polymarket–Predict.fun | 5 | 0.5¢ | 22¢ |
| Other | Polymarket–Predict.fun | 3 | 0.3¢ | 0.8¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Real Betis Balompié to score first vs. BV Borussia 09 Dortmund? | Sports | Polymarket–Predict.fun | 23¢ | 4 |
| Paris Saint-Germain FC to score first vs. Villarreal CF? | Sports | Polymarket–Predict.fun | 13¢ | 5 |
| Oregon vs. Ohio State | Sports | Kalshi–Polymarket | 11¢ | 5 |
| Will Papertrade launch a token by June 30, 2027? | Crypto | Polymarket–Predict.fun | 4.8¢ | 3 |
| QFEX FDV above $50M one day after launch? | Crypto | Polymarket–Predict.fun | 3.5¢ | 3 |
| Anthropic IPO before 2027? | Economics & Finance | Polymarket–Predict.fun | 3.1¢ | 4 |
| Will Crude Oil reach a new all-time high by December 31? | Economics & Finance | Polymarket–Predict.fun | 2.0¢ | 4 |
| Will the Republicans win the Michigan Senate race in 2026? | Elections & Politics | Polymarket–Predict.fun | 1.8¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 1,802 of 4,272 pairs traded on both venues in the same minute, 44,315 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 1.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 928 | 30,022 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 874 | 14,293 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Overwatch: ZETA DIVISION vs Crazy Raccoon (BO5) - OCS Korea Stage 3 Playoffs Seeding Decider Matches | Kalshi–Polymarket | 9.9¢ | 17¢ | 15 |
| Taranto: Leonardo Rossi vs Alessio Balestrieri | Kalshi–Polymarket | 7.0¢ | 24¢ | 10 |
| Marist vs. San Diego | Kalshi–Polymarket | 7.0¢ | 25¢ | 19 |
| Kansas State vs. Colorado: O/U 45.5 | Kalshi–Polymarket | 6.0¢ | 32¢ | 12 |
| Winnipeg Blue Bombers vs. Toronto Argonauts | Kalshi–Polymarket | 5.0¢ | 39¢ | 18 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 30 of 40 | $767 |
| Elections & Politics | Predict.fun | 40 | 5 of 40 | $220 |
| Sports | Kalshi | 6 | 5 of 6 | $11.99 |
| Sports | Polymarket | 40 | 8 of 40 | $183 |
| Sports | Predict.fun | 34 | 0 of 34 | – |
| Crypto | Polymarket | 40 | 16 of 40 | $89.53 |
| Crypto | Predict.fun | 40 | 5 of 40 | $120 |
| Economics & Finance | Polymarket | 40 | 27 of 40 | $374 |
| Economics & Finance | Predict.fun | 40 | 5 of 40 | $98.42 |
| Tech & Science | Polymarket | 40 | 31 of 40 | $221 |
| Tech & Science | Predict.fun | 40 | 4 of 40 | $16.24 |
| Other | Polymarket | 40 | 17 of 40 | $24.99 |
| Other | Predict.fun | 40 | 0 of 40 | – |

## Settlement

Events that started in the last seven days: 14,431 pairs have settled on both venues and 14,399 settled the same way (100%); 196 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 20 | 20 | 10 |
| Sports | 14,228 | 14,196 | 186 |
| Crypto | 64 | 64 | 0 |
| Economics & Finance | 62 | 62 | 0 |
| Tech & Science | 57 | 57 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,609 | 5,534 |
| Polymarket | 13,917 | 13,835 |
| Predict.fun | 9,692 | 9,633 |
| Hyperliquid | 36 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Ann Li wins | Wuhan Tennis Open: Ann Li vs Qinwen Zheng | kalshi + predictfun | 0.29 | 0.5 |
| Belinda Bencic wins | Wuhan Tennis Open: Belinda Bencic vs Shuai Zhang | kalshi + predictfun | 0.82 | 0.5 |
| Iva Jovic wins | Wuhan Tennis Open: Iva Jovic vs Mia Pohankova | kalshi + predictfun | 0.85 | 0.5 |
| Diane Parry wins | Wuhan Tennis Open: Diane Parry vs Anna Kalinskaya | kalshi + predictfun | 0.35 | 0.5 |
| Janice Tjen wins | Wuhan Tennis Open: Janice Tjen vs Oleksandra Oliynykova | kalshi + predictfun | 0.72 | 0.5 |
| Anna Kalinskaya wins | Wuhan Tennis Open: Anna Kalinskaya vs Shuai Zhang | kalshi + predictfun | 0.68 | 0.5 |
| Isurus wins | Counter-Strike: Isurus vs Hacha Esports (BO3) - CCT South America Series 7 Playoffs | kalshi + predictfun | 0.64 | 0.5 |
| Color wins | Counter-Strike: Color vs ex-Zero Tenacity (BO3) - NODWIN Clutch Series Playoffs | kalshi + polymarket | 0.52 | 0.5 |
| Color wins | Counter-Strike: Color vs ex-Zero Tenacity (BO3) - NODWIN Clutch Series Playoffs | kalshi + predictfun | 0.52 | 0.5 |
| ALKA wins | Counter-Strike: ALKA vs ARK E-sports (BO3) - Gamers Club Liga Série A Group A | kalshi + polymarket | 0.57 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,496) is Sports.
- Every Hyperliquid pair (137) is Sports.
- 187 pairs carry a different category on each side (104 of them point to different divisions); for example "Fanny Pire wins" is Sports on Kalshi and Crypto on Polymarket; "San Diego wins" is Sports on Kalshi and Culture on Polymarket; "Israel wins" is Sports on Kalshi and World on Polymarket.
- 2,099 pairs have a category on one side only (side without one: Polymarket 2,098, Predict.fun 1).
- 45 Kalshi–Hyperliquid pairs are matched across different dates; for example "Arsenal wins" and "English Premier League Matchday 9: Liverpool v Arsenal: Arsenal" (Kalshi 2026-11-01, Hyperliquid 2026-11-08).
- 42 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Juventus FC win on 2026-11-01?" and "Italian Serie A Matchday 10: Juventus v Napoli: Juventus" (Polymarket 2026-11-01, Hyperliquid 2026-11-08).
- 1 Kalshi–Polymarket pairs are matched across different start times; for example "OldBoys wins" and "Counter-Strike: OldBoys vs Fire Flux Esports (BO1) - ESEA Advanced Europe Regular Season" (Kalshi 2026-11-01 18:00Z, Polymarket 2026-11-10 19:00Z).
- 16 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 11,078 of 12,977 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (36 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
