# Kairos cross-venue report, 2026-11-23

Generated 2026-11-23 23:27 UTC from Kairos's catalog of linked markets, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 868 | 520 | 0 of 207 | 1.1¢ (35 pairs) | – |
| Sports | 2,608 | 2,339 | 2 of 1,063 | 1.0¢ (433 pairs) | 6,986 of 7,028 |
| Crypto | 1,225 | 1,225 | 0 of 314 | 2.0¢ (41 pairs) | 5,247 of 5,928 |
| Economics & Finance | 429 | 391 | 0 of 209 | 0.8¢ (44 pairs) | 221 of 222 |
| Tech & Science | 543 | 537 | 0 of 111 | 2.8¢ (61 pairs) | 994 of 996 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 414 pairs fall outside the six divisions (Culture 414, Entertainment 156, Science and Technology 1).

## Pairs

Kairos listed 6,087 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 5,269 (87%), 66 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 520 of 521 |
| Elections & Politics | Kalshi–Polymarket | 0 of 174 |
| Elections & Politics | Kalshi–Predict.fun | 0 of 173 |
| Sports | Polymarket–Predict.fun | 1,288 of 1,291 |
| Sports | Kalshi–Polymarket | 709 of 715 |
| Sports | Kalshi–Predict.fun | 316 of 468 |
| Sports | Kalshi–Hyperliquid | 0 of 46 |
| Sports | Polymarket–Hyperliquid | 0 of 44 |
| Sports | Predict.fun–Hyperliquid | 26 of 44 |
| Crypto | Polymarket–Predict.fun | 1,225 of 1,225 |
| Economics & Finance | Polymarket–Predict.fun | 391 of 391 |
| Economics & Finance | Kalshi–Polymarket | 0 of 19 |
| Economics & Finance | Kalshi–Predict.fun | 0 of 19 |
| Tech & Science | Polymarket–Predict.fun | 537 of 537 |
| Tech & Science | Kalshi–Polymarket | 0 of 5 |
| Tech & Science | Kalshi–Predict.fun | 0 of 1 |
| Other | Polymarket–Predict.fun | 257 of 257 |
| Other | Kalshi–Polymarket | 0 of 80 |
| Other | Kalshi–Predict.fun | 0 of 77 |

| Not lined up | Pairs |
|---|---|
| not a sports market; questions not compared | 548 |
| could not confirm both markets ask about the same team | 149 |
| different dates | 90 |
| could not line up the outcomes | 19 |
| different start times | 5 |
| could not tell which outcome is the Kalshi YES outcome | 4 |
| Polymarket market not found | 3 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 207 | 165 | 14 | 0 |
| Sports | 709 | 3 | 2 | 354 | 92 | 1 | 0 |
| Crypto | 0 | 0 | 0 | 314 | 191 | 7 | 0 |
| Economics & Finance | 0 | 0 | 0 | 209 | 154 | 15 | 0 |
| Tech & Science | 0 | 0 | 0 | 111 | 84 | 6 | 0 |
| Other | 0 | 0 | 0 | 63 | 45 | 7 | 0 |

