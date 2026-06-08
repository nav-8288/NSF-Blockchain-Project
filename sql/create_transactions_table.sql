CREATE TABLE transactions (
    tx_hash TEXT PRIMARY KEY,
    block_number BIGINT,
    timestamp TIMESTAMP,
    month TEXT,
    from_address TEXT,
    to_address TEXT,
    value_eth NUMERIC,
    gas BIGINT,
    gas_price_gwei NUMERIC,
    input_preview TEXT,
    is_contract_interaction BOOLEAN
);
