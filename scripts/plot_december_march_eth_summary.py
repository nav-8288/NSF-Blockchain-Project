import pandas as pd
import matplotlib.pyplot as plt

input_file = "data/december_march_eth_summary.csv"

total_output = "analyses/seasonal_eth_analysis/december_march_total_eth_moved.png"
avg_output = "analyses/seasonal_eth_analysis/december_march_average_eth_moved.png"
max_output = "analyses/seasonal_eth_analysis/december_march_largest_transaction.png"

df = pd.read_csv(input_file)

print("December vs March ETH Summary")
print("-----------------------------")
print(df.to_string(index=False))

# Convert total ETH moved into millions for cleaner chart labels
df["total_eth_moved_millions"] = df["total_eth_moved"] / 1_000_000

# Chart 1: Total ETH moved
plt.figure(figsize=(8, 6))
plt.bar(df["month"], df["total_eth_moved_millions"])
plt.xlabel("Month")
plt.ylabel("Total ETH moved, in millions")
plt.title("Total ETH Moved: December 2025 vs March 2026")
plt.tight_layout()
plt.savefig(total_output, dpi=300)
plt.close()

# Chart 2: Average ETH moved
plt.figure(figsize=(8, 6))
plt.bar(df["month"], df["avg_eth_moved"])
plt.xlabel("Month")
plt.ylabel("Average ETH per transaction")
plt.title("Average ETH per Top 100 Transaction")
plt.tight_layout()
plt.savefig(avg_output, dpi=300)
plt.close()

# Chart 3: Largest single transaction
plt.figure(figsize=(8, 6))
plt.bar(df["month"], df["max_eth_moved"])
plt.xlabel("Month")
plt.ylabel("Largest single transaction, ETH")
plt.title("Largest Single ETH Transaction: December vs March")
plt.tight_layout()
plt.savefig(max_output, dpi=300)
plt.close()

print()
print(f"Saved total ETH chart to {total_output}")
print(f"Saved average ETH chart to {avg_output}")
print(f"Saved largest transaction chart to {max_output}")
