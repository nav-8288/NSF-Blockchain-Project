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

##Notes

*The current version is address-based, so it analyzes one wallet or contract address at a time.
*Some transactions show 0 ETH because they are smart contract interactions rather than direct ETH transfers.
*Some transactions may have a blank receiver address, which can happen with contract creation transactions.
*Generated CSV files are being kept locally for now instead of being committed to GitHub.

### Next Steps


