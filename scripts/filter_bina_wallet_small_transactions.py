import pandas as pd

input_file = "data/bina_wallet_outgoing_eth_transactions.csv"
output_file = "data/bina_wallet_likely_10_dollar_transactions.csv"

df = pd.read_csv(input_file)

df["datetime"] = pd.to_datetime(df["datetime"])
df["value_eth"] = pd.to_numeric(df["value_eth"])

# Temporary ETH-value filter for likely ~$10 transactions.
# Around Oct 2025, transactions near 0.0025 ETH are roughly around $10
# depending on ETH/USD price at the time.
filtered = df[
    (df["value_eth"] >= 0.0020) &
    (df["value_eth"] <= 0.0030)
].copy()

filtered = filtered.sort_values("datetime")

filtered.to_csv(output_file, index=False)

print(f"Saved {len(filtered)} likely $10-range transactions to {output_file}")
print()
print(filtered[["datetime", "to", "value_eth", "hash"]].to_string(index=False))
