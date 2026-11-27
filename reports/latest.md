# Kairos cross-venue report, 2026-11-27

Generated 2026-11-27 20:44 UTC from Kairos's catalog of linked markets, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 911 | 561 | 0 of 225 | 1.0¢ (25 pairs) | 47 of 47 |
| Sports | 2,678 | 2,287 | 0 of 1,236 | 1.0¢ (574 pairs) | 5,603 of 5,643 |
| Crypto | 1,228 | 1,228 | 0 of 294 | 1.1¢ (38 pairs) | 5,200 of 5,850 |
| Economics & Finance | 435 | 397 | 0 of 221 | 0.6¢ (35 pairs) | 161 of 165 |
| Tech & Science | 660 | 653 | 0 of 171 | 2.0¢ (68 pairs) | 948 of 952 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 385 pairs fall outside the six divisions (Culture 385, Entertainment 156, Science and Technology 1).

## Pairs

Kairos listed 6,297 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 5,354 (85%), 68 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 561 of 562 |
| Elections & Politics | Kalshi–Polymarket | 0 of 175 |
| Elections & Politics | Kalshi–Predict.fun | 0 of 174 |
| Sports | Polymarket–Predict.fun | 1,180 of 1,181 |
| Sports | Kalshi–Polymarket | 752 of 760 |
| Sports | Kalshi–Predict.fun | 303 of 469 |
| Sports | Polymarket–Hyperliquid | 0 of 90 |
| Sports | Predict.fun–Hyperliquid | 52 of 90 |
| Sports | Kalshi–Hyperliquid | 0 of 88 |
| Crypto | Polymarket–Predict.fun | 1,228 of 1,228 |
| Economics & Finance | Polymarket–Predict.fun | 397 of 397 |
| Economics & Finance | Kalshi–Polymarket | 0 of 19 |
| Economics & Finance | Kalshi–Predict.fun | 0 of 19 |
| Tech & Science | Polymarket–Predict.fun | 653 of 653 |
| Tech & Science | Kalshi–Polymarket | 0 of 6 |
| Tech & Science | Kalshi–Predict.fun | 0 of 1 |
| Other | Polymarket–Predict.fun | 228 of 228 |
| Other | Kalshi–Polymarket | 0 of 80 |
| Other | Kalshi–Predict.fun | 0 of 77 |

| Not lined up | Pairs |
|---|---|
| not a sports market; questions not compared | 551 |
| different dates | 179 |
| could not confirm both markets ask about the same team | 160 |
| could not line up the outcomes | 39 |
| Kalshi market is finalized | 4 |
| different start times | 4 |
| Kalshi market is determined | 2 |
| could not tell which outcome is the Kalshi YES outcome | 2 |
| Kalshi market is inactive | 1 |
| Polymarket market not found | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 225 | 183 | 14 | 0 |
| Sports | 752 | 3 | 0 | 484 | 119 | 3 | 0 |
| Crypto | 0 | 0 | 0 | 294 | 190 | 7 | 0 |
| Economics & Finance | 0 | 0 | 0 | 221 | 160 | 14 | 0 |
| Tech & Science | 0 | 0 | 0 | 171 | 123 | 6 | 0 |
| Other | 0 | 0 | 0 | 57 | 47 | 6 | 0 |

