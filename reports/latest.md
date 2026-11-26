# Kairos cross-venue report, 2026-11-26

Generated 2026-11-26 20:59 UTC from Kairos's catalog of linked markets, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 876 | 526 | 0 of 222 | 1.9¢ (31 pairs) | 47 of 47 |
| Sports | 2,700 | 2,331 | 1 of 1,190 | 1.0¢ (480 pairs) | 5,669 of 5,708 |
| Crypto | 1,228 | 1,228 | 0 of 291 | 2.0¢ (27 pairs) | 5,212 of 5,850 |
| Economics & Finance | 430 | 392 | 0 of 215 | 0.5¢ (29 pairs) | 181 of 184 |
| Tech & Science | 623 | 617 | 0 of 166 | 2.3¢ (84 pairs) | 1,049 of 1,053 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 390 pairs fall outside the six divisions (Culture 390, Entertainment 156, Science and Technology 1).

## Pairs

Kairos listed 6,247 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 5,327 (85%), 62 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 526 of 527 |
| Elections & Politics | Kalshi–Polymarket | 0 of 175 |
| Elections & Politics | Kalshi–Predict.fun | 0 of 174 |
| Sports | Polymarket–Predict.fun | 1,247 of 1,248 |
| Sports | Kalshi–Polymarket | 735 of 737 |
| Sports | Kalshi–Predict.fun | 298 of 469 |
| Sports | Kalshi–Hyperliquid | 0 of 82 |
| Sports | Polymarket–Hyperliquid | 0 of 82 |
| Sports | Predict.fun–Hyperliquid | 51 of 82 |
| Crypto | Polymarket–Predict.fun | 1,228 of 1,228 |
| Economics & Finance | Polymarket–Predict.fun | 392 of 392 |
| Economics & Finance | Kalshi–Polymarket | 0 of 19 |
| Economics & Finance | Kalshi–Predict.fun | 0 of 19 |
| Tech & Science | Polymarket–Predict.fun | 617 of 617 |
| Tech & Science | Kalshi–Polymarket | 0 of 5 |
| Tech & Science | Kalshi–Predict.fun | 0 of 1 |
| Other | Polymarket–Predict.fun | 233 of 233 |
| Other | Kalshi–Polymarket | 0 of 80 |
| Other | Kalshi–Predict.fun | 0 of 77 |

| Not lined up | Pairs |
|---|---|
| not a sports market; questions not compared | 550 |
| could not confirm both markets ask about the same team | 169 |
| different dates | 164 |
| could not line up the outcomes | 32 |
| different start times | 2 |
| could not tell which outcome is the Kalshi YES outcome | 2 |
| Polymarket market not found | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 222 | 174 | 14 | 0 |
| Sports | 735 | 6 | 1 | 455 | 123 | 8 | 0 |
| Crypto | 0 | 0 | 0 | 291 | 196 | 5 | 0 |
| Economics & Finance | 0 | 0 | 0 | 215 | 149 | 13 | 0 |
| Tech & Science | 0 | 0 | 0 | 166 | 120 | 4 | 0 |
| Other | 0 | 0 | 0 | 58 | 46 | 6 | 0 |

