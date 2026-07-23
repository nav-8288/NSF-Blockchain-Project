-- Joe Lubin / MakerDAO-related ETH transfer analysis
-- Wallet analyzed:
-- 0x1b3cb81e51011b549d78bf720b0d924ac763a7c2

-- Find large outgoing ETH transfers from the Lubin-linked wallet.
-- The cutoff is 30,000 ETH because the large movement appears split
-- across multiple transactions.

SELECT
    timestamp,
    tx_hash,
    from_address,
    to_address,
    value_eth
FROM lubin_actual_transactions
WHERE LOWER(from_address) = LOWER('0x1b3cb81e51011b549d78bf720b0d924ac763a7c2')
  AND value_eth >= 30000
ORDER BY timestamp;

-- Summarize the number and total value of large outgoing transfers.

SELECT
    COUNT(*) AS large_transfer_count,
    SUM(value_eth) AS total_eth_moved
FROM lubin_actual_transactions
WHERE LOWER(from_address) = LOWER('0x1b3cb81e51011b549d78bf720b0d924ac763a7c2')
  AND value_eth >= 30000;

-- Focus only on the June 6, 2026 movement.

SELECT
    timestamp,
    tx_hash,
    from_address,
    to_address,
    value_eth
FROM lubin_actual_transactions
WHERE LOWER(from_address) = LOWER('0x1b3cb81e51011b549d78bf720b0d924ac763a7c2')
  AND timestamp >= '2026-06-06'
  AND timestamp < '2026-06-07'
  AND value_eth >= 30000
ORDER BY timestamp;

-- Total ETH moved on June 6, 2026 through large outgoing transfers.

SELECT
    COUNT(*) AS june_6_large_transfer_count,
    SUM(value_eth) AS june_6_total_eth_moved
FROM lubin_actual_transactions
WHERE LOWER(from_address) = LOWER('0x1b3cb81e51011b549d78bf720b0d924ac763a7c2')
  AND timestamp >= '2026-06-06'
  AND timestamp < '2026-06-07'
  AND value_eth >= 30000;