Not priced: no Predict.fun trades yet 3,098; no live quotes for Hyperliquid yet 52.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 25 | 43 | 1.0¢ | 4.0¢ | 35% |
| Sports | 574 | 3,492 | 1.0¢ | 2.0¢ | 11% |
| Crypto | 38 | 54 | 1.1¢ | 8.0¢ | 48% |
| Economics & Finance | 35 | 161 | 0.6¢ | 2.4¢ | 13% |
| Tech & Science | 68 | 129 | 2.0¢ | 7.0¢ | 64% |
| Other | 10 | 19 | 1.5¢ | 9.0¢ | 47% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 25 | 1.0¢ | 4.0¢ |
| Sports | Kalshi–Polymarket | 252 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 92 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Predict.fun | 206 | 0.0¢ | 1.0¢ |
| Sports | Predict.fun–Hyperliquid | 24 | 0.7¢ | 1.5¢ |
| Crypto | Polymarket–Predict.fun | 38 | 1.1¢ | 8.0¢ |
| Economics & Finance | Polymarket–Predict.fun | 35 | 0.6¢ | 2.4¢ |
| Tech & Science | Polymarket–Predict.fun | 68 | 2.0¢ | 7.0¢ |
| Other | Polymarket–Predict.fun | 10 | 1.5¢ | 9.0¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Counter-Strike: BOJONG vs HAVU (BO3) - Elisa Open Suomi Playoffs | Sports | Kalshi–Predict.fun | 6.6¢ | 3 |
| Jensen Huang announced resignation or removal again by December 31, 2027? | Economics & Finance | Polymarket–Predict.fun | 5.2¢ | 5 |
| Counter-Strike: ex-Sashi Academy vs Fortress (BO3) - European Pro League Series 11 Closed Qualifier Group B | Sports | Kalshi–Polymarket | 5.0¢ | 5 |
| Bitcoin Up or Down on November 28? | Crypto | Polymarket–Predict.fun | 5.0¢ | 6 |
| Will the highest temperature in Tokyo be 21°C on November 28? | Tech & Science | Polymarket–Predict.fun | 5.0¢ | 4 |
| Will Donald Trump be the #1 searched person on Google this year? | Tech & Science | Polymarket–Predict.fun | 4.8¢ | 4 |
| Will the highest temperature in Paris be 4°C on November 28? | Tech & Science | Polymarket–Predict.fun | 4.4¢ | 3 |
| Will Ethereum dip to $1,500 in November? | Crypto | Polymarket–Predict.fun | 4.1¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 446 of 693 pairs traded on both venues in the same minute, 20,424 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 210 | 13,476 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 236 | 6,948 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Counter-Strike: RoundsGG vs OldBoys (BO3) - ESEA Advanced Europe Playoffs | Kalshi–Polymarket | 4.0¢ | 28¢ | 45 |
| Counter-Strike: Hype Tech vs WRAITH PCIFIC (BO3) - Exort Fiesta Playoffs | Polymarket–Predict.fun | 4.0¢ | 10¢ | 11 |
| Counter-Strike: ENCELADE vs AXE - Map 2 Winner | Polymarket–Predict.fun | 3.3¢ | 11¢ | 10 |
| Counter-Strike: PARTIZAN vs Inner Circle Prospect (BO3) - ESEA Advanced Europe Playoffs | Kalshi–Polymarket | 3.2¢ | 32¢ | 24 |
| Counter-Strike: Rune Eaters vs LPH Gaming - Map 1 Winner | Polymarket–Predict.fun | 3.1¢ | 8.0¢ | 10 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 25 of 40 | $654 |
| Elections & Politics | Predict.fun | 40 | 2 of 40 | $22,722 |
| Sports | Kalshi | 18 | 12 of 18 | $404 |
| Sports | Polymarket | 33 | 13 of 33 | $683 |
| Sports | Predict.fun | 29 | 10 of 29 | $341 |
| Crypto | Polymarket | 40 | 6 of 40 | $523 |
| Crypto | Predict.fun | 40 | 0 of 40 | – |
| Economics & Finance | Polymarket | 40 | 22 of 40 | $186 |
| Economics & Finance | Predict.fun | 40 | 7 of 40 | $149 |
| Tech & Science | Polymarket | 40 | 29 of 40 | $2,331 |
| Tech & Science | Predict.fun | 40 | 10 of 40 | $120 |
| Other | Polymarket | 40 | 20 of 40 | $36.94 |
| Other | Predict.fun | 40 | 0 of 40 | – |

