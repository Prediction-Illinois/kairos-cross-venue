# Kairos cross-venue report, 2026-10-13

Generated 2026-10-13 18:57 UTC from Kairos's matched-market catalog, Market Data API and fee quotes, and Kalshi and Polymarket order books. Pairs are grouped into [Prediction@Illinois](https://prediction-illinois.github.io)'s six market divisions by Kairos's own categories.

## Overview

| Division | Pairs Kairos lists | Lined up | Edge after fees, confirmed | Median gap, last 24 h | Settled the same way, last 7 days |
|---|---|---|---|---|---|
| Elections & Politics | 383 | 383 | 2 of 170 | 0.5¢ (20 pairs) | – |
| Sports | 13,094 | 13,000 | 0 of 3,832 | 0.7¢ (991 pairs) | 10,708 of 10,718 |
| Crypto | 455 | 455 | 0 of 282 | 1.5¢ (49 pairs) | 422 of 422 |
| Economics & Finance | 291 | 291 | 0 of 169 | 0.5¢ (24 pairs) | – |
| Tech & Science | 137 | 137 | 0 of 55 | 1.2¢ (12 pairs) | 2 of 2 |
| Climate & Weather | 0 | 0 | – | – | – |

Another 24 pairs fall outside the six divisions (Culture 24).

## Pairs

Kairos listed 14,384 matched pairs across 6 venue combinations; oracle3-extras lined up the outcomes of 14,290 (99%), 58 of them with a warning such as a postponed game.

![Pairs by division](img/pairs-by-division.png)

| Division | Venues | Lined up |
|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 383 of 383 |
| Sports | Polymarket–Predict.fun | 10,329 of 10,364 |
| Sports | Kalshi–Polymarket | 2,266 of 2,318 |
| Sports | Kalshi–Predict.fun | 278 of 282 |
| Sports | Kalshi–Hyperliquid | 53 of 53 |
| Sports | Polymarket–Hyperliquid | 53 of 53 |
| Sports | Predict.fun–Hyperliquid | 21 of 24 |
| Crypto | Polymarket–Predict.fun | 455 of 455 |
| Economics & Finance | Polymarket–Predict.fun | 291 of 291 |
| Tech & Science | Polymarket–Predict.fun | 137 of 137 |
| Other | Polymarket–Predict.fun | 24 of 24 |

| Not lined up | Pairs |
|---|---|
| different dates | 48 |
| different events | 32 |
| could not confirm both markets ask about the same team | 5 |
| could not tell which outcome is the Kalshi YES outcome | 3 |
| Polymarket market not found | 3 |
| could not line up the outcomes | 3 |

## Live check

Each pair is priced on both venues and checked for a basket that pays more than it costs after both venues' fees. Kalshi and Polymarket have public order books, so their edges are walked down the books. Predict.fun is priced from its last trades, which can be weeks old; the largest of those edges are confirmed with Kairos fee quotes, which walk the live Predict.fun book.

| Division | Priced on live books | Edge after fees | Left after the books | Priced from last trades | Edge on last trades | Checked with fee quotes | Confirmed |
|---|---|---|---|---|---|---|---|
| Elections & Politics | 0 | 0 | 0 | 170 | 103 | 14 | 2 |
| Sports | 2,266 | 1 | 0 | 1,566 | 662 | 15 | 0 |
| Crypto | 0 | 0 | 0 | 282 | 167 | 6 | 0 |
| Economics & Finance | 0 | 0 | 0 | 169 | 106 | 9 | 0 |
| Tech & Science | 0 | 0 | 0 | 55 | 33 | 5 | 0 |
| Other | 0 | 0 | 0 | 21 | 16 | 1 | 0 |

Not priced: no Predict.fun trades yet 9,634; no live quotes for Hyperliquid yet 127.

| Division | Venues | Market A | Market B | Basket | Contracts | Net edge | Checked with | Closes |
|---|---|---|---|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | Will John Fetterman win the 2028 Democratic presidential nomination? | Will John Fetterman win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2300 | Kairos fee quotes | 2028-11-08 |
| Elections & Politics | Polymarket–Predict.fun | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | Will Oprah Winfrey win the 2028 Democratic presidential nomination? | YES on A + NO on B | 250.0 | $0.2300 | Kairos fee quotes | 2028-11-08 |

Net edge is for all the contracts together. It assumes every leg fills at the prices used, both markets settle the same way, and money tied up until settlement costs nothing, which matters for markets that close years from now. Closes is the earlier of the two markets' closing times.

Most edges at the top of the book disappear after fees, in the order books, or once a stale last trade meets the live book.

## Price agreement, last 24 hours

For every pair, both venues' last trades in each hour of the last 24 hours, up to the event's start (a game under way is compared on its pre-game prices only).

![Gap by division](img/gap-by-division.png)

