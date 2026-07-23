import pandas as pd
import matplotlib.pyplot as plt

input_file = "data/binance_related_wallet_top100_outgoing.csv"

hist_output = "analyses/ethereum_wallet_distribution/binance_related_wallet_top100_distribution.png"
time_output = "analyses/ethereum_wallet_distribution/binance_related_wallet_top100_over_time.png"

df = pd.read_csv(input_file)

df["block_timestamp"] = pd.to_datetime(df["block_timestamp"])
df["value_eth"] = pd.to_numeric(df["value_eth"])

print("Ethereum Wallet Distribution Summary")
print("------------------------------------")
print("Wallet address: 0x28c6c06298d514db089934071355e5743bf21d60")
print(f"Outgoing transactions in top 100 dataset: {len(df)}")
print(f"First transaction: {df['block_timestamp'].min()}")
print(f"Last transaction: {df['block_timestamp'].max()}")
print(f"Minimum ETH sent: {df['value_eth'].min():.6f}")
print(f"Maximum ETH sent: {df['value_eth'].max():.6f}")
print(f"Average ETH sent: {df['value_eth'].mean():.6f}")
print(f"Median ETH sent: {df['value_eth'].median():.6f}")
print(f"Total ETH sent: {df['value_eth'].sum():.6f}")

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df["value_eth"], bins=20)
plt.xlabel("ETH Sent")
plt.ylabel("Transaction Count")
plt.title("Distribution of Outgoing ETH Amounts in Top 100 Dataset")
plt.tight_layout()
plt.savefig(hist_output, dpi=300)
plt.close()

# Scatter plot over time
plt.figure(figsize=(10, 6))
plt.scatter(df["block_timestamp"], df["value_eth"], s=20)
plt.xlabel("Date")
plt.ylabel("ETH Sent")
plt.title("Outgoing ETH Transaction Values Over Time")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(time_output, dpi=300)
plt.close()

print()
print(f"Saved histogram to {hist_output}")
print(f"Saved time graph to {time_output}")
