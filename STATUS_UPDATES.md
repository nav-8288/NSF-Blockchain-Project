# Status Updates

This file is used to keep track of weekly progress for the NSF Blockchain Project. Updates summarize the main work completed, current progress, issues encountered, and next steps.

## Week 1: Project Setup

### Work Completed

*Created the GitHub repository and added an initial README for the NSF Blockchain Project.
*Outlined the main project goals, including collecting Ethereum mainnet transaction data, organizing it by month, and analyzing high-value transactions.
*Reviewed Tejas’s scores/interactions files to understand how Etherscan data can be collected and structured.
*Created an initial Python script based on Tejas’s Etherscan API structure.
*Modified the script to collect full transaction records instead of only wallet addresses.
*Added fields such as transaction hash, timestamp, month, sender address, receiver address, ETH value, gas price, input preview, and smart contract interaction status.
*Moved the Etherscan API key into a .env file and added a .gitignore file.
*Generated a cleaned transaction CSV from real Ethereum mainnet data.
*Installed PostgreSQL, created the nsf_blockchain database, and imported the cleaned transaction data.
*Ran initial SQL queries for row count, top-value transactions, and monthly summaries.
*Exported the SQL results into local CSV files for review.

### Current Focus

Right now, the project has a working address-based pipeline:

Etherscan API -> Python script -> Clean CSV -> PostgreSQL -> SQL analysis

### Notes

*The current version is address-based, so it analyzes one wallet or contract address at a time.
*Some transactions show 0 ETH because they are smart contract interactions rather than direct ETH transfers.
*Some transactions may have a blank receiver address, which can happen with contract creation transactions.
*Generated CSV files are being kept locally for now instead of being committed to GitHub.


## Week 2: Large ETH Transfer Investigation

### Work Completed

* Investigated the recent Joseph Lubin / Consensys-related ETH movement.
* Located the relevant Ethereum wallet address: `0x1b3cb81e51011b549d78bf720b0d924ac763a7c2`.
* Generated a cleaned transaction CSV for the wallet.
* Imported 405 wallet transactions into PostgreSQL as `lubin_actual_transactions`.
* Queried the recent transaction data for transfers greater than or equal to 39,000 ETH.
* Found two separate 40,000 ETH transfers from June 6, 2026.
* Exported the two large-transfer results into a local CSV file for review.
* Checked the receiving wallet addresses on Etherscan to see whether they were connected to MakerDAO/Maker Vault activity.
* Found that one receiving address was labeled as a “Maker Vault Owner.”
* Found that the second receiving address later sent 40,000 ETH to `DSProxy #213,508`.
* Set up BigQuery in the available sandbox/trial environment to test broader Ethereum mainnet transaction analysis.
* Used BigQuery’s public Ethereum mainnet transaction table to move beyond only one wallet or contract address.
* Ran a query to pull the top 10 normal ETH-value transactions for each month from June 2025 through June 2026.
* Exported the monthly top 10 transaction results locally as a CSV file for review.

### Findings

The reported ETH movement does not appear as one single 80,000+ ETH transaction in the wallet’s normal transaction data. Instead, it appears to be split across two separate 40,000 ETH transfers.

| Timestamp           | From Address                                 | To Address                                   | Value      |
| ------------------- | -------------------------------------------- | -------------------------------------------- | ---------- |
| 2026-06-06 00:11:35 | `0x1b3cb81e51011b549d78bf720b0d924ac763a7c2` | `0x22de0b5c40f012782a667ccdaa15406ba1201246` | 40,000 ETH |
| 2026-06-06 00:18:35 | `0x1b3cb81e51011b549d78bf720b0d924ac763a7c2` | `0xabed497d0ccb6916c95dd98ad4402febf5f52fe7` | 40,000 ETH |

Based on Etherscan labels and follow-up transfers, the receiving addresses appear to be connected to MakerDAO/Maker Vault activity. I would describe them as MakerDAO/Maker Vault-related rather than saying they are directly MakerDAO-owned.

The monthly mainnet query is different from the earlier Etherscan work because it looks across Ethereum mainnet transactions instead of only one specific wallet address. For this first monthly analysis, I focused on normal ETH transactions, meaning direct ETH value moved in the transaction itself. The results show the top 10 ETH-value transactions for each month from June 2025 through June 2026.


### Additional Notes

