import pandas as pd
import matplotlib.pyplot as plt

input_file = "data/joe_lubin_large_eth_transfers.csv"
output_file = "analyses/joe_lubin_makerdao_analysis/joe_lubin_large_transfers.png"

df = pd.read_csv(input_file)

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["value_eth"] = pd.to_numeric(df["value_eth"])

print("Joe Lubin Large ETH Transfer Summary")
print("-----------------------------------")
print(f"Large transfers found: {len(df)}")
print(f"First transfer: {df['timestamp'].min()}")
print(f"Last transfer: {df['timestamp'].max()}")
print(f"Total ETH moved: {df['value_eth'].sum():.2f}")
print()
print(df[["timestamp", "to_address", "value_eth", "tx_hash"]].to_string(index=False))

df["transfer_label"] = df["timestamp"].dt.strftime("%Y-%m-%d %H:%M")

plt.figure(figsize=(10, 6))
plt.bar(df["transfer_label"], df["value_eth"])
plt.xlabel("Transfer time")
plt.ylabel("ETH moved")
plt.title("Large ETH Transfers from Lubin-Linked Wallet")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.close()

print()
print(f"Saved chart to {output_file}")
