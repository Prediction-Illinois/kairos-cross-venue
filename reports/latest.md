# Kairos cross-venue report, 2026-11-08

Generated 2026-11-08 17:41 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 376 | 376 | 0 of 181 | 2.1¢ (24 pairs) | 116 of 116 |
| Sports | 8,650 | 8,541 | 5 of 2,950 | 1.0¢ (929 pairs) | 17,668 of 17,752 |
| Crypto | 382 | 382 | 0 of 267 | 1.8¢ (10 pairs) | – |
| Economics & Finance | 289 | 289 | 0 of 188 | 1.0¢ (22 pairs) | – |
| Tech & Science | 88 | 88 | 0 of 49 | 1.2¢ (5 pairs) | 2 of 2 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 120 pairs fall outside the six divisions (Culture 117, no category 3).

## Pairs

Kairos listed 9,905 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 9,793 (99%), 66 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 376 of 376 |
| Sports | Polymarket–Predict.fun | 6,339 of 6,339 |
| Sports | Kalshi–Polymarket | 1,861 of 1,873 |
| Sports | Kalshi–Predict.fun | 327 of 330 |
| Sports | Kalshi–Hyperliquid | 0 of 55 |
| Sports | Polymarket–Hyperliquid | 0 of 39 |
| Sports | Predict.fun–Hyperliquid | 14 of 14 |
| Crypto | Polymarket–Predict.fun | 382 of 382 |
| Economics & Finance | Polymarket–Predict.fun | 289 of 289 |
| Tech & Science | Polymarket–Predict.fun | 88 of 88 |
| Other | Polymarket–Predict.fun | 117 of 117 |
| Other | Polymarket–Hyperliquid | 0 of 3 |

| Not lined up | Pairs |
|---|---|
| different dates | 97 |
| different start times | 5 |
| could not confirm both markets ask about the same team | 4 |
| Kalshi market is inactive | 4 |
| could not tell which outcome is the Kalshi YES outcome | 2 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 181 | 143 | 12 | 0 |
| Sports | 1,861 | 7 | 5 | 1,089 | 533 | 13 | 0 |
| Crypto | 0 | 0 | 0 | 267 | 143 | 3 | 0 |
| Economics & Finance | 0 | 0 | 0 | 188 | 141 | 13 | 0 |
| Tech & Science | 0 | 0 | 0 | 49 | 36 | 3 | 0 |
| Other | 0 | 0 | 0 | 37 | 24 | 6 | 0 |

Not priced: no Predict.fun trades yet 6,107; no live quotes for Hyperliquid yet 14.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Tie is the result | Will Al Faisaly Saudi Club vs. Al Diraiyah Saudi Club end in a draw? | YES on A + NO on B | 21520.47 | $3800.2983 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Diriyah Club wins | Will Al Diraiyah Saudi Club win on 2026-11-07? | NO on A + YES on B | 23752.55 | $1934.3337 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Al-Faisaly wins | Will Al Faisaly Saudi Club win on 2026-11-07? | NO on A + YES on B | 14026.46 | $1343.5006 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Oriol Roca Batalla wins | Lima: Oriol Roca-Batalla vs Emilio Camacho | NO on A + YES on B | 7.11 | $0.0751 | order books | 2026-11-15 |
| Sports | Kalshi–Polymarket | STATE wins | Counter-Strike: STATE vs MASQ (BO1) - Dust2.dk Ligaen Regular Season | NO on A + YES on B | 2.0 | $0.0132 | order books | 2026-11-09 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 24 | 42 | 2.1¢ | 4.4¢ | 57% |
| Sports | 929 | 4,322 | 1.0¢ | 2.0¢ | 15% |
| Crypto | 10 | 12 | 1.8¢ | 4.0¢ | 50% |
| Economics & Finance | 22 | 44 | 1.0¢ | 6.2¢ | 34% |
| Tech & Science | 5 | 12 | 1.2¢ | 2.6¢ | 17% |
| Other | 9 | 36 | 1.2¢ | 9.7¢ | 36% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 24 | 2.1¢ | 4.4¢ |
| Sports | Kalshi–Polymarket | 426 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 53 | 0.5¢ | 2.0¢ |
| Sports | Polymarket–Predict.fun | 446 | 0.6¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 4 | 0.5¢ | 1.0¢ |
| Crypto | Polymarket–Predict.fun | 10 | 1.8¢ | 4.0¢ |
| Economics & Finance | Polymarket–Predict.fun | 22 | 1.0¢ | 6.2¢ |
| Tech & Science | Polymarket–Predict.fun | 5 | 1.2¢ | 2.6¢ |
| Other | Polymarket–Predict.fun | 9 | 1.2¢ | 9.7¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Counter-Strike: Low Cortisol vs Rush (BO3) - CCT South America Group Stage | Sports | Kalshi–Predict.fun | 13¢ | 3 |
| Counter-Strike: Ryvex vs Drama eSports (BO3) - CCT Europe Closed Qualifier: Series Group D | Sports | Polymarket–Predict.fun | 10¢ | 3 |
| Will Dani win the GMGN GGC Season 1 Grand Final? | Other | Polymarket–Predict.fun | 7.1¢ | 6 |
| Will Joe Burrow win the 2026 NFL MVP? | Sports | Polymarket–Predict.fun | 4.8¢ | 3 |
| Will J.D. Vance win the 2028 Republican presidential nomination? | Elections & Politics | Polymarket–Predict.fun | 4.4¢ | 5 |
| Will gas win the GMGN GGC Season 1 Grand Final? | Other | Polymarket–Predict.fun | 4.1¢ | 3 |
| Will Roxo win the GMGN GGC Season 1 Grand Final? | Other | Polymarket–Predict.fun | 3.6¢ | 3 |
| Will Jon Ossoff win the 2028 Democratic presidential nomination? | Elections & Politics | Polymarket–Predict.fun | 2.9¢ | 4 |

