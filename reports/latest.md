# Kairos cross-venue report, 2026-11-24

Generated 2026-11-24 21:58 UTC from Kairos's catalog of linked markets, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 878 | 528 | 0 of 213 | 1.5¢ (37 pairs) | – |
| Sports | 2,596 | 2,329 | 2 of 1,185 | 1.0¢ (381 pairs) | 5,800 of 5,844 |
| Crypto | 1,228 | 1,228 | 0 of 317 | 1.0¢ (21 pairs) | 5,184 of 5,859 |
| Economics & Finance | 447 | 409 | 0 of 215 | 0.5¢ (35 pairs) | 213 of 214 |
| Tech & Science | 601 | 595 | 0 of 113 | 2.9¢ (55 pairs) | 1,071 of 1,073 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 409 pairs fall outside the six divisions (Culture 409, Entertainment 156, Science and Technology 1).

## Pairs

Kairos listed 6,159 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 5,340 (87%), 84 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 528 of 529 |
| Elections & Politics | Kalshi–Polymarket | 0 of 175 |
| Elections & Politics | Kalshi–Predict.fun | 0 of 174 |
| Sports | Polymarket–Predict.fun | 1,210 of 1,210 |
| Sports | Kalshi–Polymarket | 799 of 805 |
| Sports | Kalshi–Predict.fun | 291 of 448 |
| Sports | Polymarket–Hyperliquid | 0 of 45 |
| Sports | Predict.fun–Hyperliquid | 29 of 45 |
| Sports | Kalshi–Hyperliquid | 0 of 43 |
| Crypto | Polymarket–Predict.fun | 1,228 of 1,228 |
| Economics & Finance | Polymarket–Predict.fun | 409 of 409 |
| Economics & Finance | Kalshi–Polymarket | 0 of 19 |
| Economics & Finance | Kalshi–Predict.fun | 0 of 19 |
| Tech & Science | Polymarket–Predict.fun | 595 of 595 |
| Tech & Science | Kalshi–Polymarket | 0 of 5 |
| Tech & Science | Kalshi–Predict.fun | 0 of 1 |
| Other | Polymarket–Predict.fun | 251 of 252 |
| Other | Kalshi–Polymarket | 0 of 80 |
| Other | Kalshi–Predict.fun | 0 of 77 |

| Not lined up | Pairs |
|---|---|
| not a sports market; questions not compared | 550 |
| could not confirm both markets ask about the same team | 150 |
| different dates | 82 |
| Kalshi market is finalized | 17 |
| could not line up the outcomes | 17 |
| could not tell which outcome is the Kalshi YES outcome | 2 |
| Polymarket market not found | 1 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 213 | 171 | 15 | 0 |
| Sports | 799 | 3 | 2 | 386 | 124 | 3 | 0 |
| Crypto | 0 | 0 | 0 | 317 | 182 | 5 | 0 |
| Economics & Finance | 0 | 0 | 0 | 215 | 156 | 15 | 0 |
| Tech & Science | 0 | 0 | 0 | 113 | 82 | 5 | 0 |
| Other | 0 | 0 | 0 | 65 | 50 | 7 | 0 |

