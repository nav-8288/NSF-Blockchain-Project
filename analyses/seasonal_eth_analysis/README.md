# Seasonal Ethereum Transaction Analysis

## Goal

This analysis is part of the smaller blockchain analysis tasks from Week 5.

The goal was to start looking at whether Ethereum transaction activity looks different across certain months. Dr. Ramamurthy mentioned comparing December and March because December can be a period where people sell or move assets, while March may show different market behavior.

For this first version, I compared December 2025 and March 2026 using the monthly top 100 normal ETH transaction dataset.

## Dataset Used

I used the `mainnet_monthly_top100_transactions` table in PostgreSQL.

This table contains the top 100 normal ETH-value transactions for each month from June 2025 through June 2026.

For this analysis, I filtered the dataset to only:

* December 2025
* March 2026

This is not a full Ethereum market-wide analysis. It only compares the largest 100 normal ETH transfers in each selected month.

## Method

I used SQL to summarize the top 100 transactions for each month.

The main values I compared were:

* total ETH moved
* average ETH moved per transaction
* minimum ETH transaction amount
* maximum ETH transaction amount
* top sender addresses
* top receiver addresses

I also created charts to compare the two months visually.

## Summary Results

| Month | Transaction Count | Total ETH Moved | Average ETH Moved | Minimum ETH Moved | Maximum ETH Moved |
|---|---:|---:|---:|---:|---:|
| 2025-12 | 100 | 5,050,111.29 ETH | 50,501.11 ETH | 24,544.00 ETH | 190,778.10 ETH |
| 2026-03 | 100 | 4,845,311.86 ETH | 48,453.12 ETH | 22,149.25 ETH | 294,182.67 ETH |

## Main Finding

December 2025 had slightly more total ETH moved than March 2026 in the top 100 dataset.

December 2025 moved about 5.05 million ETH across the top 100 transactions, while March 2026 moved about 4.85 million ETH.

December also had a slightly higher average transaction amount:

* December 2025 average: about 50,501 ETH
* March 2026 average: about 48,453 ETH

However, March 2026 had the largest single transaction between the two months. The largest March transaction was about 294,183 ETH, while the largest December transaction was about 190,778 ETH.

So the overall result is that December had slightly higher total and average movement, but March had the bigger single spike.

## Top Sender/Receiver Notes

The repeated address patterns from earlier analysis still appeared in this comparison.

For December 2025, one of the top sender and receiver addresses was:

`0x28c6c06298d514db089934071355e5743bf21d60`

This address had already appeared often in the monthly top 10 and top 100 analysis.

For March 2026, one address that stood out was:

`0xa9ac43f5b5e38155a288d1a01d2cbc4478e14573`

This address appeared as the top sender and top receiver by total ETH in the March results.

This suggests that the month-to-month comparison is still heavily affected by large repeated wallet activity, especially exchange-related or custody-style wallets.

## Charts Created

I created three charts for this analysis:

* total ETH moved in December 2025 vs March 2026
* average ETH moved per top 100 transaction
* largest single ETH transaction in each month

The charts help show that December was slightly higher in total and average ETH moved, while March had the larger single transaction.

## Limitations

This analysis only looks at the monthly top 100 normal ETH transfers.

It does not include:

* all Ethereum transactions
* ERC-20 token transfers
* internal transactions
* smart contract-level activity
* ETH/USD price changes
* market price movement

Because of that, this should be treated as a first-pass high-value transaction comparison, not a full market behavior study.

## Next Step

A stronger version of this analysis would compare December and March across multiple years instead of only one December and one March.

Another improvement would be adding ETH price data to compare transaction activity with actual market movement.