Not priced: no Predict.fun trades yet 3,134; no live quotes for Hyperliquid yet 51.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Mira wins | Counter-Strike: Mira vs Los Niños (BO3) - Gamers Club Liga Série A Playoffs | NO on A + YES on B | 10.0 | $0.0585 | order books | 2026-11-27 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 31 | 76 | 1.9¢ | 3.3¢ | 45% |
| Sports | 480 | 2,463 | 1.0¢ | 2.0¢ | 16% |
| Crypto | 27 | 38 | 2.0¢ | 8.0¢ | 53% |
| Economics & Finance | 29 | 132 | 0.5¢ | 2.0¢ | 11% |
| Tech & Science | 84 | 163 | 2.3¢ | 8.0¢ | 64% |
| Other | 12 | 22 | 0.6¢ | 2.0¢ | 14% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 31 | 1.9¢ | 3.3¢ |
| Sports | Kalshi–Polymarket | 229 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 59 | 1.0¢ | 2.2¢ |
| Sports | Polymarket–Predict.fun | 175 | 1.0¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 17 | 0.7¢ | 2.1¢ |
| Crypto | Polymarket–Predict.fun | 27 | 2.0¢ | 8.0¢ |
| Economics & Finance | Polymarket–Predict.fun | 29 | 0.5¢ | 2.0¢ |
| Tech & Science | Polymarket–Predict.fun | 84 | 2.3¢ | 8.0¢ |
| Other | Polymarket–Predict.fun | 12 | 0.6¢ | 2.0¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Fourth Jensen Huang affair reported by December 31? | Tech & Science | Polymarket–Predict.fun | 15¢ | 3 |
| Dota 2: Spirit Academy vs Inner Circle (BO3) - European Pro League Playoffs | Sports | Kalshi–Predict.fun | 12¢ | 3 |
| Valorant: Eintracht Frankfurt vs GIANTX (BO3) - VCT EMEA Kickoff: Europe - Qualifier Swiss Stage | Sports | Kalshi–Predict.fun | 9.0¢ | 3 |
| Will the next Qwen Max model (3.9+) debut at a score of at least 1520 by June 30, 2027? | Tech & Science | Polymarket–Predict.fun | 7.6¢ | 4 |
| Will the highest temperature in Houston be between 58-59°F on November 26? | Tech & Science | Polymarket–Predict.fun | 7.0¢ | 3 |
| Will OpenAI IPO by June 30, 2027? | Economics & Finance | Polymarket–Predict.fun | 4.0¢ | 4 |
| Will Delcy Rodríguez be the leader of Venezuela end of 2026? | Elections & Politics | Polymarket–Predict.fun | 3.2¢ | 7 |
| Will Jensen Huang publicly testify before Congress by December 31, 2026? | Elections & Politics | Polymarket–Predict.fun | 3.1¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 500 of 706 pairs traded on both venues in the same minute, 20,571 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 244 | 12,240 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 256 | 8,331 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Dota 2: 4ikibamboni vs V - Game 2 Winner | Polymarket–Predict.fun | 6.5¢ | 24¢ | 12 |
| Dota 2: V vs Amaru Gaming - Game 2 Winner | Polymarket–Predict.fun | 2.8¢ | 16¢ | 10 |
| Dota 2: Team Synapse vs PuckChamp - Game 1 Winner | Polymarket–Predict.fun | 4.9¢ | 24¢ | 23 |
| Dota 2: Team Synapse vs PuckChamp - Game 2 Winner | Polymarket–Predict.fun | 4.4¢ | 20¢ | 21 |
| Arizona State Sun Devils vs. LSU Tigers | Polymarket–Predict.fun | 4.0¢ | 23¢ | 13 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 24 of 40 | $1,639 |
| Elections & Politics | Predict.fun | 40 | 3 of 40 | $234 |
| Sports | Kalshi | 17 | 10 of 17 | $237 |
| Sports | Polymarket | 33 | 14 of 33 | $53.84 |
| Sports | Predict.fun | 29 | 4 of 29 | $10.82 |
| Sports | Hyperliquid | 1 | 1 of 1 | $45.69 |
| Crypto | Polymarket | 40 | 6 of 40 | $334 |
| Crypto | Predict.fun | 40 | 1 of 40 | $193 |
| Economics & Finance | Polymarket | 40 | 23 of 40 | $671 |
| Economics & Finance | Predict.fun | 40 | 10 of 40 | $95.16 |
| Tech & Science | Polymarket | 40 | 27 of 40 | $1,412 |
| Tech & Science | Predict.fun | 40 | 4 of 40 | $24.50 |
| Other | Polymarket | 40 | 27 of 40 | $249 |
| Other | Predict.fun | 40 | 0 of 40 | – |

