-- Top 10 highest normal ETH-value transactions for each month
-- Date range: June 2025 through June 2026
-- Source: BigQuery public Ethereum mainnet transactions table


SELECT
  FORMAT_DATE('%Y-%m', DATE(block_timestamp)) AS month,
  `hash` AS tx_hash,
  block_timestamp,
  from_address,
  to_address,
  SAFE_CAST(value AS BIGNUMERIC) / 1000000000000000000 AS value_eth,
  ROW_NUMBER() OVER (
    PARTITION BY FORMAT_DATE('%Y-%m', DATE(block_timestamp))
    ORDER BY SAFE_CAST(value AS BIGNUMERIC) DESC
  ) AS monthly_rank
FROM `bigquery-public-data.crypto_ethereum.transactions`
WHERE block_timestamp >= '2025-06-01'
  AND block_timestamp < '2026-07-01'
  AND value IS NOT NULL
  AND SAFE_CAST(value AS BIGNUMERIC) > 0
QUALIFY monthly_rank <= 10
ORDER BY month, monthly_rank;
