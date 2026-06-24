-- Week 4: Repeated Address and Transaction Pair Analysis
-- This file analyzes repeated senders, receivers, and address pairs
-- from the monthly top 10 Ethereum mainnet transaction dataset.

-- Repeated sender addresses
SELECT 
    from_address AS address,
    COUNT(*) AS times_as_sender,
    SUM(value_eth) AS total_eth_sent
FROM mainnet_monthly_top10_transactions
GROUP BY from_address
ORDER BY times_as_sender DESC, total_eth_sent DESC
LIMIT 20;

-- Repeated receiver addresses
SELECT 
    to_address AS address,
    COUNT(*) AS times_as_receiver,
    SUM(value_eth) AS total_eth_received
FROM mainnet_monthly_top10_transactions
GROUP BY to_address
ORDER BY times_as_receiver DESC, total_eth_received DESC
LIMIT 20;

-- Repeated sender/receiver pairs
SELECT 
    from_address,
    to_address,
    COUNT(*) AS times_seen,
    SUM(value_eth) AS total_eth_moved
FROM mainnet_monthly_top10_transactions
GROUP BY from_address, to_address
ORDER BY times_seen DESC, total_eth_moved DESC
LIMIT 20;
