# Kairos cross-venue report, 2026-11-19

Generated 2026-11-19 20:01 UTC from Kairos's catalog of linked markets, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 764 | 418 | 0 of 191 | 1.0¢ (18 pairs) | 10 of 10 |
| Sports | 3,132 | 2,733 | 0 of 1,406 | 1.0¢ (527 pairs) | 10,379 of 10,411 |
| Crypto | 1,186 | 1,186 | 0 of 294 | 1.8¢ (47 pairs) | 2,816 of 3,171 |
| Economics & Finance | 522 | 461 | 0 of 232 | 1.4¢ (62 pairs) | 178 of 181 |
| Tech & Science | 598 | 592 | 0 of 107 | 1.0¢ (38 pairs) | 285 of 285 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 470 pairs fall outside the six divisions (Culture 470, Entertainment 156, Financials 23, Science and Technology 1).

## Pairs

Kairos listed 6,672 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 5,680 (85%), 158 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 418 of 419 |
| Elections & Politics | Kalshi–Polymarket | 0 of 173 |
| Elections & Politics | Kalshi–Predict.fun | 0 of 172 |
| Sports | Polymarket–Predict.fun | 1,390 of 1,390 |
| Sports | Kalshi–Polymarket | 900 of 909 |
| Sports | Kalshi–Predict.fun | 390 of 560 |
| Sports | Polymarket–Hyperliquid | 0 of 92 |
| Sports | Predict.fun–Hyperliquid | 53 of 92 |
| Sports | Kalshi–Hyperliquid | 0 of 89 |
| Crypto | Polymarket–Predict.fun | 1,186 of 1,186 |
| Economics & Finance | Polymarket–Predict.fun | 461 of 461 |
| Economics & Finance | Kalshi–Predict.fun | 0 of 42 |
| Economics & Finance | Kalshi–Polymarket | 0 of 19 |
| Tech & Science | Polymarket–Predict.fun | 592 of 592 |
| Tech & Science | Kalshi–Polymarket | 0 of 5 |
| Tech & Science | Kalshi–Predict.fun | 0 of 1 |
| Other | Polymarket–Predict.fun | 290 of 290 |
| Other | Kalshi–Polymarket | 0 of 103 |
| Other | Kalshi–Predict.fun | 0 of 77 |

| Not lined up | Pairs |
|---|---|
| not a sports market; questions not compared | 592 |
| different dates | 182 |
| could not confirm both markets ask about the same team | 166 |
| could not line up the outcomes | 40 |
| Kalshi market is inactive | 6 |
| Kalshi market is determined | 3 |
| Kalshi market is finalized | 2 |
| different start times | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 191 | 148 | 12 | 0 |
| Sports | 900 | 4 | 0 | 506 | 96 | 2 | 0 |
| Crypto | 0 | 0 | 0 | 294 | 169 | 5 | 0 |
| Economics & Finance | 0 | 0 | 0 | 232 | 168 | 16 | 0 |
| Tech & Science | 0 | 0 | 0 | 107 | 74 | 5 | 0 |
| Other | 0 | 0 | 0 | 69 | 54 | 10 | 0 |

