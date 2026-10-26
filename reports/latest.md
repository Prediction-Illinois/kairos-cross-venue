# Kairos cross-venue report, 2026-10-26

Generated 2026-10-26 18:19 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 460 | 460 | 2 of 220 | 1.0¢ (53 pairs) | 10 of 10 |
| Sports | 11,064 | 10,950 | 3 of 3,217 | 1.0¢ (855 pairs) | 17,018 of 17,081 |
| Crypto | 389 | 389 | 0 of 290 | 1.8¢ (46 pairs) | – |
| Economics & Finance | 303 | 303 | 0 of 205 | 0.6¢ (47 pairs) | – |
| Tech & Science | 134 | 134 | 0 of 62 | 2.0¢ (24 pairs) | 4 of 4 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 105 pairs fall outside the six divisions (Culture 105).

## Pairs

Kairos listed 12,455 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 12,341 (99%), 109 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 460 of 460 |
| Sports | Polymarket–Predict.fun | 8,410 of 8,412 |
| Sports | Kalshi–Polymarket | 2,215 of 2,254 |
| Sports | Kalshi–Predict.fun | 315 of 332 |
| Sports | Kalshi–Hyperliquid | 1 of 33 |
| Sports | Polymarket–Hyperliquid | 1 of 25 |
| Sports | Predict.fun–Hyperliquid | 8 of 8 |
| Crypto | Polymarket–Predict.fun | 389 of 389 |
| Economics & Finance | Polymarket–Predict.fun | 303 of 303 |
| Tech & Science | Polymarket–Predict.fun | 134 of 134 |
| Other | Polymarket–Predict.fun | 105 of 105 |

| Not lined up | Pairs |
|---|---|
| different dates | 98 |
| could not confirm both markets ask about the same team | 8 |
| different start times | 5 |
| different events | 2 |
| Kalshi market is inactive | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 220 | 159 | 10 | 2 |
| Sports | 2,215 | 16 | 3 | 1,002 | 448 | 15 | 0 |
| Crypto | 0 | 0 | 0 | 290 | 158 | 4 | 0 |
| Economics & Finance | 0 | 0 | 0 | 205 | 152 | 10 | 0 |
| Tech & Science | 0 | 0 | 0 | 62 | 52 | 5 | 0 |
| Other | 0 | 0 | 0 | 35 | 26 | 6 | 0 |

Not priced: no Predict.fun trades yet 8,302; no live quotes for Hyperliquid yet 10.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Beibit Zhukayev wins | Seoul: Beibit Zhukayev vs Coleman Wong | YES on A + NO on B | 131.0 | $0.4207 | order books | 2026-11-03 |
| Elections & Politics | Polymarket–Predict.fun | Will John Fetterman win the 2028 Democratic presidential nomination? | Will John Fetterman win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2400 | Kairos fee quotes | 2028-11-08 |
| Elections & Politics | Polymarket–Predict.fun | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2400 | Kairos fee quotes | 2028-11-08 |
| Sports | Kalshi–Polymarket | Hull City wins | Will Hull City AFC win on 2026-11-07? | NO on A + YES on B | 99.0 | $0.0566 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Full Game: over 50.5 points scored? | Cardinals vs. Cowboys: O/U 50.5 | NO on A + YES on B | 0.46 | $0.0025 | order books | 2026-11-01 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 53 | 216 | 1.0¢ | 3.0¢ | 23% |
| Sports | 855 | 4,266 | 1.0¢ | 2.0¢ | 18% |
| Crypto | 46 | 79 | 1.8¢ | 6.9¢ | 48% |
| Economics & Finance | 47 | 192 | 0.6¢ | 3.9¢ | 23% |
| Tech & Science | 24 | 68 | 2.0¢ | 7.0¢ | 53% |
| Other | 11 | 56 | 0.7¢ | 3.0¢ | 29% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 53 | 1.0¢ | 3.0¢ |
| Sports | Kalshi–Hyperliquid | 1 | 1.3¢ | 1.3¢ |
| Sports | Kalshi–Polymarket | 398 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 44 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Hyperliquid | 1 | 1.3¢ | 1.3¢ |
| Sports | Polymarket–Predict.fun | 409 | 0.9¢ | 2.3¢ |
| Sports | Predict.fun–Hyperliquid | 2 | 0.4¢ | 0.6¢ |
| Crypto | Polymarket–Predict.fun | 46 | 1.8¢ | 6.9¢ |
| Economics & Finance | Polymarket–Predict.fun | 47 | 0.6¢ | 3.9¢ |
| Tech & Science | Polymarket–Predict.fun | 24 | 2.0¢ | 7.0¢ |
| Other | Polymarket–Predict.fun | 11 | 0.7¢ | 3.0¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Como 1907 to score first vs. Torino FC? | Sports | Polymarket–Predict.fun | 21¢ | 5 |
| Valorant: Wolves Esports vs World Sports Invictus Gaming (BO3) - VCT Threshold China Week 2 | Sports | Kalshi–Polymarket | 20¢ | 3 |
| Nottingham Forest FC to score first vs. Brentford FC? | Sports | Polymarket–Predict.fun | 11¢ | 3 |
| Will OpenAI announce another Millennium Prize solution by December 31, 2027? | Tech & Science | Polymarket–Predict.fun | 8.0¢ | 3 |
| Will Anthropic's public ticker be $ANTH? | Economics & Finance | Polymarket–Predict.fun | 7.0¢ | 3 |
| Will any AI model reach 1575 Math Arena Score by December 31, 2026? | Tech & Science | Polymarket–Predict.fun | 5.0¢ | 3 |
| Base FDV above $6B one day after launch? | Crypto | Polymarket–Predict.fun | 4.9¢ | 3 |
| Will Ilija Srdanović be the next prime minister of Serbia? | Elections & Politics | Polymarket–Predict.fun | 4.1¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 1,482 of 3,152 pairs traded on both venues in the same minute, 44,765 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 2.7¢; before the start the 90th percentile was 1.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 770 | 29,370 | 1.0¢ | 2.6¢ |
| Polymarket–Hyperliquid | 12 | 184 | 0.9¢ | 3.2¢ |
| Polymarket–Predict.fun | 700 | 15,211 | 1.0¢ | 2.8¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| KBO Playoff: Kia Tigers vs. Samsung Lions | Kalshi–Polymarket | 7.0¢ | 34¢ | 28 |
| Grizzlies vs. Kings: O/U 237.5 | Polymarket–Predict.fun | 7.0¢ | 28¢ | 10 |
| Raptors vs. Timberwolves: O/U 209.5 | Polymarket–Predict.fun | 5.6¢ | 25¢ | 11 |
| Grizzlies vs. Kings: O/U 239.5 | Polymarket–Predict.fun | 5.0¢ | 21¢ | 11 |
| Grizzlies vs. Kings: O/U 241.5 | Polymarket–Predict.fun | 3.4¢ | 22¢ | 10 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 31 of 40 | $1,746 |
| Elections & Politics | Predict.fun | 40 | 3 of 40 | $24.74 |
| Sports | Kalshi | 13 | 7 of 13 | $1,153 |
| Sports | Polymarket | 38 | 9 of 38 | $1,200 |
| Sports | Predict.fun | 29 | 1 of 29 | $3,418 |
| Crypto | Polymarket | 40 | 14 of 40 | $329 |
| Crypto | Predict.fun | 40 | 11 of 40 | $151 |
| Economics & Finance | Polymarket | 40 | 24 of 40 | $722 |
| Economics & Finance | Predict.fun | 40 | 10 of 40 | $110 |
| Tech & Science | Polymarket | 40 | 21 of 40 | $1,258 |
| Tech & Science | Predict.fun | 40 | 11 of 40 | $301 |
| Other | Polymarket | 40 | 30 of 40 | $868 |
| Other | Predict.fun | 40 | 6 of 40 | $219 |