## Sports around game time

Games that started 6 to 30 hours ago: 2,147 of 5,161 pairs traded on both venues in the same minute, 52,374 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 1.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 1,201 | 36,479 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 946 | 15,895 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Montreal Alouettes vs. Winnipeg Blue Bombers | Kalshi–Polymarket | 4.5¢ | 21¢ | 12 |
| East Texas A&M vs. Nicholls State | Kalshi–Polymarket | 5.0¢ | 15¢ | 15 |
| Counter-Strike: Crimson Vortex vs Elusive (BO3) - CCT North America Challengers Playoffs | Kalshi–Polymarket | 4.4¢ | 9.0¢ | 11 |
| Dota 2: Xipto Esports vs Zenith - Game 2 Winner | Polymarket–Predict.fun | 4.0¢ | 12¢ | 10 |
| KHL: Traktor vs. Avtomobilist Yekaterinburg | Kalshi–Polymarket | 4.0¢ | 13¢ | 10 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 26 of 40 | $624 |
| Elections & Politics | Predict.fun | 40 | 6 of 40 | $438 |
| Sports | Kalshi | 12 | 7 of 12 | $11.62 |
| Sports | Polymarket | 40 | 9 of 40 | $194 |
| Sports | Predict.fun | 28 | 0 of 28 | – |
| Crypto | Polymarket | 40 | 19 of 40 | $140 |
| Crypto | Predict.fun | 40 | 3 of 40 | $50.00 |
| Economics & Finance | Polymarket | 40 | 17 of 40 | $226 |
| Economics & Finance | Predict.fun | 40 | 2 of 40 | $197 |
| Tech & Science | Polymarket | 40 | 21 of 40 | $244 |
| Tech & Science | Predict.fun | 40 | 3 of 40 | $2.24 |
| Other | Polymarket | 40 | 25 of 40 | $183 |
| Other | Predict.fun | 40 | 3 of 40 | $149 |

## Settlement

Events that started in the last seven days: 17,871 pairs have settled on both venues and 17,787 settled the same way (100%); 591 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 116 | 116 | 15 |
| Sports | 17,752 | 17,668 | 576 |
| Tech & Science | 2 | 2 | 0 |
| Other | 1 | 1 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 6,024 | 5,946 |
| Polymarket | 17,781 | 17,304 |
| Predict.fun | 13,068 | 12,625 |
| Hyperliquid | 51 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Sara Bejlek wins | Ningbo Open: Sara Bejlek vs Xiyu Wang | kalshi + predictfun | 0.52 | 0.5 |
| Katarzyna Kawa wins | Ningbo Open: Katarzyna Kawa vs Maja Chwalinska | kalshi + predictfun | 0.26 | 0.5 |
| Alexander Bublik wins | Almaty Open: Alexander Bublik vs Fabian Marozsan | kalshi + predictfun | 0.72 | 0.5 |
| Andre Petroski wins | UFC Fight Night: Andre Petroski vs. Azamat Bekoev (Middleweight, Prelims) | kalshi + predictfun | 0.4 | 0.5 |
| Radnicki Nis wins | Will FK Radnicki Nis win on 2026-11-02? | kalshi + polymarket | 0.25 | 0.0 |
| Tie is the result | Will FK Radnicki Nis vs. FK Zeleznicar Pancevo end in a draw? | kalshi + polymarket | 0.26 | 1.0 |
| FK Zeleznicar Pancevo wins | Will FK Zeleznicar Pancevo win on 2026-11-02? | kalshi + polymarket | 0.49 | 0.0 |
| OldBoys wins | Counter-Strike: OldBoys vs Fire Flux Esports (BO1) - ESEA Advanced Europe Regular Season | kalshi + polymarket | 0.41 | 0.5 |
| Alejandro Davidovich Fokina wins | Rolex Paris Masters: Alejandro Davidovich Fokina vs Moise Kouame | kalshi + polymarket | 0.74 | 0.5 |
| Daniel Merida wins | Rolex Paris Masters: Daniel Merida Aguilar vs Alexander Blockx | kalshi + polymarket | 0.42 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,258) is Sports.
- 455 pairs carry a different category on each side (339 of them point to different divisions); for example "Adam Bajurko wins" is Sports on Kalshi and Crypto on Polymarket; "Nikola Slavic wins" is Sports on Kalshi and Culture on Polymarket; "Israel wins" is Sports on Kalshi and World on Polymarket.
- 2,964 pairs have a category on one side only (side without one: Polymarket 2,964).
- 55 Kalshi–Hyperliquid pairs are matched across different dates; for example "Aston Villa wins" and "English Premier League Matchday 10: Manchester United v Aston Villa: Aston Villa" (Kalshi 2026-11-08, Hyperliquid 2026-11-15).
- 42 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will ACF Fiorentina win on 2026-11-08?" and "Italian Serie A Matchday 11: Fiorentina v Juventus: Fiorentina" (Polymarket 2026-11-08, Hyperliquid 2026-11-15).
- 5 Kalshi–Polymarket pairs are matched across different start times; for example "RED Canids Academy wins" and "Counter-Strike: RED Canids Academy vs Grêmio Esports (BO3) - Gamers Club Liga Série A Playoffs" (Kalshi 2026-11-08 19:00Z, Polymarket 2026-11-09 18:30Z).
- 10 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 6,107 of 7,932 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (51 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
