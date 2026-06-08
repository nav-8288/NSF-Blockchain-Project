SELECT COUNT(*) FROM transactions;

SELECT 
    timestamp,
    from_address,
    to_address,
    value_eth
FROM transactions
ORDER BY value_eth DESC
LIMIT 10;

SELECT 
    month,
    COUNT(*) AS total_transactions,
    SUM(value_eth) AS total_eth_transferred,
    AVG(value_eth) AS average_eth_value,
    MAX(value_eth) AS highest_eth_value
FROM transactions
GROUP BY month
ORDER BY month;
