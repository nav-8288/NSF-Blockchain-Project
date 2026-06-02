# NSF Blockchain Project

This repository is for my NSF blockchain research project with Dr. Bina Ramamurthy.

The project focuses on collecting and analyzing blockchain transaction data, especially Ethereum mainnet transactions. The main goal is to collect transaction data over time, store it in a structured database, analyze high-value transactions, and turn the results into useful visual insights.

## Project Overview

For this project, I will be working with Ethereum transaction data from the mainnet. The data will include both regular crypto transactions and smart contract transactions.

The transactions will be collected by month and organized in a PostgreSQL database. From there, I will analyze the data to find useful patterns, such as which transactions involve the largest amounts of money, where those transactions are being sent, and whether the receiving addresses are connected to other activity.

The final goal is to find “nuggets” of useful information from the transaction data and present them through graphs, charts, and slides.

## Main Goals

- Set up the GitHub repository for the project
- Collect Ethereum mainnet transactions
- Separate crypto transactions and smart contract transactions
- Organize transactions by month
- Store transaction data in PostgreSQL
- Use PostgreSQL as the RDBMS for analysis
- Find high-value transactions
- Analyze where large transactions are being sent
- Track address-to-address activity
- Create graphs and visualizations from the analysis
- Turn useful findings into presentation slides

## Data Collection

The project will collect Ethereum mainnet transaction data from Etherscan.

The data may include:

- Transaction hash
- Date and time
- Sender address
- Receiver address
- Transaction value
- Smart contract interaction data
- Gas information
- Monthly transaction counts

## Database and Analysis

PostgreSQL will be used to store and organize the transaction data.

Using SQL queries, the project will analyze:

- Number of transactions per month
- Highest-value transactions
- Top sending and receiving addresses
- Address-to-address transaction paths
- Differences between regular ETH transfers and smart contract transactions
- Monthly trends in transaction activity

The goal is not just to collect the data, but to use the database to find patterns that are actually meaningful.

## Visualizations

After the data is analyzed, the results can be turned into visualizations such as:

- Line graphs showing monthly transaction activity
- Graphs showing high-value transaction trends
- Charts comparing crypto transactions and smart contract transactions

These visuals will help explain the findings in a clear way.

## Presentation Slides

A slide presentation will also need to be made for this project.

The first slide should use **AlphaRacoon** as the opening slide for the presentation. After that, the slides can introduce the project, explain the data collection process, show how PostgreSQL is being used, and present the transaction analysis results.

Possible slide structure:

1. **AlphaRacoon / Title Slide**
2. Project overview
3. Why is Ethereum transaction data useful
4. Data collection process
5. Etherscan mainnet transaction data
6. PostgreSQL / RDBMS setup
7. Monthly transaction analysis
8. High-value transaction analysis
9. Address-to-address activity
10. Graphs and visual results
11. Key findings
12. Conclusion

## Tech Stack

- Python
- PostgreSQL
- SQL
- Etherscan
- Pandas
- GitHub

## Current Status

This project is currently in the setup phase. The GitHub repository is being created, and the next steps are to begin collecting Ethereum mainnet transaction data, designing the PostgreSQL database, and building the first analysis queries.

## Author

Arnav Nanda  
NSF Blockchain Project  
Research with Professor Bina Ramamurthy