## Settlement

Events that started in the last seven days: 12,710 pairs have settled on both venues and 12,012 settled the same way (95%); 134 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 47 | 47 | 0 |
| Sports | 5,643 | 5,603 | 57 |
| Crypto | 5,850 | 5,200 | 0 |
| Economics & Finance | 165 | 161 | 0 |
| Tech & Science | 952 | 948 | 77 |
| Other | 53 | 53 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 2,809 | 2,807 |
| Polymarket | 12,155 | 12,055 |
| Predict.fun | 10,693 | 10,595 |
| Hyperliquid | 31 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Tomas Martin Etcheverry wins | BNP Paribas Nordic Open: Tomas Etcheverry vs Thiago Agustin Tirante | kalshi + predictfun | 0.54 | 0.5 |
| DISFARCADOS wins | Counter-Strike: DISFARÇADOS vs RED Canids Academy (BO3) - Gamers Club Liga Série A Group B | kalshi + predictfun | 0.32 | 0.5 |
| Team Synapse wins | Dota 2: Team Synapse vs InterActive Philippines (BO3) - European Pro League Group B | kalshi + predictfun | 0.6 | 1.0 |
| Without a Roof wins | Counter-Strike: Without a Roof vs NuTorious (BO3) - CROSSFIRE Playoffs | kalshi + predictfun | 0.81 | 0.5 |
| Spirit Academy wins | Dota 2: Spirit Academy vs Team Allied (BO3) - European Pro League Group A | kalshi + polymarket | 0.64 | 0.5 |
| Vitality Academy wins | Counter-Strike: Vitality Academy vs IMAPROBLEM (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.55 | 0.5 |
| Honvéd wins | Counter-Strike: Honvéd vs Fraternity (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.67 | 0.5 |
| Will the highest temperature in Shenzhen be 19°C on November 21? | Will the highest temperature in Shenzhen be 19°C on November 20? | polymarket + predictfun | 0.0 | 1.0 |
| Will the highest temperature in Shenzhen be 22°C on November 21? | Will the highest temperature in Shenzhen be 22°C on November 20? | polymarket + predictfun | 1.0 | 0.0 |
| LPH Gaming wins | Counter-Strike: LPH Gaming vs KAMUI (BO3) - Exort Fiesta Group Stage | kalshi + predictfun | 0.54 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Hyperliquid pair (268) is Sports.
- 1,030 pairs carry a different category on each side (346 of them point to different divisions); for example "Will Bloomberg IPO by December 31, 2026?" is Tech on Polymarket and Finance on Predict.fun; "Will the U.S. confirm that aliens exist before 2027?" is Science and Technology on Kalshi and Politics on Polymarket; "Will the US confirm that aliens exist before 2027?" is Politics on Polymarket and Culture on Predict.fun.
- 90 Polymarket–Hyperliquid pairs are matched across different dates; for example "NFL Regular Season: Pittsburgh Steelers v Denver Broncos" and "Broncos vs. Steelers" (Polymarket 2026-11-27, Hyperliquid 2027-02-27).
- 88 Kalshi–Hyperliquid pairs are matched across different dates; for example "NFL Regular Season: Pittsburgh Steelers v Denver Broncos" and "Denver wins" (Kalshi 2026-11-27, Hyperliquid 2027-02-27).
- 4 Kalshi–Polymarket pairs are matched across different start times; for example "Young TigeRES wins" and "Counter-Strike: Young TigeRES vs XI Esport (BO3) - ESEA Advanced Europe Playoffs" (Kalshi 2026-11-26 19:00Z, Polymarket 2026-11-27 17:45Z).
- 760 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 3,098 of 4,602 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (31 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos's approved links (`/market-links`; `/matched-markets` until 11 November 2026), every two venues of a link making one pair, and outside sports from Kairos's equivalence clusters around every non-sports Predict.fun market; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