Not priced: no Predict.fun trades yet 3,328; no live quotes for Hyperliquid yet 53.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 18 | 27 | 1.0¢ | 2.9¢ | 33% |
| Sports | 527 | 2,285 | 1.0¢ | 2.0¢ | 20% |
| Crypto | 47 | 71 | 1.8¢ | 8.8¢ | 46% |
| Economics & Finance | 62 | 309 | 1.4¢ | 9.1¢ | 39% |
| Tech & Science | 38 | 86 | 1.0¢ | 5.0¢ | 37% |
| Other | 33 | 73 | 1.7¢ | 50¢ | 48% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 18 | 1.0¢ | 2.9¢ |
| Sports | Kalshi–Polymarket | 264 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 68 | 1.0¢ | 3.0¢ |
| Sports | Polymarket–Predict.fun | 174 | 1.0¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 21 | 0.6¢ | 1.6¢ |
| Crypto | Polymarket–Predict.fun | 47 | 1.8¢ | 8.8¢ |
| Economics & Finance | Polymarket–Predict.fun | 62 | 1.4¢ | 9.1¢ |
| Tech & Science | Polymarket–Predict.fun | 38 | 1.0¢ | 5.0¢ |
| Other | Polymarket–Predict.fun | 33 | 1.7¢ | 50¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Will "Mo Bamba" by Sheck Wes be on the radio in GTA VI at launch? | Other | Polymarket–Predict.fun | 44¢ | 3 |
| Counter-Strike: Drama eSports vs megoshort (BO3) - CCT Europe Closed Qualifier: Series #15 Group B | Sports | Kalshi–Predict.fun | 11¢ | 3 |
| Will Anthropic’s market cap be between 1.2T and 1.5T at market close on IPO day by December 31 2027? | Economics & Finance | Polymarket–Predict.fun | 9.1¢ | 23 |
| Will the highest temperature in Shenzhen be 19°C on November 20? | Tech & Science | Polymarket–Predict.fun | 9.0¢ | 4 |
| Will Anthropic’s market cap be 1.8T or greater at market close on IPO day by December 31 2027? | Economics & Finance | Polymarket–Predict.fun | 6.2¢ | 22 |
| Will Jensen Huang rejoin NVIDIA by December 31, 2027? | Economics & Finance | Polymarket–Predict.fun | 5.9¢ | 3 |
| ATP World Tour Finals, Ivan Lendl Group: Carlos Alcaraz vs Flavio Cobolli | Sports | Kalshi–Polymarket | 3.9¢ | 21 |
| Will "Despacito" by Luis Fonsi, Daddy Yankee be on the radio in GTA VI at launch? | Other | Polymarket–Predict.fun | 3.5¢ | 3 |

## Sports around game time

Games that started 6 to 30 hours ago: 450 of 652 pairs traded on both venues in the same minute, 17,453 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.3¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 269 | 12,461 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 181 | 4,992 | 1.0¢ | 4.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Counter-Strike: SINQU vs eSuba (BO1) - ESEA Advanced Europe Regular Season | Kalshi–Polymarket | 7.0¢ | 34¢ | 29 |
| Counter-Strike: FORZE Reload vs ex-INOX Division - Map 2 Winner | Polymarket–Predict.fun | 6.0¢ | 17¢ | 11 |
| Valorant: Havoc & Yonder vs Hyper Tide Gaming (BO3) - China National Tournament Split Omega: Pro Division Group B | Kalshi–Polymarket | 6.0¢ | 40¢ | 17 |
| Valorant: Qian Xing Gaming vs SEC (BO3) - China National Tournament Split Omega: Pro Division Group A | Kalshi–Polymarket | 4.2¢ | 28¢ | 32 |
| Dota 2: Team Lynx vs Spirit Academy - Game 1 Winner | Polymarket–Predict.fun | 4.3¢ | 21¢ | 19 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 25 of 40 | $334 |
| Elections & Politics | Predict.fun | 40 | 3 of 40 | $184 |
| Sports | Kalshi | 16 | 11 of 16 | $57.00 |
| Sports | Polymarket | 37 | 9 of 37 | $184 |
| Sports | Predict.fun | 27 | 4 of 27 | $14.54 |
| Crypto | Polymarket | 40 | 9 of 40 | $130 |
| Crypto | Predict.fun | 40 | 7 of 40 | $9.20 |
| Economics & Finance | Polymarket | 40 | 25 of 40 | $576 |
| Economics & Finance | Predict.fun | 40 | 10 of 40 | $261 |
| Tech & Science | Polymarket | 40 | 29 of 40 | $260 |
| Tech & Science | Predict.fun | 40 | 2 of 40 | $595 |
| Other | Polymarket | 40 | 29 of 40 | $648 |
| Other | Predict.fun | 40 | 10 of 40 | $16.55 |