## Settlement

Events that started in the last seven days: 17,095 pairs have settled on both venues and 17,032 settled the same way (100%); 502 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 10 | 10 | 12 |
| Sports | 17,081 | 17,018 | 490 |
| Tech & Science | 4 | 4 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,658 | 5,381 |
| Polymarket | 16,929 | 16,861 |
| Predict.fun | 12,453 | 12,404 |
| Hyperliquid | 154 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Ann Li wins | Wuhan Tennis Open: Ann Li vs Qinwen Zheng | kalshi + predictfun | 0.29 | 0.5 |
| Belinda Bencic wins | Wuhan Tennis Open: Belinda Bencic vs Shuai Zhang | kalshi + predictfun | 0.82 | 0.5 |
| Iva Jovic wins | Wuhan Tennis Open: Iva Jovic vs Mia Pohankova | kalshi + predictfun | 0.85 | 0.5 |
| Diane Parry wins | Wuhan Tennis Open: Diane Parry vs Anna Kalinskaya | kalshi + predictfun | 0.35 | 0.5 |
| Janice Tjen wins | Wuhan Tennis Open: Janice Tjen vs Oleksandra Oliynykova | kalshi + predictfun | 0.72 | 0.5 |
| Anna Kalinskaya wins | Wuhan Tennis Open: Anna Kalinskaya vs Shuai Zhang | kalshi + predictfun | 0.68 | 0.5 |
| Elite Klan wins | Counter-Strike: Elite Klan vs Passion Academy (BO3) - United21 Group D | kalshi + predictfun | 0.46 | 0.5 |
| Copenhagen Wolves wins | Counter-Strike: Copenhagen Wolves vs Sökerorg (BO3) - European Pro League Regular Playoffs | kalshi + predictfun | 0.62 | 0.5 |
| Hacha Esports wins | Counter-Strike: Hacha Esports vs Los Niños (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.34 | 0.5 |
| Gremio Esports wins | Counter-Strike: Grêmio Esports vs SUKEBAN (BO3) - CCT South America Series 7 Group Stage | kalshi + predictfun | 0.55 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,619) is Sports.
- Every Hyperliquid pair (66) is Sports.
- 206 pairs carry a different category on each side (94 of them point to different divisions); for example "Kenta Kawada wins" is Sports on Kalshi and Crypto on Polymarket; "Drake wins" is Sports on Kalshi and Culture on Polymarket; "Will a team from LPL (China) win LoL Worlds 2026?" is World on Polymarket and Esports on Predict.fun.
- 1,399 pairs have a category on one side only (side without one: Polymarket 1,399).
- 32 Kalshi–Hyperliquid pairs are matched across different dates; for example "Bournemouth wins" and "English Premier League Matchday 9: Bournemouth AFC v Leeds United: Bournemouth AFC" (Kalshi 2026-10-31, Hyperliquid 2026-11-07).
- 25 Kalshi–Polymarket pairs are matched across different dates; for example "Arizona wins" and "Arizona vs. Texas Tech" (Kalshi 2026-10-30, Polymarket starts 2026-10-31 16:00Z).
- 24 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Sevilla FC win on 2026-10-26?" and "Spanish La Liga Matchday 10: Sevilla FC v CA Osasuna: Sevilla FC" (Polymarket 2026-10-26, Hyperliquid 2026-11-02).
- 9 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 8,302 of 10,124 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (154 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
