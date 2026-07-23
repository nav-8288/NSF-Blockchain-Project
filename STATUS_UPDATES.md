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



## Week 6: Smaller Blockchain Analysis Tasks

### Work Started

After the Week 5 meeting, I started working on smaller blockchain analysis tasks instead of only focusing on the larger monthly transaction dataset.

The goal this week was to complete a few focused analyses that each have a clear question, a script/query, a result, and at least one visual. I started with two Ethereum-based tasks because they were the most direct to finish with the data and tools I already had.

### Bina Wallet Small Transaction Analysis

The first task I worked on was the small transaction analysis for Dr. Ramamurthy's Ethereum wallet:

`0x3e6937bb87A66E3A4DbE5488A4863f5b29674cC3`

For this analysis, I used the Etherscan API to pull the wallet's normal Ethereum transaction history. Then I filtered for outgoing ETH transactions where this wallet was the sender.

The goal was to look for transactions around the $9.50 to $10.50 range. Since the transaction data gives the value in ETH instead of USD, I first used an approximate ETH range of `0.0020 ETH` to `0.0030 ETH` to identify likely $10-range transactions.

This first pass found 24 likely $10-range outgoing transactions. The transactions ranged from 2024-06-17 to 2025-10-14. Most of the activity was concentrated on 2025-10-14, when 20 of the 24 filtered transactions occurred.

I also created a chart showing the number of likely $10-range transactions by date and added a separate README for the analysis under:

`analyses/bina_wallet_10_dollar_transactions/`

The main limitation is that this is still based on ETH amount, not exact historical USD value. To make it exact, I would need to join each transaction with historical ETH/USD price data and then filter directly between $9.50 and $10.50.

### Ethereum Wallet Transaction Distribution Analysis

The second task I worked on was a transaction distribution analysis for a high-activity Ethereum address:

`0x28c6c06298d514db089934071355e5743bf21d60`

I chose this address because it appeared often in the earlier monthly top 10 and top 100 transaction datasets. Based on earlier label checks, it appears to be exchange-related, so it was a useful example for looking at how a high-activity wallet behaves in the dataset.

For this analysis, I used the monthly top 100 normal ETH transaction table and filtered for rows where this address was the sender. This gave 125 outgoing ETH transactions from June 2025 through June 2026.

Summary results:

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

I created two visuals for this analysis:

* a histogram showing the distribution of outgoing ETH transaction amounts
* a scatter plot showing outgoing ETH transaction values over time

The main thing I noticed is that most transactions were in the tens of thousands of ETH range, but a few very large outliers pulled the average higher than the median. This made the analysis a good example of why both average and median are useful when looking at blockchain transaction amounts.

This analysis was added under:

`analyses/ethereum_wallet_distribution/`

### Current Takeaway

This week helped move the project toward smaller, more focused blockchain analysis examples.

The Bina wallet analysis focused on small outgoing transactions and produced a filtered result, summary, and chart. The Ethereum wallet distribution analysis focused on a high-activity address and produced summary statistics plus two transaction visuals.

Both tasks followed the same basic structure:

Question -> collect/filter data -> summarize results -> create graph -> document findings

### Seasonal Ethereum Transaction Analysis

I also started the seasonal Ethereum analysis task by comparing December 2025 and March 2026.

For this first version, I used the monthly top 100 normal ETH transaction dataset that I already imported into PostgreSQL. I filtered the table for December 2025 and March 2026 and compared the total ETH moved, average ETH moved, minimum transaction amount, maximum transaction amount, and the top sender/receiver addresses for each month.

The summary showed that December 2025 had slightly more total ETH moved than March 2026 in the top 100 dataset. December moved about 5.05 million ETH, while March moved about 4.85 million ETH.

December also had a slightly higher average transaction size, about 50,501 ETH compared to about 48,453 ETH in March. However, March had the largest single transaction, about 294,183 ETH, compared to December's largest transaction of about 190,778 ETH.

I created three charts for this analysis:

* total ETH moved in December 2025 vs March 2026
* average ETH moved per top 100 transaction
* largest single ETH transaction in each month

This is still a first-pass seasonal comparison because it only looks at the top 100 normal ETH transfers for two selected months. It does not include all Ethereum transactions, ERC-20 transfers, internal transactions, or ETH/USD price changes. A stronger version later would compare December and March across multiple years.

### Joe Lubin / MakerDAO-Related ETH Transfer Analysis

I also worked on the Joe Lubin / MakerDAO-related ETH transfer task.

For this analysis, I used the Lubin-linked wallet that I had already started investigating earlier in the project:

`0x1b3cb81e51011b549d78bf720b0d924ac763a7c2`

I queried the wallet's normal outgoing ETH transactions from my local PostgreSQL table and filtered for large transfers greater than or equal to 30,000 ETH.

This returned 8 large outgoing transfers from 2022 through 2026, totaling 426,700 ETH.

The main finding was from June 6, 2026. The large movement did not appear as one single transaction. Instead, it appeared as three separate large outgoing transfers:

* 40,000 ETH
* 40,000 ETH
* 30,000 ETH

Together, those three transactions add up to 110,000 ETH.

This helped clarify my earlier Week 2 result. My first query found the two 40,000 ETH transfers, but it missed the 30,000 ETH transfer because the cutoff was too high. After lowering the cutoff to 30,000 ETH, the full June 6 movement became clearer.

I also created a bar chart showing the large outgoing transfers from the wallet and added a separate README for this analysis under:

`analyses/joe_lubin_makerdao_analysis/`

The current limitation is that this analysis only looks at normal ETH transactions. A deeper version would trace the receiving addresses further and look more closely at the Maker Vault / DSProxy activity.

## Week 7:

### Bitcoin UTXO Transaction Tree Analysis

I also completed the Bitcoin UTXO transaction tree task.

This task was different from the Ethereum analyses because Bitcoin uses the UTXO model instead of Ethereum's account-based model. Instead of tracking one wallet balance, the goal was to follow transaction outputs as they are spent into later transactions.

I first tested the Bitcoin genesis transaction:

`4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b`

The script checked the genesis transaction output and found that the 50 BTC output did not produce a normal forward spend path. I documented this as a special case instead of forcing it into the graph.

After that, I used an early spendable Bitcoin transaction as a practical example and traced the UTXO path forward.

The practical trace produced:

* 12 trace rows
* 8 unique source transactions traced
* max hop reached: 7
* 11 spent outputs followed

Since the hop count starts at 0, reaching hop 7 means the trace covered 8 levels. This goes past the original 4-5 hop goal from the meeting notes.

I also created CSV outputs and graph visualizations for both the genesis test and the practical UTXO example. The graph is intentionally simple, while the CSV contains the output indexes, BTC values, and spent-by transaction IDs.

This task helped me understand how different Bitcoin transaction tracing is compared to Ethereum wallet analysis.

