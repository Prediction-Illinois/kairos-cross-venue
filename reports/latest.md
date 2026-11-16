# Kairos cross-venue report, 2026-11-16

Generated 2026-11-16 00:07 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | – | – | 2 of 2 |
| Sports | 2,602 | 2,309 | 2 of 1,080 | 1.0¢ (339 pairs) | 11,507 of 11,553 |
| Crypto | 0 | 0 | – | – | – |
| Economics & Finance | 0 | 0 | – | – | 1 of 1 |
| Tech & Science | 0 | 0 | – | – | 10 of 10 |
| Climate & Weather | 0 | 0 | – | – | – |

## Pairs

Kairos listed 2,602 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 2,309 (89%), 0 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Sports | Polymarket–Predict.fun | 1,147 of 1,147 |
| Sports | Kalshi–Polymarket | 802 of 808 |
| Sports | Kalshi–Predict.fun | 327 of 491 |
| Sports | Kalshi–Hyperliquid | 0 of 53 |
| Sports | Predict.fun–Hyperliquid | 33 of 52 |
| Sports | Polymarket–Hyperliquid | 0 of 51 |

| Not lined up | Pairs |
|---|---|
| could not confirm both markets ask about the same team | 164 |
| different dates | 107 |
| could not line up the outcomes | 19 |
| different start times | 3 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Sports | 802 | 5 | 2 | 278 | 70 | 50 | 0 |

Not priced: no Predict.fun trades yet 1,196; no live quotes for Hyperliquid yet 33.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Suraj R Prabodh wins | M25 Bhubaneswar: Suraj R Prabodh vs Amrutjay Mohanty | YES on A + NO on B | 8.0 | $0.0294 | order books | 2026-11-23 |
| Sports | Kalshi–Polymarket | Carolina wins | Hurricanes vs. Rangers | NO on A + YES on B | 1.0 | $0.0110 | order books | 2026-11-22 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Sports | 339 | 1,216 | 1.0¢ | 3.0¢ | 27% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Sports | Kalshi–Polymarket | 227 | 1.0¢ | 4.0¢ |
| Sports | Kalshi–Predict.fun | 25 | 1.0¢ | 3.0¢ |
| Sports | Polymarket–Predict.fun | 70 | 1.0¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 17 | 1.2¢ | 3.6¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Tennessee Tech vs. Mississippi State | Sports | Kalshi–Polymarket | 6.0¢ | 3 |
| M25 Vale do Lobo: Duarte Lima Sanches vs Yanis Peterhans | Sports | Kalshi–Polymarket | 5.0¢ | 4 |
| Counter-Strike: Galorys vs BARCA (BO3) - CCT South America Playoffs | Sports | Kalshi–Predict.fun | 3.0¢ | 4 |

## Sports around game time

Games that started 6 to 30 hours ago: 785 of 1,959 pairs traded on both venues in the same minute, 22,214 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 2.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 415 | 15,019 | 1.0¢ | 2.0¢ |
| Polymarket–Predict.fun | 370 | 7,195 | 1.0¢ | 2.2¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| UFC 334: Evan Elder vs. Samuel Sanches (Lightweight, Early Prelims) | Polymarket–Predict.fun | 4.0¢ | 10¢ | 10 |
| Campbell vs. Elon | Kalshi–Polymarket | 3.0¢ | 17¢ | 20 |
| McNeese vs. Southeastern Louisiana | Kalshi–Polymarket | 3.0¢ | 11¢ | 13 |
| ICC Women's Emerging Nations Trophy T20s: Thailand Women vs Zimbabwe Women | Polymarket–Predict.fun | 3.0¢ | 6.0¢ | 12 |
| NJIT Highlanders vs. Fairfield Stags | Kalshi–Polymarket | 3.0¢ | 16¢ | 13 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Sports | Kalshi | 20 | 13 of 20 | $31.35 |
| Sports | Polymarket | 35 | 12 of 35 | $126 |
| Sports | Predict.fun | 25 | 2 of 25 | $387 |

