# Kairos cross-venue report, 2026-11-07

Generated 2026-11-07 17:29 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 377 | 377 | 0 of 178 | 1.4¢ (29 pairs) | 119 of 119 |
| Sports | 10,872 | 10,754 | 8 of 3,563 | 1.0¢ (1,194 pairs) | 16,275 of 16,352 |
| Crypto | 388 | 388 | 0 of 273 | 2.8¢ (25 pairs) | 64 of 64 |
| Economics & Finance | 288 | 288 | 0 of 185 | 1.1¢ (27 pairs) | 52 of 52 |
| Tech & Science | 88 | 88 | 0 of 49 | 0.9¢ (9 pairs) | 6 of 6 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 118 pairs fall outside the six divisions (Culture 117, no category 1).

## Pairs

Kairos listed 12,131 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 12,013 (99%), 55 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 377 of 377 |
| Sports | Polymarket–Predict.fun | 8,094 of 8,094 |
| Sports | Kalshi–Polymarket | 2,283 of 2,307 |
| Sports | Kalshi–Predict.fun | 365 of 367 |
| Sports | Kalshi–Hyperliquid | 0 of 53 |
| Sports | Polymarket–Hyperliquid | 0 of 39 |
| Sports | Predict.fun–Hyperliquid | 12 of 12 |
| Crypto | Polymarket–Predict.fun | 388 of 388 |
| Economics & Finance | Polymarket–Predict.fun | 288 of 288 |
| Tech & Science | Polymarket–Predict.fun | 88 of 88 |
| Other | Polymarket–Predict.fun | 118 of 118 |

| Not lined up | Pairs |
|---|---|
| different dates | 104 |
| Polymarket market not found | 5 |
| different start times | 3 |
| could not confirm both markets ask about the same team | 3 |
| could not tell which outcome is the Kalshi YES outcome | 1 |
| name and team-code checks point to different outcomes | 1 |
| Kalshi market is inactive | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 178 | 134 | 12 | 0 |
| Sports | 2,283 | 9 | 8 | 1,280 | 425 | 12 | 0 |
| Crypto | 0 | 0 | 0 | 273 | 142 | 4 | 0 |
| Economics & Finance | 0 | 0 | 0 | 185 | 139 | 13 | 0 |
| Tech & Science | 0 | 0 | 0 | 49 | 38 | 3 | 0 |
| Other | 0 | 0 | 0 | 37 | 23 | 6 | 0 |