| Division | Pairs compared | Hours compared | Median gap | 90th percentile | Hours 2¢ or more apart |
|---|---|---|---|---|---|
| Elections & Politics | 20 | 70 | 0.5¢ | 1.2¢ | 1% |
| Sports | 991 | 4,768 | 0.7¢ | 2.0¢ | 13% |
| Crypto | 49 | 89 | 1.5¢ | 4.1¢ | 44% |
| Economics & Finance | 24 | 103 | 0.5¢ | 1.4¢ | 6% |
| Tech & Science | 12 | 22 | 1.2¢ | 2.6¢ | 36% |
| Other | 3 | 25 | 1.0¢ | 1.8¢ | 0% |

| Division | Venues | Pairs compared | Median gap | 90th percentile |
|---|---|---|---|---|
| Elections & Politics | Polymarket–Predict.fun | 20 | 0.5¢ | 1.2¢ |
| Sports | Kalshi–Polymarket | 355 | 1.0¢ | 2.0¢ |
| Sports | Kalshi–Predict.fun | 64 | 1.0¢ | 2.0¢ |
| Sports | Polymarket–Predict.fun | 572 | 0.3¢ | 1.8¢ |
| Crypto | Polymarket–Predict.fun | 49 | 1.5¢ | 4.1¢ |
| Economics & Finance | Polymarket–Predict.fun | 24 | 0.5¢ | 1.4¢ |
| Tech & Science | Polymarket–Predict.fun | 12 | 1.2¢ | 2.6¢ |
| Other | Polymarket–Predict.fun | 3 | 1.0¢ | 1.8¢ |

| Most persistent gaps (at least 3 hours compared) | Division | Venues | Median gap | Hours |
|---|---|---|---|---|
| Central Arkansas vs. Tarleton State | Sports | Kalshi–Polymarket | 6.0¢ | 5 |
| Will Gen.G win Worlds 2026? | Sports | Polymarket–Predict.fun | 4.9¢ | 3 |
| Merrimack vs. Dartmouth | Sports | Kalshi–Polymarket | 4.0¢ | 3 |
| Will Bitcoin dip to $80,000 in October? | Crypto | Polymarket–Predict.fun | 2.0¢ | 7 |
| Will Ethereum dip to $2,300 in October? | Crypto | Polymarket–Predict.fun | 1.9¢ | 4 |
| Will Apple release a touchscreen MacBook in 2026? | Tech & Science | Polymarket–Predict.fun | 1.7¢ | 6 |
| Will the US confirm that aliens exist before 2027? | Other | Polymarket–Predict.fun | 1.3¢ | 16 |
| Will 1 Fed rate cut happen in 2026? | Economics & Finance | Polymarket–Predict.fun | 1.2¢ | 6 |

## Sports around game time

Games that started 6 to 30 hours ago: 787 of 1,293 pairs traded on both venues in the same minute, 26,162 minutes in all. The median gap between the two last trades was 1.0¢ and the 90th percentile 3.0¢; before the start the 90th percentile was 2.0¢.

![Gap around game time](img/gap-by-minute.png)

| Venues | Pairs compared | Minutes | Median gap | 90th percentile |
|---|---|---|---|---|
| Kalshi–Polymarket | 473 | 18,042 | 1.0¢ | 3.0¢ |
| Polymarket–Predict.fun | 314 | 8,120 | 1.0¢ | 4.0¢ |

| Most persistent gaps (at least 10 minutes compared) | Venues | Median gap | Largest | Minutes |
|---|---|---|---|---|
| LoL: G2 HEL vs AZ Rising Eterna - Game 1 Winner | Polymarket–Predict.fun | 9.2¢ | 52¢ | 15 |
| KHL: Torpedo vs. Metallurg Magnitogorsk | Kalshi–Polymarket | 6.9¢ | 71¢ | 10 |
| Dota 2: Yakult Brothers vs Zenith - Game 1 Winner | Polymarket–Predict.fun | 4.8¢ | 40¢ | 23 |
| KHL: Ak Bars Kazan vs. HC Sochi | Kalshi–Polymarket | 4.0¢ | 18¢ | 16 |
| LoL: SK Gaming Avarosa vs Blue Otter Europe - Game 2 Winner | Polymarket–Predict.fun | 3.0¢ | 25¢ | 14 |

These are trade prices up to a minute apart, not quotes: a gap shows the venues disagreeing, not an arbitrage that could have been executed.

## Trading activity

24-hour volume from Kairos trade metrics for up to 40 pairs per division, chosen at random each day.

| Division | Venue | Markets sampled | Traded in the last 24 h | Median 24 h volume of those |
|---|---|---|---|---|
| Elections & Politics | Polymarket | 40 | 28 of 40 | $1,315 |
| Elections & Politics | Predict.fun | 40 | 7 of 40 | $1,540 |
| Sports | Kalshi | 9 | 4 of 9 | $8.41 |
| Sports | Polymarket | 38 | 4 of 38 | $1,221 |
| Sports | Predict.fun | 31 | 2 of 31 | $9,296 |
| Sports | Hyperliquid | 2 | 0 of 2 | – |
| Crypto | Polymarket | 40 | 14 of 40 | $191 |
| Crypto | Predict.fun | 40 | 2 of 40 | $234 |
| Economics & Finance | Polymarket | 40 | 23 of 40 | $1,555 |
| Economics & Finance | Predict.fun | 40 | 8 of 40 | $3,490 |
| Tech & Science | Polymarket | 40 | 27 of 40 | $972 |
| Tech & Science | Predict.fun | 40 | 6 of 40 | $21.37 |
| Other | Polymarket | 24 | 14 of 24 | $179 |
| Other | Predict.fun | 24 | 4 of 24 | $11,184 |

