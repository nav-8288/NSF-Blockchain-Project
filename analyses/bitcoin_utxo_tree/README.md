# Bitcoin UTXO Transaction Tree Analysis

## Goal

This analysis is part of the Week 5 blockchain analysis tasks.

The goal was to look at Bitcoin transaction tracing using the UTXO model. This was different from the Ethereum tasks because Ethereum is account-based, while Bitcoin tracks value through transaction outputs.

For this task, I first tested the Bitcoin genesis transaction since the meeting notes mentioned starting from Satoshi Nakamoto's genesis transaction. After that, I used an early spendable Bitcoin transaction to build a practical UTXO transaction path.

## Background

Bitcoin does not track balances the same way Ethereum does.

In Ethereum, it is more natural to look at an address and review the transactions going in and out of that account. In Bitcoin, transactions spend previous outputs and create new outputs. Those outputs can later become inputs to future transactions.

Because of that, tracing Bitcoin activity means following transaction outputs as they are spent in later transactions.

## Genesis Transaction Test

The first transaction I tested was the Bitcoin genesis coinbase transaction:

`4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b`

The script checked the output from the genesis transaction and found:

| Metric | Result |
|---|---:|
| Genesis outputs checked | 1 |
| Genesis spent outputs | 0 |
| Genesis output value | 50 BTC |

The genesis transaction did not produce a normal forward spend path in this trace. I kept this as a finding instead of trying to force the trace to continue.

Because of that, I used a later spendable transaction to demonstrate the actual UTXO tree tracing.

## Practical UTXO Trace

For the practical tracing example, I used the early Bitcoin transaction:

`f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16`

The script followed spent outputs forward through later transactions. I traced up to 8 levels, which is more than the original 4-5 hop goal from the meeting notes.

## Summary Results

| Metric | Result |
|---|---:|
| Demo trace rows | 12 |
| Unique source transactions traced | 8 |
| Maximum hop reached | 7 |
| Spent outputs followed | 11 |

Since the hop count starts at 0, reaching hop 7 means the trace covered 8 levels.

## Method

I used a Python script to:

* look up a Bitcoin transaction
* check each transaction output
* determine whether each output was spent
* find the transaction that spent the output
* follow one forward path through spent outputs
* save the trace results to a CSV
* create a directed graph showing the UTXO path

The graph shows transaction IDs as nodes and arrows showing how outputs were spent into later transactions.

The graph is intentionally simple so it stays readable. The exact output indexes, BTC values, and spent-by transaction IDs are saved in the CSV files.

## Main Finding

The genesis transaction test ended immediately because the genesis coinbase output did not have a normal forward spend path.

The practical example showed how Bitcoin UTXO tracing works. Instead of following an account balance like in Ethereum, the script follows outputs from one transaction into later transactions.

The final trace reached 8 levels and produced a visual path showing how Bitcoin outputs can move through later transactions.

## Files Created

* `data/bitcoin_genesis_utxo_test.csv`
  * CSV output from testing the genesis transaction.

* `data/bitcoin_utxo_tree_trace.csv`
  * CSV output from the practical UTXO trace.

* `analyses/bitcoin_utxo_tree/bitcoin_genesis_utxo_test.png`
  * Graph showing the genesis transaction test.

* `analyses/bitcoin_utxo_tree/bitcoin_utxo_tree.png`
  * Graph showing the practical Bitcoin UTXO transaction tree.

## Limitations

This is not a full Bitcoin transaction graph.

The script follows a forward path and keeps the graph readable. Some Bitcoin transactions have multiple outputs, and a deeper version could branch out and follow every spent output.

This analysis also does not identify the real-world owners of the transactions. It only traces transaction-output relationships.

## Next Step

A stronger version of this analysis would trace multiple branches instead of only following one path. Another improvement would be labeling transaction types or addresses if reliable public labels are available.