Not priced: no Predict.fun trades yet 7,716; no live quotes for Hyperliquid yet 12.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Tie is the result | Will Al Faisaly Saudi Club vs. Al Diraiyah Saudi Club end in a draw? | YES on A + NO on B | 10679.47 | $3157.9659 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Tie is the result | Will Al Fateh Saudi Club vs. Al Riyadh Saudi Club end in a draw? | YES on A + NO on B | 13122.81 | $3062.8579 | order books | 2026-11-06 |
| Sports | Kalshi–Polymarket | Al-Fateh wins | Will Al Fateh Saudi Club win on 2026-11-06? | NO on A + YES on B | 10124.49 | $1834.8059 | order books | 2026-11-06 |
| Sports | Kalshi–Polymarket | Diriyah Club wins | Will Al Diraiyah Saudi Club win on 2026-11-07? | NO on A + YES on B | 16833.8 | $1707.1643 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Al-Faisaly wins | Will Al Faisaly Saudi Club win on 2026-11-07? | NO on A + YES on B | 9199.46 | $1118.0872 | order books | 2026-11-07 |
| Sports | Kalshi–Polymarket | Al-Riyadh wins | Will Al Riyadh Saudi Club win on 2026-11-06? | NO on A + YES on B | 13835.66 | $995.4452 | order books | 2026-11-06 |
| Sports | Kalshi–Polymarket | Orlando wins | Magic vs. Kings | YES on A + NO on B | 2.42 | $0.0067 | order books | 2026-11-11 |
| Sports | Kalshi–Polymarket | Will over 2.5 goals be scored? | PFC Ludogorets 1945 Razgrad vs. FC CSKA 1948: O/U 2.5 | NO on A + YES on B | 0.03 | $0.0007 | order books | 2026-11-07 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 29 | 64 | 1.4¢ | 5.3¢ | 39% |
| Sports | 1,194 | 5,519 | 1.0¢ | 2.0¢ | 13% |
| Crypto | 25 | 53 | 2.8¢ | 12¢ | 68% |
| Economics & Finance | 27 | 66 | 1.1¢ | 5.9¢ | 32% |
| Tech & Science | 9 | 16 | 0.9¢ | 2.4¢ | 25% |
| Other | 10 | 53 | 1.1¢ | 7.8¢ | 42% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 29 | 1.4¢ | 5.3¢ |
| Sports | Kalshi–Polymarket | 598 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 108 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Predict.fun | 476 | 0.9¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 12 | 0.8¢ | 1.3¢ |
| Crypto | Polymarket–Predict.fun | 25 | 2.8¢ | 12¢ |
| Economics & Finance | Polymarket–Predict.fun | 27 | 1.1¢ | 5.9¢ |
| Tech & Science | Polymarket–Predict.fun | 9 | 0.9¢ | 2.4¢ |
| Other | Polymarket–Predict.fun | 10 | 1.1¢ | 7.8¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Dota 2: Froglings vs Astra Invicta (BO3) - 1win Essence Play-in Group A | Sports | Kalshi–Predict.fun | 18¢ | 5 |
| Puffpaw FDV above $200M one day after launch? | Crypto | Polymarket–Predict.fun | 15¢ | 4 |
| AHL: Coachella Valley Firebirds vs. Tucson Roadrunners | Sports | Kalshi–Polymarket | 6.0¢ | 3 |
| Puffpaw FDV above $300M one day after launch? | Crypto | Polymarket–Predict.fun | 5.2¢ | 5 |
| Dota 2: InterActive Philippines vs PuckChamp (BO3) - DreamLeague Division 2 Group B | Sports | Kalshi–Polymarket | 5.1¢ | 3 |
| Will WaiterG win the GMGN GGC Season 1 Grand Final? | Other | Polymarket–Predict.fun | 5.0¢ | 3 |
| Will Christopher Luxon be the next Prime Minister of New Zealand after the 2026 elections? | Elections & Politics | Polymarket–Predict.fun | 4.8¢ | 7 |
| Puffpaw FDV above $50M one day after launch? | Crypto | Polymarket–Predict.fun | 3.5¢ | 5 |

## Sports around game time

Games that started 6 to 30 hours ago: 988 of 1,926 pairs traded on both venues in the same minute, 29,182 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 555 | 21,903 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 433 | 7,279 | 1.0¢ | 3.7¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Mobile Legends Bang Bang: Natus Vincere vs Team Liquid ID (BO5) - MPL Indonesia Playoffs | Kalshi–Polymarket | 7.0¢ | 38¢ | 11 |
| Counter-Strike: Drama eSports vs Ryvex - Map 1 Winner | Polymarket–Predict.fun | 5.3¢ | 13¢ | 13 |
| Call of Duty: G2 Minnesota vs Carolina Royal Ravens (BO5) - Monster Launch Invitational Group A | Kalshi–Polymarket | 5.2¢ | 23¢ | 25 |
| Counter-Strike: your end vs Low Cortisol (BO3) - CCT South America Group Stage | Kalshi–Polymarket | 5.0¢ | 10¢ | 62 |
| Spurs vs. Kings: O/U 232.5 | Polymarket–Predict.fun | 4.0¢ | 34¢ | 12 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 30 of 40 | $661 |
| Elections & Politics | Predict.fun | 40 | 5 of 40 | $47.05 |
| Sports | Kalshi | 13 | 7 of 13 | $888 |
| Sports | Polymarket | 38 | 13 of 38 | $1,246 |
| Sports | Predict.fun | 29 | 3 of 29 | $8,512 |
| Crypto | Polymarket | 40 | 15 of 40 | $206 |
| Crypto | Predict.fun | 40 | 6 of 40 | $163 |
| Economics & Finance | Polymarket | 40 | 24 of 40 | $461 |
| Economics & Finance | Predict.fun | 40 | 6 of 40 | $410 |
| Tech & Science | Polymarket | 40 | 20 of 40 | $554 |
| Tech & Science | Predict.fun | 40 | 11 of 40 | $62.72 |
| Other | Polymarket | 40 | 15 of 40 | $291 |
| Other | Predict.fun | 40 | 3 of 40 | $1,400 |