## Settlement

Events that started in the last seven days: 11,142 pairs have settled on both venues and 11,132 settled the same way (100%); 388 are still settling or have no result from Kairos.

| Division | Settled on both venues | Same way | Still settling |
|---|---|---|---|
| Sports | 10,718 | 10,708 | 388 |
| Crypto | 422 | 422 | 0 |
| Tech & Science | 2 | 2 | 0 |

| Venue | Markets looked up | Resolved |
|---|---|---|
| Kalshi | 3,694 | 3,673 |
| Polymarket | 11,247 | 11,045 |
| Predict.fun | 7,945 | 7,811 |
| Hyperliquid | 174 | 0 |

| Market A | Market B | Venues | A first outcome paid | B first outcome paid |
|---|---|---|---|---|
| Alex de Minaur wins | Shanghai Rolex Masters: Alex de Minaur vs Alex Molcan | kalshi + polymarket | 0.72 | 0.5 |
| Kangyuan Shi wins | Jinan: Kangyuan Shi vs Akira Santillan | kalshi + polymarket | 0.03 | 0.5 |
| Keegan Smith wins | Jinan: Keegan Smith vs Yuquan Jin | kalshi + polymarket | 0.96 | 0.5 |
| Ann Li wins | Wuhan Tennis Open: Ann Li vs Qinwen Zheng | kalshi + polymarket | 0.29 | 0.5 |
| Belinda Bencic wins | Wuhan Tennis Open: Belinda Bencic vs Shuai Zhang | kalshi + polymarket | 0.82 | 0.5 |
| Iva Jovic wins | Wuhan Tennis Open: Iva Jovic vs Mia Pohankova | kalshi + polymarket | 0.85 | 0.5 |
| Diane Parry wins | Wuhan Tennis Open: Diane Parry vs Anna Kalinskaya | kalshi + polymarket | 0.35 | 0.5 |
| Janice Tjen wins | Wuhan Tennis Open: Janice Tjen vs Oleksandra Oliynykova | kalshi + polymarket | 0.72 | 0.5 |
| Anna Kalinskaya wins | Wuhan Tennis Open: Anna Kalinskaya vs Shuai Zhang | kalshi + polymarket | 0.68 | 0.5 |
| aoyi li wins | M25 Qian Daohu: Shanghui Li vs Lingxi Zhao | kalshi + polymarket | 1.0 | 0.0 |

## Notes for Kairos

- No matched pairs in Climate & Weather.
- Every Kalshi pair (2,653) is Sports.
- Every Hyperliquid pair (130) is Sports.
- 106 pairs carry a different category on each side (102 of them point to different divisions); for example "Chirag Duhan wins" is Sports on Kalshi and Crypto on Polymarket; "Marist wins" is Sports on Kalshi and Culture on Polymarket; "Will a team from LPL (China) win LoL Worlds 2026?" is World on Polymarket and Esports on Predict.fun.
- 1,372 pairs have a category on one side only (side without one: Polymarket 1,372).
- 48 Kalshi–Polymarket pairs are matched across different dates; for example "Yaroslav Demin wins" and "M25 Qian Daohu: Yaroslav Demin vs Filip Peliwo" (Kalshi 2026-10-14, Polymarket starts 2026-10-13 03:00Z).
- 32 Polymarket–Predict.fun pairs are matched across different events; for example "Athletic Club leading at halftime?" (lal-ray-bil-2026-10-10-halftime-result vs lal-lev-bil-2026-09-16-halftime-result).
- 14 more pairs could not be confirmed automatically and were left out (see "Not lined up" above).
- 9,634 of 11,918 pairs with a Predict.fun side have no Predict.fun trades yet (no mark), so they cannot be priced.
- No resolutions came back for Hyperliquid (174 markets whose events started 6 hours to 7 days before the report).

## Method

- Pairs come from Kairos `/matched-markets`; [oracle3-extras](https://github.com/YichengYang-Ethan/oracle3-extras) checks each one on both venues and decides which outcome of market B pays when market A's first outcome pays.
- Divisions follow Kairos's categories (Politics and World: Elections & Politics; Sports and Esports: Sports; Finance: Economics & Finance; Tech and Science: Tech & Science). When the two sides disagree, Sports comes first, then Climate & Weather, Economics & Finance, Elections & Politics, Tech & Science and Crypto.
- The live check uses each venue's published fee schedule (oracle3), Kalshi and Polymarket order books, Kairos marks for Predict.fun last trades and Kairos fee quotes to confirm them.
- Price agreement uses Kairos hourly candles; the sports section uses one-minute candles; trading activity uses `/v1/trades/metrics`; settlement uses `/v1/resolutions`.
- Only aggregates and a few example rows are published here.