Not priced: no Predict.fun trades yet 3,203; no live quotes for Hyperliquid yet 29.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Sports | Kalshi–Polymarket | Noemy De Bessa wins | W15 Lousada: Noemy De Bessa vs Valentina Losciale | YES on A + NO on B | 0.38 | $0.0105 | order books | 2026-12-02 |
| Sports | Kalshi–Polymarket | Alexander Wagner wins | M15 Antalya: Alexander Wagner vs Heorhii Shylov | YES on A + NO on B | 7.0 | $0.0081 | order books | 2026-12-02 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 37 | 100 | 1.5¢ | 5.6¢ | 44% |
| Sports | 381 | 1,893 | 1.0¢ | 2.0¢ | 20% |
| Crypto | 21 | 44 | 1.0¢ | 9.8¢ | 48% |
| Economics & Finance | 35 | 140 | 0.5¢ | 4.4¢ | 19% |
| Tech & Science | 55 | 121 | 2.9¢ | 18¢ | 62% |
| Other | 17 | 39 | 0.7¢ | 3.1¢ | 26% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 37 | 1.5¢ | 5.6¢ |
| Sports | Kalshi–Polymarket | 211 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 45 | 1.0¢ | 3.0¢ |
| Sports | Polymarket–Predict.fun | 123 | 0.2¢ | 2.0¢ |
| Sports | Predict.fun–Hyperliquid | 2 | 0.2¢ | 8.6¢ |
| Crypto | Polymarket–Predict.fun | 21 | 1.0¢ | 9.8¢ |
| Economics & Finance | Polymarket–Predict.fun | 35 | 0.5¢ | 4.4¢ |
| Tech & Science | Polymarket–Predict.fun | 55 | 2.9¢ | 18¢ |
| Other | Polymarket–Predict.fun | 17 | 0.7¢ | 3.1¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Will the highest temperature in Shenzhen be 20°C on November 25? | Tech & Science | Polymarket–Predict.fun | 18¢ | 3 |
| New NVIDIA CEO named by December 31, 2026? | Economics & Finance | Polymarket–Predict.fun | 15¢ | 4 |
| Fourth Jensen Huang affair reported by December 31? | Tech & Science | Polymarket–Predict.fun | 7.7¢ | 12 |
| Will the highest temperature in Shanghai be 14°C on November 25? | Tech & Science | Polymarket–Predict.fun | 7.0¢ | 4 |
| Counter-Strike: FlyQuest RED vs Milk (BO3) - CROSSFIRE Playoffs | Sports | Kalshi–Polymarket | 6.0¢ | 7 |
| AI bubble burst in 2026? | Economics & Finance | Polymarket–Predict.fun | 4.5¢ | 3 |
| Will Variational launch a token by December 31, 2026? | Crypto | Polymarket–Predict.fun | 4.3¢ | 4 |
| Will NVIDIA (NVDA) hit (HIGH) $176 in November? | Economics & Finance | Polymarket–Predict.fun | 4.1¢ | 4 |

## Sports around game time

Games that started 6 to 30 hours ago: 497 of 830 pairs traded on both venues in the same minute, 21,193 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 316 | 15,797 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 181 | 5,396 | 1.0¢ | 3.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| Counter-Strike: Lilmix vs maybe - Map 1 Winner | Polymarket–Predict.fun | 3.9¢ | 20¢ | 22 |
| Valorant: University War vs ARG.MIX (BO3) - VCT Americas Kickoff: LATAM South - Qualifier Group Stage | Kalshi–Polymarket | 3.0¢ | 31¢ | 64 |
| KHL: Salavat Yulaev Ufa vs. Neftekhimik Nizhnekamsk | Kalshi–Polymarket | 3.0¢ | 13¢ | 21 |
| KHL: Metallurg Magnitogorsk vs. Dinamo Minsk | Kalshi–Polymarket | 2.0¢ | 6.0¢ | 18 |
| Dota 2: PuckChamp vs InterActive Philippines - Game 1 Winner | Polymarket–Predict.fun | 3.0¢ | 13¢ | 23 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 28 of 40 | $490 |
| Elections & Politics | Predict.fun | 40 | 3 of 40 | $6.29 |
| Sports | Kalshi | 19 | 12 of 19 | $89.48 |
| Sports | Polymarket | 32 | 15 of 32 | $296 |
| Sports | Predict.fun | 29 | 4 of 29 | $764 |
| Crypto | Polymarket | 40 | 9 of 40 | $6,169 |
| Crypto | Predict.fun | 40 | 5 of 40 | $178 |
| Economics & Finance | Polymarket | 40 | 29 of 40 | $680 |
| Economics & Finance | Predict.fun | 40 | 7 of 40 | $432 |
| Tech & Science | Polymarket | 40 | 35 of 40 | $939 |
| Tech & Science | Predict.fun | 40 | 8 of 40 | $47.99 |
| Other | Polymarket | 40 | 25 of 40 | $1,847 |
| Other | Predict.fun | 40 | 8 of 40 | $300 |