## Settlement

Events that started in the last seven days: 11,630 pairs have settled on both venues and 11,584 settled the same way (100%); 204 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 2 | 2 | 0 |
| Sports | 11,553 | 11,507 | 204 |
| Economics & Finance | 1 | 1 | 0 |
| Tech & Science | 10 | 10 | 0 |
| Other | 64 | 64 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 3,999 | 3,999 |
| Polymarket | 11,128 | 10,969 |
| Predict.fun | 8,512 | 8,354 |
| Hyperliquid | 29 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Alejandro Davidovich Fokina wins | Rolex Paris Masters: Alejandro Davidovich Fokina vs Moise Kouame | kalshi + predictfun | 0.74 | 0.5 |
| Daniel Merida wins | Rolex Paris Masters: Daniel Merida Aguilar vs Alexander Blockx | kalshi + predictfun | 0.42 | 0.5 |
| Stefanos Tsitsipas wins | Rolex Paris Masters: Stefanos Tsitsipas vs Learner Tien | kalshi + predictfun | 0.45 | 0.5 |
| Tie is the result | Will Al Faisaly Saudi Club vs. Al Diraiyah Saudi Club end in a draw? | kalshi + predictfun | 0.37 | 1.0 |
| Nazim Sadykhov wins | UFC 334: Nazim Sadykhov vs. Jefferson Nascimento (Lightweight, Early Prelims) | kalshi + polymarket | 0.7 | 0.5 |
| Adrian Yanez wins | UFC 334: Adrian Yañez vs. Juan Diaz (Bantamweight, Early Prelims) | kalshi + polymarket | 0.53 | 0.5 |
| G2 Ares wins | Counter-Strike: G2 Ares vs Saint Sinners (BO3) - European Pro League Group D | kalshi + predictfun | 0.52 | 0.5 |
| Froglings wins | Dota 2: Froglings vs Astra Invicta (BO3) - 1win Essence Play-in Group A | kalshi + predictfun | 0.31 | 0.5 |
| thirst for victory wins | Valorant: thirst for victory vs SETOUCHI SPARKS (BO3) - Asia Pacific Predator League Japan Playoffs | kalshi + predictfun | 0.36 | 0.5 |
| Xipto Esports wins | Dota 2: Xipto Esports vs angry birds (BO3) - Asgard Championship Group A | kalshi + predictfun | 0.64 | 1.0 |

## Notes for Kairos

- No matched pairs in Elections & Politics, Crypto, Economics & Finance, Tech & Science, and Climate & Weather.
- Every Kalshi pair (1,352) is Sports.
- Every Polymarket pair (2,006) is Sports.
- Every Predict.fun pair (1,690) is Sports.
- Every Hyperliquid pair (156) is Sports.
- 106 pairs carry a different category on each side (20 of them point to different divisions); for example "UEFA Nations League A, Matchday 6: Germany v Netherlands: Netherlands" is Sports on Hyperliquid and Crypto on Polymarket.
- 619 pairs have a category on one side only (side without one: Polymarket 619).
- 53 Kalshi–Hyperliquid pairs are matched across different dates; for example "UEFA Nations League B, Matchday 6: Switzerland v Scotland: Switzerland" and "Switzerland wins" (Kalshi 2026-11-16, Hyperliquid 2026-11-23).
- 51 Polymarket–Hyperliquid pairs are matched across different dates; for example "UEFA Nations League B, Matchday 6: Switzerland v Scotland: Switzerland" and "Will Switzerland win on 2026-11-16?" (Polymarket 2026-11-16, Hyperliquid 2026-11-23).
- 3 Kalshi–Polymarket pairs are matched across different dates; for example "Sacramento Republic wins" and "Will Sacramento Republic FC win on 2026-11-15?" (Kalshi 2026-11-15, Polymarket starts 2026-11-17 02:00Z).
- 183 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 1,196 of 1,507 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (29 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos's approved links (`/market-links`; `/matched-markets` until 11 November 2026), every two venues of a link making one pair; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