## Settlement

Events that started in the last seven days: 14,131 pairs have settled on both venues and 13,741 settled the same way (97%); 336 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Elections & Politics | 10 | 10 | 2 |
| Sports | 10,411 | 10,379 | 176 |
| Crypto | 3,171 | 2,816 | 0 |
| Economics & Finance | 181 | 178 | 0 |
| Tech & Science | 285 | 285 | 158 |
| Other | 73 | 73 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 3,031 | 3,027 |
| Polymarket | 13,935 | 13,623 |
| Predict.fun | 11,951 | 11,664 |
| Hyperliquid | 17 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Alejandro Davidovich Fokina wins | Rolex Paris Masters: Alejandro Davidovich Fokina vs Moise Kouame | kalshi + predictfun | 0.74 | 0.5 |
| Daniel Merida wins | Rolex Paris Masters: Daniel Merida Aguilar vs Alexander Blockx | kalshi + predictfun | 0.42 | 0.5 |
| Stefanos Tsitsipas wins | Rolex Paris Masters: Stefanos Tsitsipas vs Learner Tien | kalshi + predictfun | 0.45 | 0.5 |
| Nazim Sadykhov wins | UFC 334: Nazim Sadykhov vs. Jefferson Nascimento (Lightweight, Early Prelims) | kalshi + polymarket | 0.7 | 0.5 |
| Adrian Yanez wins | UFC 334: Adrian Yañez vs. Juan Diaz (Bantamweight, Early Prelims) | kalshi + polymarket | 0.53 | 0.5 |
| ex-RUSTEC wins | Counter-Strike: ex-RUSTEC vs Sökerorg (BO3) - CCT Europe Group Stage | kalshi + predictfun | 0.65 | 0.5 |
| Time to Sleep wins | Dota 2: Time to Sleep vs CyberHero (BO3) - Asgard Championship Group B | kalshi + predictfun | 0.19 | 0.5 |
| BORRACHEIROS wins | Counter-Strike: BORRACHEIROS vs your end (BO3) - CCT South America Group Stage | kalshi + predictfun | 0.7 | 0.5 |
| Younglings wins | Counter-Strike: Younglings vs SINQU (BO1) - ESEA Advanced Europe Regular Season | kalshi + polymarket | 0.0 | 0.5 |
| Washington wins | Washington Huskies vs. Utah Utes | kalshi + polymarket | 0.41 | 0.5 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Hyperliquid pair (273) is Sports.
- 1,095 pairs carry a different category on each side (390 of them point to different divisions); for example "Will SpaceX have the highest IPO Market Cap 2026?" is Science on Polymarket and Finance on Predict.fun; "US national Bitcoin reserve before 2027?" is Politics on Polymarket and Crypto on Predict.fun; "Will Bloomberg IPO by December 31, 2026?" is Tech on Polymarket and Finance on Predict.fun.
- 92 Polymarket–Hyperliquid pairs are matched across different dates; for example "NBA Regular Season: Minnesota Timberwolves v New York Knicks" and "Knicks vs. Timberwolves" (Polymarket 2026-11-19, Hyperliquid 2027-02-19).
- 89 Kalshi–Hyperliquid pairs are matched across different dates; for example "NBA Regular Season: Minnesota Timberwolves v New York Knicks" and "New York wins" (Kalshi 2026-11-19, Hyperliquid 2027-02-19).
- 1 Kalshi–Predict.fun pairs are matched across different dates; for example "Spirit Academy wins" and "Dota 2: Spirit Academy vs Team Allied (BO3) - European Pro League Group A" (Kalshi 2026-11-22, Predict.fun 2026-11-17).
- 809 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 3,328 of 4,780 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (17 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos's approved links (`/market-links`; `/matched-markets` until 11 November 2026), every two venues of a link making one pair, and outside sports from Kairos's equivalence clusters around every non-sports Predict.fun market; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