## Settlement

Events that started in the last seven days: 16,593 pairs have settled on both venues and 16,516 settled the same way (100%); 571 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 119 | 119 | 13 |
| Sports | 16,352 | 16,275 | 558 |
| Crypto | 64 | 64 | 0 |
| Economics & Finance | 52 | 52 | 0 |
| Tech & Science | 6 | 6 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 5,591 | 5,526 |
| Polymarket | 16,513 | 16,036 |
| Predict.fun | 12,178 | 11,747 |
| Hyperliquid | 46 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Sara Bejlek wins | Ningbo Open: Sara Bejlek vs Xiyu Wang | kalshi + predictfun | 0.52 | 0.5 |
| Katarzyna Kawa wins | Ningbo Open: Katarzyna Kawa vs Maja Chwalinska | kalshi + predictfun | 0.26 | 0.5 |
| Alexander Bublik wins | Almaty Open: Alexander Bublik vs Fabian Marozsan | kalshi + predictfun | 0.72 | 0.5 |
| Andre Petroski wins | UFC Fight Night: Andre Petroski vs. Azamat Bekoev (Middleweight, Prelims) | kalshi + polymarket | 0.4 | 0.5 |
| Andre Petroski wins | UFC Fight Night: Andre Petroski vs. Azamat Bekoev (Middleweight, Prelims) | kalshi + predictfun | 0.4 | 0.5 |
| Esport BERG wins | Counter-Strike: Esport BERG vs Diamant Esports (BO1) - ESEA Advanced Europe Regular Season | kalshi + predictfun | 0.45 | 0.5 |
| Team Synapse wins | Dota 2: Team Synapse vs Zero Tenacity (BO3) - NEXUS SERIES Playoffs | kalshi + predictfun | 0.6 | 0.5 |
| Radnicki Nis wins | Will FK Radnicki Nis win on 2026-11-02? | kalshi + polymarket | 0.25 | 0.0 |
| Tie is the result | Will FK Radnicki Nis vs. FK Zeleznicar Pancevo end in a draw? | kalshi + polymarket | 0.26 | 1.0 |
| FK Zeleznicar Pancevo wins | Will FK Zeleznicar Pancevo win on 2026-11-02? | kalshi + polymarket | 0.49 | 0.0 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,727) is Sports.
- Every Hyperliquid pair (104) is Sports.
- 332 pairs carry a different category on each side (190 of them point to different divisions); for example "Lorenzo Claverie wins" is Sports on Kalshi and Crypto on Polymarket; "Eric David Verdes wins" is Sports on Kalshi and Culture on Polymarket; "Israel wins" is Sports on Kalshi and World on Polymarket.
- 2,424 pairs have a category on one side only (side without one: Polymarket 2,421, Hyperliquid 2, Predict.fun 1).
- 53 Kalshi–Hyperliquid pairs are matched across different dates; for example "Manchester City wins" and "English Premier League MD 10: Nottingham Forest v Manchester City: Manchester City" (Kalshi 2026-11-07, Hyperliquid 2026-11-14).
- 39 Polymarket–Hyperliquid pairs are matched across different dates; for example "Will Paris Saint-Germain FC win on 2026-11-07?" and "French Ligue 1 Matchday 10: Paris Saint Germain v Troyes: Paris Saint Germain" (Polymarket 2026-11-07, Hyperliquid 2026-11-14).
- 12 Kalshi–Polymarket pairs are matched across different dates; for example "Priscila Cachoeira wins" and "UFC Fight Night: Priscila Cachoeira vs. Nina Miloševic (Women's Bantamweight, Prelims)" (Kalshi 2026-11-06, Polymarket starts 2026-11-07 22:00Z).
- 11 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 7,716 of 9,730 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (46 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