Not priced: no Predict.fun trades yet 3,276; no live quotes for Hyperliquid yet 26.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Niklas Waldner wins | M15 Sharm ElSheikh: Niklas Waldner vs Dzmitry Dziubailau | YES on A + NO on B | 6.0 | $0.0109 | order books | 2026-12-01 |
| Sports | Kalshi–Polymarket | Alen Mujakic wins | M15 Antalya: Alen Mujakic vs Alejandro Mateo Berge Nourescu | YES on A + NO on B | 0.04 | $0.0002 | order books | 2026-12-01 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 35 | 80 | 1.1¢ | 5.4¢ | 42% |
| Sports | 433 | 2,530 | 1.0¢ | 2.0¢ | 16% |
| Crypto | 41 | 67 | 2.0¢ | 10¢ | 58% |
| Economics & Finance | 44 | 143 | 0.8¢ | 7.2¢ | 34% |
| Tech & Science | 61 | 101 | 2.8¢ | 9.9¢ | 60% |
| Other | 15 | 27 | 1.0¢ | 9.8¢ | 30% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 35 | 1.1¢ | 5.4¢ |
| Sports | Kalshi–Polymarket | 236 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 56 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Predict.fun | 131 | 0.0¢ | 1.0¢ |
| Sports | Predict.fun–Hyperliquid | 10 | 0.5¢ | 1.0¢ |
| Crypto | Polymarket–Predict.fun | 41 | 2.0¢ | 10¢ |
| Economics & Finance | Polymarket–Predict.fun | 44 | 0.8¢ | 7.2¢ |
| Tech & Science | Polymarket–Predict.fun | 61 | 2.8¢ | 9.9¢ |
| Other | Polymarket–Predict.fun | 15 | 1.0¢ | 9.8¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| New NVIDIA CEO named by December 31, 2026? | Economics & Finance | Polymarket–Predict.fun | 13¢ | 3 |
| Counter-Strike: VTK vs Haze (BO3) - CCT Europe Contenders #11 Playoffs | Sports | Kalshi–Predict.fun | 9.0¢ | 3 |
| Will Trump speak to Emmanuel Macron by November 30? | Elections & Politics | Polymarket–Predict.fun | 8.7¢ | 3 |
| Bitcoin Up or Down on November 24? | Crypto | Polymarket–Predict.fun | 6.0¢ | 9 |
| Will the highest temperature in Hong Kong be 22°C on November 24? | Tech & Science | Polymarket–Predict.fun | 6.0¢ | 3 |
| Counter-Strike: FLXRE vs AXE (BO3) - CCT Europe Contenders #11 Playoffs | Sports | Kalshi–Predict.fun | 5.0¢ | 3 |
| Will the highest temperature in Shanghai be 14°C on November 24? | Tech & Science | Polymarket–Predict.fun | 5.0¢ | 4 |
| Will the highest temperature in Miami be between 80-81°F on November 23? | Tech & Science | Polymarket–Predict.fun | 5.0¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 457 of 769 pairs traded on both venues in the same minute, 22,382 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 274 | 16,641 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 183 | 5,741 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Valorant: Mafiosos vs Master Bank (BO3) - VCT Americas Kickoff: Brazil Group Stage | Kalshi–Polymarket | 5.4¢ | 28¢ | 14 |
| Valorant: Any Questions Gaming vs SEC (BO3) - China National Tournament Split Omega: Pro Division Playoffs | Polymarket–Predict.fun | 5.0¢ | 16¢ | 16 |
| Valorant: Unsettled Resentment vs KeepBest Gaming (BO3) - China National Tournament Split Omega: Pro Division Playoffs | Polymarket–Predict.fun | 3.5¢ | 18¢ | 28 |
| Valorant: Unsettled Resentment vs KeepBest Gaming (BO3) - China National Tournament Split Omega: Pro Division Playoffs | Kalshi–Polymarket | 4.0¢ | 25¢ | 122 |
| Valorant: Victory No Limits vs Young Gaming (BO3) - China National Tournament Split Omega: Pro Division Playoffs | Polymarket–Predict.fun | 3.6¢ | 16¢ | 30 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 25 of 40 | $346 |
| Elections & Politics | Predict.fun | 40 | 1 of 40 | $269 |
| Sports | Kalshi | 19 | 9 of 19 | $229 |
| Sports | Polymarket | 32 | 9 of 32 | $100 |
| Sports | Predict.fun | 29 | 4 of 29 | $209 |
| Crypto | Polymarket | 40 | 8 of 40 | $84.56 |
| Crypto | Predict.fun | 40 | 2 of 40 | $805 |
| Economics & Finance | Polymarket | 40 | 24 of 40 | $573 |
| Economics & Finance | Predict.fun | 40 | 10 of 40 | $85.13 |
| Tech & Science | Polymarket | 40 | 25 of 40 | $2,652 |
| Tech & Science | Predict.fun | 40 | 4 of 40 | $68.15 |
| Other | Polymarket | 40 | 24 of 40 | $381 |
| Other | Predict.fun | 40 | 4 of 40 | $75.34 |

