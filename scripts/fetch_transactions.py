import requests
import pandas as pd
import os
from datetime import datetime ##Formats time of transaction

from dotenv import load_dotenv

#SAME ETHERSCAN API IDEA AS getInteraction function from Tejas's code, BUT CHANGING WHAT DATA WE KEEP FROM API RESPONSE #
#What transactions happened, how much ETH moved, who sent it, who received it, and when? COLLECTING FULL TRANSACTION DATA #


def fetch_transactions(contract_address,api_key,chainID,output_file="transactions_clean.csv"):


    ##Same Etherscan API request structure from getInteraction.py
    ##still using the "txlist" action since it returns normal transactions for wallet/sc address

    api_endpoint = (
        f"https://api.etherscan.io/v2/api"
        f"?chainid={chainID}"
        f"&module=account"
        f"&action=txlist"
        f"&address={contract_address}"
        f"&startblock=0"
        f"&endblock=99999999"
        f"&page=1"
        f"&offset=10000"
        f"&sort=asc"
        f"&apikey={api_key}"
    )

    ##send a request to Etherscan
    response = requests.get(api_endpoint)

    #convert the response into py list data
    data = response.json()

    #check if Etherscan returned an error instead of transaction data
    if data["status"] != "1":
        print("Etherscan returned an error:")
        print(data["message"])
        print(data["result"])
        return None

    ##This list will store full tx's rows. Using lst since every tx will be stored
    transactions = []

    ##iterate through every "item" or "transaction" in the data returned by Etherscan 
    for item in data["result"]:

        #Etherscan gives tx value in Wei
        #Wei is samllest unit of ETH, 1.0 ETH = 10^18 Wei

        val_wei = int(item["value"])
        val_eth = val_wei / 10**18

        ##Etherscan gives timestamp as Unix format, datetime converts into readable format
        timestamp = datetime.fromtimestamp(int(item["timeStamp"]))

        #This stores the full transaction details. 
        transactions.append({
            "tx_hash": item["hash"],
            "block_number": item["blockNumber"],
            "timestamp": timestamp,
            "month": timestamp.strftime("%Y-%m"),
            "from_address": item["from"],
            "to_address": item["to"],
            "value_wei": val_wei,
            "value_eth": val_eth,
            "gas": item["gas"],
            "gas_price": item["gasPrice"],
            "input": item["input"],

            ##if the input is just "0x", usually means a normal ETH transfer
            ##if input has more data, its a SC interaction

            "is_contract_interaction": item["input"] != "0x"
        })

    ##convert the list of tx dicts into pandas DataFrame
    df = pd.DataFrame(transactions)

    ##make a cleaner version of input so CSV is easier to read
    df["input_preview"] = df["input"].str[:20]

    ##convert gas price from wei to Gwei; easier to understand
    df["gas_price_gwei"] = df["gas_price"].astype(float)/ 10**9

    ##save cleaner tx data for easier viewing

    clean_df = df[[
        "tx_hash",
        "block_number",
        "timestamp",
        "month",
        "from_address",
        "to_address",
        "value_eth",
        "gas",
        "gas_price_gwei",
        "input_preview",
        "is_contract_interaction"
    ]]

    ##save tx data to a CSV file; gives something simple to inspect before postgres
    clean_df.to_csv(output_file, index=False)

    print(f"Tx's have been saved to {output_file}")

    ##Quick first analysis step; Sort tx's by ETH value and prints top 10 high value tx's
    top_txs = clean_df.sort_values("value_eth", ascending=False).head(10)

    print("\nTop 10 transactions by ETH value:")
    print(top_txs[["timestamp", "from_address", "to_address", "value_eth"]])

    return clean_df
    

if __name__ == "__main__":
    #Replace with wallet or contrad address to test 
    address = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe" #ETH foundation address

    load_dotenv()

    api_key = os.getenv("ETHERSCAN_API_KEY")

    chainID = 1 #Ethereum Mainnet

    fetch_transactions(address,api_key,chainID)