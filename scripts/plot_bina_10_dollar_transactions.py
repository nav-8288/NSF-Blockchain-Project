import pandas as pd
import matplotlib.pyplot as plt

input_file = "data/bina_wallet_likely_10_dollar_transactions.csv"
output_file = "data/bina_wallet_likely_10_dollar_transactions_by_date.png"

df = pd.read_csv(input_file)

df["datetime"] = pd.to_datetime(df["datetime"])
df["date"] = df["datetime"].dt.date

daily_counts = df.groupby("date").size().reset_index(name="transaction_count")

plt.figure(figsize=(10, 6))
plt.bar(daily_counts["date"].astype(str), daily_counts["transaction_count"])
plt.xlabel("Date")
plt.ylabel("Number of Transactions")
plt.title("Bina Wallet Likely $10 Transactions by Date")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(output_file, dpi=300)

print(f"Saved graph to {output_file}")
