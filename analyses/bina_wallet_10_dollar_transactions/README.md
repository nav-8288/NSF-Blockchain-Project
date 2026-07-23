# Bina Wallet Small Transaction Analysis

## Goal

This analysis is part of the smaller blockchain analysis tasks discussed with Dr. Ramamurthy for Week 5.

Instead of only focusing on one large dataset, the goal is to complete a few focused blockchain analyses that use real wallet or transaction data and produce clear results, queries, and visuals.

For this task, I looked at outgoing transactions from Dr. Ramamurthy's Ethereum wallet and tried to identify small transactions that were likely around the $10 range.

Wallet analyzed:

`0x3e6937bb87A66E3A4DbE5488A4863f5b29674cC3`

## Project Context

During the Week 5 meeting, Dr. Ramamurthy suggested doing multiple smaller blockchain analyses instead of only focusing on large-scale transaction datasets.

The main tasks discussed were:

* Analyzing the Joe Lubin / MakerDAO-related ETH movement.
* Looking at small outgoing transactions from Dr. Ramamurthy's wallet, especially around the $9.50 to $10.50 range.
* Creating transaction distribution graphs for selected Ethereum addresses.
* Comparing general Ethereum activity in December and March.
* Building a Bitcoin UTXO transaction path/tree, since Bitcoin uses the UTXO model while Ethereum uses an account/wallet model.

This wallet analysis is the first smaller analysis I started because it had a specific address and a clear target range.

## Method

I used the Etherscan API to pull normal Ethereum transactions for the wallet address.

After collecting the wallet transaction history, I filtered for:

* outgoing transactions only
* transactions where the wallet was the sender
* transactions with ETH value greater than zero

The original goal was to find transactions in the $9.50 to $10.50 range. One issue is that Ethereum transaction data gives the amount in ETH, not the USD value at the time of the transaction.

Because of that, I first filtered for small outgoing ETH transactions between:

`0.0020 ETH` and `0.0030 ETH`

This range was used as a first approximation for likely $10-range transactions. To confirm the exact dollar value, the next step would be joining each transaction date with historical ETH/USD price data.

## Files Created

* `data/bina_wallet_outgoing_eth_transactions.csv`

  * Full outgoing ETH transaction list for the wallet.

* `data/bina_wallet_likely_10_dollar_transactions.csv`

  * Filtered list of outgoing transactions that are likely around the $10 range based on ETH amount.

* `data/bina_wallet_likely_10_dollar_transactions_by_date.png`

  * Chart showing how many likely $10-range transactions occurred on each date.

## Summary Results

After filtering the outgoing wallet transactions, I found 24 likely $10-range transactions.

| Metric                        |              Result |
| ----------------------------- | ------------------: |
| Likely $10-range transactions |                  24 |
| First transaction             | 2024-06-17 00:10:40 |
| Last transaction              | 2025-10-14 08:04:16 |
| Unique receiving addresses    |                  23 |
| Minimum ETH sent              |        0.002437 ETH |
| Maximum ETH sent              |        0.002881 ETH |
| Average ETH sent              |        0.002545 ETH |
| Total ETH sent                |        0.061092 ETH |

## Transactions by Date

| Date       | Transaction Count |
| ---------- | ----------------: |
| 2024-06-17 |                 2 |
| 2024-06-21 |                 1 |
| 2025-09-29 |                 1 |
| 2025-10-14 |                20 |

## Main Finding

Most of the likely $10-range transactions happened on one date.

Out of the 24 filtered transactions, 20 happened on October 14, 2025. The other 4 transactions were spread across June 2024 and September 2025.

This suggests that the wallet had a cluster of small outgoing ETH transactions around the same approximate value on October 14, 2025.

The filtered transactions also went to 23 unique receiving addresses, so most of the transactions were sent to different wallets.

## Chart Explanation

The chart shows the number of likely $10-range outgoing transactions by date.

The x-axis shows the date, and the y-axis shows how many transactions from the filtered set occurred on that date.

The chart makes the October 14, 2025 cluster easy to see because 20 of the 24 filtered transactions happened on that day.

## Limitations

This is not yet an exact USD-based filter.

The current filter is based on ETH amount, not historical USD value. I used the `0.0020 ETH` to `0.0030 ETH` range as an estimate for likely $10-range transactions.

To make this more exact, I would need to add historical ETH/USD price data and calculate:

`transaction_usd_value = value_eth * historical_eth_usd_price`

Then I could filter directly for:

`$9.50 <= transaction_usd_value <= $10.50`

## Next Step

The next improvement would be adding historical ETH/USD prices for the transaction dates. That would let me confirm which transactions were actually between $9.50 and $10.50 at the time they happened.

For now, this analysis gives a first version of the task by identifying likely $10-range outgoing ETH transactions, summarizing the count and time range, and creating a visual of when the transactions occurred.