## Settlement

Events that started in the last seven days: 14,203 pairs have settled on both venues and 13,477 settled the same way (95%); 201 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Sports | 7,028 | 6,986 | 117 |
| Crypto | 5,928 | 5,247 | 0 |
| Economics & Finance | 222 | 221 | 0 |
| Tech & Science | 996 | 994 | 84 |
| Other | 29 | 29 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 3,029 | 3,024 |
| Polymarket | 13,831 | 13,659 |
| Predict.fun | 11,927 | 11,769 |
| Hyperliquid | 21 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Matteo Berrettini wins | Rolex Paris Masters: Matteo Berrettini vs Carlos Alcaraz | kalshi + predictfun | 0.16 | 0.5 |
| Washington wins | Washington Huskies vs. Utah Utes | kalshi + predictfun | 0.41 | 0.5 |
| Pepperdine wins | Pepperdine Waves vs. Oregon Ducks | kalshi + predictfun | 0.09 | 0.5 |
| Brest Esport wins | Valorant: Brest Esport vs Gesichtenhausen (BO3) - Spike Series Convergence EMEA - DACH Group B | kalshi + predictfun | 0.5 | 0.0 |
| Leo Team wins | Counter-Strike: Leo Team vs Honvéd (BO3) - CCT Europe Group Stage | kalshi + predictfun | 0.7 | 0.5 |
| Bitcoin Up or Down - November 16, 6:40PM-6:45PM ET | Bitcoin Up or Down - November 16, 6:40PM-6:45PM ET | polymarket + predictfun | 0.0 | 1.0 |
| Ethereum Up or Down - November 16, 6:50PM-6:55PM ET | Ethereum Up or Down - November 16, 6:50PM-6:55PM ET | polymarket + predictfun | 1.0 | 0.0 |
| BNB Up or Down - November 16, 6:50PM-6:55PM ET | BNB Up or Down - November 16, 6:50PM-6:55PM ET | polymarket + predictfun | 1.0 | 0.5 |
| Bitcoin Up or Down - November 16, 7:20PM-7:25PM ET | Bitcoin Up or Down - November 16, 7:20PM-7:25PM ET | polymarket + predictfun | 0.0 | 1.0 |
| BNB Up or Down - November 16, 7:20PM-7:25PM ET | BNB Up or Down - November 16, 7:20PM-7:25PM ET | polymarket + predictfun | 0.0 | 1.0 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Hyperliquid pair (134) is Sports.
- 1,052 pairs carry a different category on each side (345 of them point to different divisions); for example "Ledger IPO closing market cap above $1B?" is Crypto on Polymarket and Finance on Predict.fun; "Will SpaceX have the highest IPO Market Cap 2026?" is Science on Polymarket and Finance on Predict.fun; "US national Bitcoin reserve before 2027?" is Politics on Polymarket and Crypto on Predict.fun.
- 46 Kalshi–Hyperliquid pairs are matched across different dates; for example "NBA Regular Season: Philadelphia 76ers v Portland Trail Blazers" and "Portland wins" (Kalshi 2026-11-23, Hyperliquid 2027-02-23).
- 44 Polymarket–Hyperliquid pairs are matched across different dates; for example "NBA Regular Season: Philadelphia 76ers v Portland Trail Blazers" and "Trail Blazers vs. 76ers" (Polymarket 2026-11-23, Hyperliquid 2027-02-23).
- 5 Kalshi–Polymarket pairs are matched across different start times; for example "Villainous wins" and "Counter-Strike: Villainous vs Wanted Goons (BO3) - CROSSFIRE Playoffs" (Kalshi 2026-11-23 01:00Z, Polymarket 2026-11-24 02:00Z).
- 723 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 3,276 of 4,560 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (21 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos's approved links (`/market-links`; `/matched-markets` until 11 November 2026), every two venues of a link making one pair, and outside sports from Kairos's equivalence clusters around every non-sports Predict.fun market; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
