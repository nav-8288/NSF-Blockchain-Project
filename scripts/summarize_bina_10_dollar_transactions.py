import pandas as pd

input_file = "data/bina_wallet_likely_10_dollar_transactions.csv"

df = pd.read_csv(input_file)

df["datetime"] = pd.to_datetime(df["datetime"])
df["date"] = df["datetime"].dt.date
df["value_eth"] = pd.to_numeric(df["value_eth"])

print("Bina Wallet Likely $10 Transaction Summary")
print("-----------------------------------------")
print(f"Transaction count: {len(df)}")
print(f"First transaction: {df['datetime'].min()}")
print(f"Last transaction: {df['datetime'].max()}")
print(f"Unique receiving addresses: {df['to'].nunique()}")
print(f"Minimum ETH sent: {df['value_eth'].min():.6f}")
print(f"Maximum ETH sent: {df['value_eth'].max():.6f}")
print(f"Average ETH sent: {df['value_eth'].mean():.6f}")
print(f"Total ETH sent: {df['value_eth'].sum():.6f}")

print("\nTransactions by date:")
print(df.groupby("date").size().reset_index(name="transaction_count").to_string(index=False))
