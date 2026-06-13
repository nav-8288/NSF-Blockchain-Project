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


### Next Steps

* Review the top 10 highest-value normal ETH transactions for each month from June 2025 to June 2026.
* Spot-check selected transaction hashes on Etherscan to confirm the BigQuery results.
* Add the BigQuery SQL query to the GitHub repository so the analysis can be reproduced.
* Continue broader month-to-month Ethereum mainnet transaction analysis using BigQuery.
* Continue using PostgreSQL, CSV exports, and SQL-based filtering to organize the results.
* Prepare the monthly results so they can later be used for graphs, charts, or presentation slides.


