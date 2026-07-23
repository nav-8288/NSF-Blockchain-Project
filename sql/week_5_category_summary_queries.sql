-- Week 5: Category Summary and Visualization Prep
-- These queries use the Week 4 address_labels table to summarize the
-- monthly top 10 Ethereum mainnet transactions by broad category.

-- 1. Overall category summary across the full dataset

WITH categorized AS (
    SELECT
        CASE
            WHEN COALESCE(fl.category, 'Unknown') ILIKE '%Exchange%'
              OR COALESCE(tl.category, 'Unknown') ILIKE '%Exchange%'
                THEN 'Exchange/Custody or Exchange-Linked'
            WHEN COALESCE(fl.category, 'Unknown') = 'Unknown'
              OR COALESCE(tl.category, 'Unknown') = 'Unknown'
                THEN 'Remaining Unknown Activity'
            ELSE 'Other Known Activity'
        END AS broad_category,
        t.value_eth
    FROM mainnet_monthly_top10_transactions t
    LEFT JOIN address_labels fl
        ON LOWER(t.from_address) = LOWER(fl.address)
    LEFT JOIN address_labels tl
        ON LOWER(t.to_address) = LOWER(tl.address)
)
SELECT
    broad_category,
    COUNT(*) AS transaction_count,
    ROUND(SUM(value_eth), 2) AS total_eth,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percent_of_transactions,
    ROUND(100.0 * SUM(value_eth) / SUM(SUM(value_eth)) OVER (), 2) AS percent_of_eth
FROM categorized
GROUP BY broad_category
ORDER BY total_eth DESC;


-- 2. Monthly category breakdown for charting

SELECT
    t.month,
    CASE
        WHEN COALESCE(fl.category, 'Unknown') ILIKE '%Exchange%'
          OR COALESCE(tl.category, 'Unknown') ILIKE '%Exchange%'
            THEN 'Exchange/Custody or Exchange-Linked'
        WHEN COALESCE(fl.category, 'Unknown') = 'Unknown'
          OR COALESCE(tl.category, 'Unknown') = 'Unknown'
            THEN 'Remaining Unknown Activity'
        ELSE 'Other Known Activity'
    END AS broad_category,
    COUNT(*) AS transaction_count,
    ROUND(SUM(t.value_eth), 2) AS total_eth
FROM mainnet_monthly_top10_transactions t
LEFT JOIN address_labels fl
    ON LOWER(t.from_address) = LOWER(fl.address)
LEFT JOIN address_labels tl
    ON LOWER(t.to_address) = LOWER(tl.address)
GROUP BY t.month, broad_category
ORDER BY t.month, broad_category;


-- 3. Export monthly category breakdown to CSV
-- This CSV is kept locally in the data folder and can be used for charts.

\copy (
    SELECT
        t.month,
        CASE
            WHEN COALESCE(fl.category, 'Unknown') ILIKE '%Exchange%'
              OR COALESCE(tl.category, 'Unknown') ILIKE '%Exchange%'
                THEN 'Exchange/Custody or Exchange-Linked'
            WHEN COALESCE(fl.category, 'Unknown') = 'Unknown'
              OR COALESCE(tl.category, 'Unknown') = 'Unknown'
                THEN 'Remaining Unknown Activity'
            ELSE 'Other Known Activity'
        END AS broad_category,
        COUNT(*) AS transaction_count,
        ROUND(SUM(t.value_eth), 2) AS total_eth
    FROM mainnet_monthly_top10_transactions t
    LEFT JOIN address_labels fl
        ON LOWER(t.from_address) = LOWER(fl.address)
    LEFT JOIN address_labels tl
        ON LOWER(t.to_address) = LOWER(tl.address)
    GROUP BY t.month, broad_category
    ORDER BY t.month, broad_category
) TO '/Users/Arnav/Desktop/NSF-Blockchain-Project/data/monthly_category_breakdown.csv' WITH CSV HEADER;