## Settlement

Events that started in the last seven days: 13,022 pairs have settled on both venues and 12,300 settled the same way (94%); 178 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Sports | 5,844 | 5,800 | 90 |
| Crypto | 5,859 | 5,184 | 0 |
| Economics & Finance | 214 | 213 | 0 |
| Tech & Science | 1,073 | 1,071 | 88 |
| Other | 32 | 32 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 2,976 | 2,971 |
| Polymarket | 12,499 | 12,364 |
| Predict.fun | 10,892 | 10,767 |
| Hyperliquid | 33 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Matteo Berrettini wins | Rolex Paris Masters: Matteo Berrettini vs Carlos Alcaraz | kalshi + predictfun | 0.16 | 0.5 |
| Tomas Martin Etcheverry wins | BNP Paribas Nordic Open: Tomas Etcheverry vs Thiago Agustin Tirante | kalshi + predictfun | 0.54 | 0.5 |
| Pepperdine wins | Pepperdine Waves vs. Oregon Ducks | kalshi + predictfun | 0.09 | 0.5 |
| Leo Team wins | Counter-Strike: Leo Team vs Honvéd (BO3) - CCT Europe Group Stage | kalshi + predictfun | 0.7 | 0.5 |
| Tulpar wins | Counter-Strike: Tulpar vs Revise (BO3) - Exort Fiesta Closed Qualifier: Series #4 Play-in | kalshi + predictfun | 0.44 | 0.5 |
| BRUTE SQ wins | Counter-Strike: BRUTE SQ vs STATE (BO3) - United21 Playoffs | kalshi + predictfun | 0.3 | 0.5 |
| Axorfy Gaming wins | Counter-Strike: Axorfy Gaming vs MEIA NOITE (BO3) - CCT South America Challengers #4 Playoffs | kalshi + predictfun | 0.68 | 0.5 |
| Bitcoin Up or Down - November 17, 5:45PM-5:50PM ET | Bitcoin Up or Down - November 17, 5:45PM-5:50PM ET | polymarket + predictfun | 1.0 | 0.0 |
| Bitcoin Up or Down - November 17, 5:50PM-5:55PM ET | Bitcoin Up or Down - November 17, 5:50PM-5:55PM ET | polymarket + predictfun | 0.0 | 1.0 |
| Ethereum Up or Down - November 17, 6:20PM-6:25PM ET | Ethereum Up or Down - November 17, 6:20PM-6:25PM ET | polymarket + predictfun | 0.0 | 1.0 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Hyperliquid pair (133) is Sports.
- 1,025 pairs carry a different category on each side (366 of them point to different divisions); for example "Ledger IPO closing market cap above $1B?" is Crypto on Polymarket and Finance on Predict.fun; "Will SpaceX have the highest IPO Market Cap 2026?" is Science on Polymarket and Finance on Predict.fun; "US national Bitcoin reserve before 2027?" is Politics on Polymarket and Crypto on Predict.fun.
- 45 Polymarket–Hyperliquid pairs are matched across different dates; for example "UEFA Champions League Matchday 5: RB Leipzig v RC Lens: RB Leipzig" and "Will RB Leipzig win on 2026-11-24?" (Polymarket 2026-11-24, Hyperliquid 2027-02-24).
- 37 Kalshi–Hyperliquid pairs are matched across different dates; for example "NBA Regular Season: Orlando Magic v Detroit Pistons" and "Detroit wins" (Kalshi 2026-11-24, Hyperliquid 2027-02-24).
- 737 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 3,203 of 4,541 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (33 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos's approved links (`/market-links`; `/matched-markets` until 11 November 2026), every two venues of a link making one pair, and outside sports from Kairos's equivalence clusters around every non-sports Predict.fun market; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
