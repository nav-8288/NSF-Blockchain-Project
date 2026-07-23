# Ethereum Wallet Transaction Distribution Analysis

## Goal

This analysis is one of the smaller blockchain analysis tasks from Week 5.

The goal was to take one active Ethereum address and look at the distribution of its outgoing ETH transaction amounts. This is meant to be a reusable type of analysis, where the same idea could be applied to other wallets later.

## Wallet Analyzed

`0x28c6c06298d514db089934071355e5743bf21d60`

I chose this address because it showed up many times in my earlier monthly top 10 and monthly top 100 Ethereum transaction analysis. It was one of the strongest repeated sender/receiver addresses in the larger dataset.

Based on my earlier label checks, this address appears to be exchange-related, so this analysis is mainly looking at how a high-activity exchange/custody-style wallet behaves inside the top 100 dataset.

## Dataset Used

For this analysis, I used the monthly top 100 normal ETH-value transaction dataset from June 2025 through June 2026.

This is important because this analysis is not looking at the wallet's full Ethereum history. It only looks at the transactions from this wallet that appeared inside the monthly top 100 dataset.

So the question for this analysis is:

> When this address appears as a sender in the monthly top 100 dataset, what do its outgoing ETH transaction amounts look like?

## Method

I filtered the `mainnet_monthly_top100_transactions` table for rows where this address was the sender.

Then I calculated basic summary statistics for the outgoing ETH amounts:

* transaction count
* first and last transaction date
* minimum transaction amount
* maximum transaction amount
* average transaction amount
* median transaction amount
* total ETH sent

I also created two graphs:

* a histogram of outgoing ETH amounts
* a scatter plot of outgoing ETH amounts over time

## Summary Results

| Metric                                   |               Result |
| ---------------------------------------- | -------------------: |
| Outgoing transactions in top 100 dataset |                  125 |
| First transaction                        |  2025-06-02 06:48:35 |
| Last transaction                         |  2026-06-27 13:04:23 |
| Minimum ETH sent                         |    22,157.641303 ETH |
| Maximum ETH sent                         |   539,595.961000 ETH |
| Average ETH sent                         |    60,190.799273 ETH |
| Median ETH sent                          |    35,090.515351 ETH |
| Total ETH sent                           | 7,523,849.909111 ETH |

## What I Found

This address was very active in the monthly top 100 dataset. It appeared as the sender for 125 outgoing ETH transactions.

Most of the transactions were in the tens of thousands of ETH range, but there were also a few very large outliers. The largest transaction in this filtered set was about 539,596 ETH.

The average outgoing transaction amount was about 60,191 ETH, while the median was about 35,091 ETH. Since the average is much higher than the median, the distribution is being pulled upward by a smaller number of very large transactions.

## Chart Notes

The histogram shows that most outgoing transactions are grouped toward the lower end of the range, while only a few transactions are extremely large.

The scatter plot shows when the outgoing transfers occurred over time. It shows that this wallet had repeated high-value outgoing transactions across the June 2025 to June 2026 period, with a few major spikes.

## Limitations

This is not a full wallet history analysis.

It only includes this wallet's outgoing transactions that appeared in the monthly top 100 normal ETH-value dataset. There may be many other transactions from this wallet that are not included here because they were not large enough to appear in the monthly top 100 list.

Also, this analysis only looks at normal ETH transfers. It does not include ERC-20 token transfers, internal transactions, or other smart contract-level activity.

## Next Step

This analysis can be reused for other Ethereum addresses by changing the selected wallet address. A useful next step would be to compare this exchange-related wallet with another type of wallet, such as a DeFi contract, staking-related address, or individual wallet.

