import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ETHERSCAN_API_KEY")
ADDRESS = "0x3e6937bb87A66E3A4DbE5488A4863f5b29674cC3"

url = "https://api.etherscan.io/v2/api"

params = {
    "chainid": "1",
    "module": "account",
    "action": "txlist",
    "address": ADDRESS,
    "startblock": 0,
    "endblock": 99999999,
    "page": 1,
    "offset": 10000,
    "sort": "asc",
    "apikey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

if data.get("status") != "1":
    print("Etherscan returned an issue:")
    print(data)
    exit()

txs = data["result"]

df = pd.DataFrame(txs)

df["datetime"] = pd.to_datetime(df["timeStamp"], unit="s")
df["value_eth"] = pd.to_numeric(df["value"]) / 10**18

# Keep useful columns
cols = [
    "hash",
    "datetime",
    "from",
    "to",
    "value_eth",
    "gas",
    "gasPrice",
    "isError",
    "txreceipt_status",
    "input"
]

df = df[cols]

# Outgoing ETH transactions only
outgoing = df[
    (df["from"].str.lower() == ADDRESS.lower()) &
    (df["value_eth"] > 0)
].copy()

output_file = "data/bina_wallet_outgoing_eth_transactions.csv"
outgoing.to_csv(output_file, index=False)

print(f"Saved {len(outgoing)} outgoing ETH transactions to {output_file}")
print(outgoing[["datetime", "to", "value_eth", "hash"]].head(20))