* The current transaction collection script is still address-based, so this investigation was done by first identifying the relevant wallet address and then pulling that wallet’s transaction history.
* The original search for one transaction greater than 80,000 ETH did not return a single matching transaction in the normal transaction data.
* Etherscan labels and follow-up transfers were useful for checking whether the receiving addresses were connected to MakerDAO/Maker Vault activity.
* This investigation helped show how wallet labels, transaction hashes, receiver addresses, and follow-up transfers can be used together to classify large Ethereum movements.
* BigQuery is more useful than Etherscan for broader mainnet-level monthly analysis because Etherscan is mainly practical for wallet or contract-level transaction history.
* The BigQuery monthly query focuses on normal ETH transactions, so it does not include internal transactions, ERC-20 transfers, or other contract-level value movements.
* The monthly results include the month, transaction hash, timestamp, sender address, receiver address, ETH amount, and monthly rank.


## Week 3: Monthly Mainnet Transaction Review

### Work Completed

* Started working with BigQuery in the sandbox/trial environment to test broader Ethereum mainnet transaction analysis.
* Used BigQuery since Etherscan works better for one wallet or contract at a time, while BigQuery lets me look across mainnet transaction data more broadly.
* Spent time learning how to query the public Ethereum mainnet dataset and reviewing fields such as transaction hash, timestamp, sender address, receiver address, and transaction value.
* Reviewed the CSV containing the top 10 normal ETH-value transactions for each month from June 2025 through June 2026.
* Started going through the sender and receiver addresses to see if any repeated patterns stood out.
* Noticed that many of the largest transfers were not random one-time wallets, but repeated high-volume addresses.
* Worked through the monthly query results to see which addresses appeared more than once across the highest-value transactions.
* Manually checked selected repeated addresses on Etherscan to compare the raw BigQuery results with public wallet labels.
* Updated the GitHub weekly notes to document the BigQuery workflow, address patterns, and early classification notes.


### Findings

The monthly top 10 transaction CSV has 130 rows total, with 10 high-value normal ETH transactions for each month from June 2025 through June 2026.

So far, nothing in the CSV looks like an obvious scam or fraud case by itself. A lot of the activity looks more like large exchange or custody wallet movement because the same addresses show up multiple times and move very large amounts of ETH.

One repeated pair that stood out was:

`0x28c6c06298d514db089934071355e5743bf21d60`

and

`0xf977814e90da44bfa03b6295a0616a897441acec`

After checking Etherscan, these appear to be Binance-related wallets. Since they show up more than once and move large amounts of ETH back and forth, this looks more like exchange wallet rebalancing than random suspicious activity.

Another address that stood out was:

`0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43`

This address appeared as a repeated receiver for large ETH transfers. It looks Coinbase-related from the label check, but I still want to check it more because it may be tied to exchange or contract activity.

In March 2026, I also noticed multiple transfers around 250,000 ETH going to:

`0xa9ac43f5b5e38155a288d1a01d2cbc4478e14573`

This address appears to be connected to an OKX hot wallet. The repeated same-size transfers are still interesting, but the label makes it look more like an exchange/custody movement than something clearly suspicious.

Another address I still want to check more is:

`0x77134cbc06cb00b66f4c7e623d5fdbf6777635ec`

This one appeared in a chain movement pattern in June 2026, so I want to look more into whether it has a label, whether it is a wallet or contract, and what other addresses it interacts with.

### Address Notes So Far

| Address | What I found so far |
|---|---|
| `0x28c6c06298d514db089934071355e5743bf21d60` | Appears to be a Binance wallet (Binance 14) and shows up in repeated high-value transfers. |
| `0xf977814e90da44bfa03b6295a0616a897441acec` | Also appears to be Binance-related (Binance Hot Wallet 20) and has repeated movement with the address above. |
| `0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511` | Appears to be a Coinbase wallet (Coinbase 44). |
| `0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43` | Looks Coinbase-related (Coinbase wallet), but I want to check it more because it appears as a repeated receiver. |
| `0xa9ac43f5b5e38155a288d1a01d2cbc4478e14573` | Appears to be connected to an OKX hot wallet (OKX: Hot Wallet 3) and received repeated large transfers. |
| `0x77134cbc06cb00b66f4c7e623d5fdbf6777635ec` | Still needs more checking. It appeared in a June 2026 chain-like transfer pattern. |

### Additional Notes

* The BigQuery results are only showing normal ETH transactions, meaning ETH value moved directly in the transaction.
* These results do not include internal transactions, ERC-20 transfers, or other smart contract-level value movements.
* Right now, I am not calling anything suspicious yet. I am mainly looking for repeated address patterns and checking whether those addresses are known wallets on Etherscan.
* The biggest pattern so far is that many of the top monthly ETH transfers seem to involve major exchange or custody wallets.
* This gives me a starting point for classifying the biggest ETH movements instead of only listing the transactions by value.
* A large part of this week was spent understanding how to move from address-based Etherscan data collection to broader mainnet-level analysis using BigQuery. The work this week was mostly exploratory, so the focus was on learning the dataset, checking whether the query results made sense, and starting to identify repeated wallet patterns.

### Next Steps