## Settlement

Events that started in the last seven days: 12,885 pairs have settled on both venues and 12,201 settled the same way (95%); 134 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 47 | 47 | 0 |
| Sports | 5,708 | 5,669 | 57 |
| Crypto | 5,850 | 5,212 | 0 |
| Economics & Finance | 184 | 181 | 0 |
| Tech & Science | 1,053 | 1,049 | 77 |
| Other | 43 | 43 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 2,859 | 2,859 |
| Polymarket | 12,316 | 12,225 |
| Predict.fun | 10,825 | 10,731 |
| Hyperliquid | 38 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Tomas Martin Etcheverry wins | BNP Paribas Nordic Open: Tomas Etcheverry vs Thiago Agustin Tirante | kalshi + predictfun | 0.54 | 0.5 |
| LPH Gaming wins | Counter-Strike: LPH Gaming vs Honvéd (BO3) - Exort Fiesta Group Stage | kalshi + predictfun | 0.43 | 0.5 |
| Zero Tenacity wins | Dota 2: Zero Tenacity vs Inner Circle (BO3) - European Pro League Group A | kalshi + predictfun | 0.35 | 0.5 |
| DISFARCADOS wins | Counter-Strike: DISFARÇADOS vs RED Canids Academy (BO3) - Gamers Club Liga Série A Group B | kalshi + polymarket | 0.32 | 0.5 |
| DISFARCADOS wins | Counter-Strike: DISFARÇADOS vs RED Canids Academy (BO3) - Gamers Club Liga Série A Group B | kalshi + predictfun | 0.32 | 0.5 |
| Rcave wins | Counter-Strike: Rcave vs DINERO (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.61 | 0.5 |
| Team Synapse wins | Dota 2: Team Synapse vs InterActive Philippines (BO3) - European Pro League Group B | kalshi + predictfun | 0.6 | 1.0 |
| Without a Roof wins | Counter-Strike: Without a Roof vs NuTorious (BO3) - CROSSFIRE Playoffs | kalshi + polymarket | 0.81 | 0.5 |
| Without a Roof wins | Counter-Strike: Without a Roof vs NuTorious (BO3) - CROSSFIRE Playoffs | kalshi + predictfun | 0.81 | 0.5 |
| BNB Up or Down - November 19, 4:05PM-4:10PM ET | BNB Up or Down - November 19, 4:05PM-4:10PM ET | polymarket + predictfun | 0.0 | 1.0 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Hyperliquid pair (246) is Sports.
- 1,026 pairs carry a different category on each side (341 of them point to different divisions); for example "Will Bloomberg IPO by December 31, 2026?" is Tech on Polymarket and Finance on Predict.fun; "Will the U.S. confirm that aliens exist before 2027?" is Science and Technology on Kalshi and Politics on Polymarket; "Will the US confirm that aliens exist before 2027?" is Politics on Polymarket and Culture on Predict.fun.
- 82 Kalshi–Hyperliquid pairs are matched across different dates; for example "NFL Regular Season: Detroit Lions v Chicago Bears" and "Chicago wins" (Kalshi 2026-11-26, Hyperliquid 2027-02-26).
- 82 Polymarket–Hyperliquid pairs are matched across different dates; for example "NFL Regular Season: Detroit Lions v Chicago Bears" and "Bears vs. Lions" (Polymarket 2026-11-26, Hyperliquid 2027-02-26).
- 2 Kalshi–Polymarket pairs are matched across different start times; for example "Joblife wins" and "Valorant: Joblife vs la Masia (BO3) - VCT EMEA Kickoff: Europe - Qualifier Swiss Stage" (Kalshi 2026-11-26 16:00Z, Polymarket 2026-11-26 19:30Z).
- 754 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 3,134 of 4,592 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (38 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos's approved links (`/market-links`; `/matched-markets` until 11 November 2026), every two venues of a link making one pair, and outside sports from Kairos's equivalence clusters around every non-sports Predict.fun market; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