* Keep checking repeated addresses on Etherscan for public labels.
* Continue building out the address notes as I identify more repeated wallets.
* Look for repeated sender/receiver pairs across multiple months.
* Start separating the large transfers into groups like exchange movement, custody movement, DeFi-related activity, or unknown.
* Use these notes to help explain what the largest monthly ETH transfers actually represent.
* Prepare the findings so they can later be used for graphs, charts, or presentation slides.



## Week 4: Repeated Address Pattern Analysis

### Work Started

* Continued working with the monthly top 10 Ethereum mainnet transaction CSV from June 2025 through June 2026.
* Imported the CSV into PostgreSQL so I could run local SQL analysis on the results.
* Ran queries to find repeated senders, repeated receivers, and repeated sender/receiver pairs.
* Started using SQL to find patterns instead of only checking each address manually.
* Created an `address_labels` table to separate known exchange/custody or exchange-linked addresses from addresses that were still unclear.

### Findings

The repeated-address queries showed that a lot of the largest ETH transfers were concentrated around a smaller group of high-volume addresses.

The strongest repeated sender was:

`0x28c6c06298d514db089934071355e5743bf21d60`

This address appeared 13 times as a sender and sent about 2.77 million ETH total.

The strongest repeated receiver was:

`0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43`

This address appeared 21 times as a receiver and received about 2.42 million ETH total.

The strongest repeated pair was:

`0x28c6c06298d514db089934071355e5743bf21d60`

to

`0xf977814e90da44bfa03b6295a0616a897441acec`

This pair appeared 9 times and moved over 2.3 million ETH total. Since both addresses appear Binance-related, this looks more like exchange wallet movement or internal rebalancing than random activity.

Another repeated pattern was:

`0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511`

to

`0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43`

This pair appeared 6 times and moved over 900,000 ETH total.

### Continued Review

After the repeated-address queries, I added more labels to the `address_labels` table based on Etherscan checks and funding history. Some addresses that first showed up as unknown appeared connected to Binance, Coinbase, OKX, Kraken, Bitfinex, Deribit, Revolut, Beacon Depositor, Aave staking, and other exchange or staking-related activity.

After adding more labels, I reran the Unknown to Unknown repeated-pair query. The query returned zero repeated Unknown to Unknown pairs, which means the repeated unknown patterns were mostly explained after adding the new labels.

This does not mean that every unknown address has been identified. It only means that the repeated Unknown to Unknown address pairs disappeared after manual review and labeling.

I also checked the largest remaining Unknown to Unknown transfers. A few addresses still had no clear label, but several were connected to known entities or funding sources:

| Transaction          | What I found                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------- |
| 2025-06, 214,893 ETH | Receiver looks like Revolut Cold Wallet. Sender still needs more checking.                |
| 2025-10, 198,289 ETH | Addresses look connected to Deribit 16 and Deribit 8.                                     |
| 2025-12, 166,022 ETH | Sender looks like Beacon Depositor. Receiver still needs more checking.                   |
| 2026-05, 165,021 ETH | Both addresses still need more checking.                                                  |
| 2025-09, 165,010 ETH | Sender appears funded by Unit Treasury. Receiver still needs more checking.               |
| 2025-12, 141,816 ETH | Sender looks like Beacon Depositor. Receiver appears connected to Garrett Bullish.        |
| 2025-08, 141,056 ETH | Sender looks connected to Unit Treasury. Receiver looks like Beacon Depositor.            |
| 2025-12, 112,867 ETH | Addresses look connected to Kraken 183 and Kraken 246.                                    |
| 2025-11, 110,100 ETH | Sender appears funded by Binance 15. Receiver appears to be an Aave ETH staking contract. |
| 2026-06, 107,141 ETH | Addresses appear connected to Bitfinex funding history.                                   |

### Monthly Category Breakdown

I also started summarizing the monthly top 10 transactions by broader category. This helped show how much of each month’s largest ETH movement was connected to exchange/custody or exchange-linked addresses compared to remaining unknown activity.

Several months were mostly exchange/custody or exchange-linked based on the current labels:

| Month   | Exchange/Custody or Exchange-Linked |    Remaining Unknown Activity |
| ------- | ----------------------------------: | ----------------------------: |
| 2025-07 |    10 transactions, about 1.43M ETH |                0 transactions |
| 2025-08 |     9 transactions, about 1.44M ETH | 1 transaction, about 141K ETH |
| 2025-09 |     9 transactions, about 1.44M ETH | 1 transaction, about 165K ETH |
| 2026-03 |    10 transactions, about 1.62M ETH |                0 transactions |

Some months still had a larger amount of remaining unknown activity:

| Month   |     Remaining Unknown Activity |
| ------- | -----------------------------: |
| 2025-12 | 6 transactions, about 697K ETH |
| 2025-10 | 4 transactions, about 498K ETH |
| 2025-06 | 2 transactions, about 322K ETH |
| 2026-05 | 3 transactions, about 313K ETH |
| 2026-06 | 3 transactions, about 289K ETH |

### Current Takeaway

So far, the largest normal ETH transfers in this dataset seem heavily influenced by exchange/custody wallets, exchange-linked wallets, staking-related movement, and large institutional wallet activity.

I am not labeling the unclear addresses as suspicious yet. Some addresses still need more checking, but the repeated high-value patterns mostly seem connected to known exchange or custody activity.

The monthly category breakdown also gives a better direction for the next part of the work. Instead of only checking random addresses, I can focus on months with the most remaining unknown activity, especially December 2025 and October 2025.

### Next Steps

* Keep improving the `address_labels` table as more wallet labels are found.
* Focus on the months with the highest remaining unknown activity, especially December 2025 and October 2025.
* Continue separating large transfers into categories like exchange movement, custody movement, staking-related activity, known entity movement, and unknown activity.
* Prepare the repeated-address and monthly category results for possible charts, tables, or presentation summaries.

## Week 5: Expanding the Monthly Transaction Dataset

### Work Started

* Expanded the BigQuery analysis from the monthly top 10 normal ETH-value transactions to the monthly top 100 transactions.
* Pulled the top 100 normal ETH-value transactions for each month from June 2025 through June 2026.
* Exported the results as a CSV and imported them into PostgreSQL.
* Created a new table called `mainnet_monthly_top100_transactions`.
* Confirmed the new dataset has 1,300 rows, which matches 13 months with 100 transactions per month.
* Started running repeated sender, receiver, and sender/receiver pair queries on the larger dataset.

### Early Findings

The purpose of expanding to the monthly top 100 dataset was to see whether the repeated wallet patterns from Week 4 still appear in a larger sample.

The first queries showed that repeated high-volume wallet activity is still present. One address that stood out again was:

`0x28c6c06298d514db089934071355e5743bf21d60`

This address appeared 125 times as a sender and 97 times as a receiver in the top 100 dataset.

One repeated pair that stood out was:

`0xb5d85cbf7cb3ee0d56b3bb207d5fc4b82f43f511`

to

`0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43`

This pair appeared 33 times and moved about 2.37 million ETH total.

The Binance-related pair from the earlier analysis also still appeared:

`0x28c6c06298d514db089934071355e5743bf21d60`

to

`0xf977814e90da44bfa03b6295a0616a897441acec`

This pair appeared 11 times and moved about 3.04 million ETH total.

### Current Takeaway

The early top 100 results suggest that the repeated address patterns from Week 4 are not only limited to the monthly top 10 transactions. Expanding the dataset gives a better base for checking whether exchange/custody and exchange-linked movement continue to appear in a larger sample of high-value normal ETH transfers.

At the same time, the project direction may shift away from only focusing on large datasets. Dr. Ramamurthy suggested that instead of only using large data, we may be able to do multiple smaller analyses using blockchain data. This could be a good direction because the repeated-address work can still be useful, but it may be combined with smaller case studies or more focused blockchain analysis examples.

### Platform Update

After the earlier BigQuery work, concerns came up about whether Google Storage / BigQuery should be used for the project because of university approval and data storage rules.

For now, I am pausing additional BigQuery work until the preferred platform is clearer. The BigQuery work already completed is still useful because it helped create the monthly transaction datasets and test the repeated-address analysis workflow.

The current workflow has been:

BigQuery public Ethereum data -> CSV export -> PostgreSQL -> repeated address and category analysis

If AWS is preferred, the workflow could likely be adjusted to something like:

AWS S3 / Athena -> CSV export -> PostgreSQL -> repeated address and category analysis

The main analysis process would stay similar. The platform used to collect or query the data may change, but the PostgreSQL analysis, repeated address queries, address label table, and category breakdown approach can still be reused.

Before moving further with AWS, I need to confirm whether I should use AWS Educate, AWS Free Tier / credits, or a UB-approved AWS setup. I also need to confirm whether the next direction should be AWS setup, continued local PostgreSQL analysis, or multiple smaller blockchain analyses.

### Next Steps

* Confirm the preferred AWS route with Dr. Ramamurthy before setting up a full AWS workflow.
* Pause additional BigQuery work until the platform direction is clearer.
* Continue using the exported CSVs and local PostgreSQL database for analysis that has already been completed.
* Discuss whether the project should shift toward multiple smaller blockchain analyses instead of only large-scale transaction datasets.
* Ask what type of smaller analyses would be most useful for the project, such as exchange/custody movement, staking activity, DeFi contracts, wallet classification, or unusual transaction patterns.


