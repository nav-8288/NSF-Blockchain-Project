# Joe Lubin / MakerDAO-Related ETH Transfer Analysis

## Goal

This analysis looks at the large ETH movement connected to a wallet linked to Joseph Lubin / Consensys.

This was one of the main case-study tasks from the Week 5 meeting. The goal was to check the actual transaction data and see how the reported large ETH movement appears on-chain.

At first, I was looking for one very large transaction, but the data showed that the movement was split across multiple transactions instead.

## Wallet Analyzed

`0x1b3cb81e51011b549d78bf720b0d924ac763a7c2`

This is the Lubin-linked wallet I had already started investigating earlier in the project.

## Dataset Used

I used the local PostgreSQL table:

`lubin_actual_transactions`

This table contains normal Ethereum transactions that were collected from the Etherscan API for the Lubin-linked wallet.

## Method

I queried outgoing ETH transactions from the wallet and filtered for large transfers.

For this version, I used the cutoff:

`value_eth >= 30000`

I used 30,000 ETH as the cutoff because the large movement did not appear as one single transaction. Using this lower cutoff made it possible to catch the separate large transfers that were part of the same overall movement.

The results were exported to a CSV and then used to create a bar chart showing the large outgoing transfers.

## Summary Results

| Metric | Result |
|---|---:|
| Large outgoing transfers found | 8 |
| First large transfer | 2022-04-24 23:36:16 |
| Last large transfer | 2026-06-06 02:06:11 |
| Total ETH moved across large transfers | 426,700 ETH |

## Large Transfers Found

| Timestamp | Receiving Address | ETH Moved |
|---|---|---:|
| 2022-04-24 23:36:16 | `0xabed497d0ccb6916c95dd98ad4402febf5f52fe7` | 54,000 ETH |
| 2022-05-09 16:06:36 | `0x214984f6f8b4197a9a32159ed17b72650331538a` | 96,700 ETH |
| 2022-06-18 15:58:55 | `0x214984f6f8b4197a9a32159ed17b72650331538a` | 62,000 ETH |
| 2023-01-04 08:24:23 | `0x3113b42b97de26116b2957288ea94120d5c3e84b` | 64,000 ETH |
| 2023-02-25 23:42:47 | `0x22de0b5c40f012782a667ccdaa15406ba1201246` | 40,000 ETH |
| 2026-06-06 00:11:35 | `0x22de0b5c40f012782a667ccdaa15406ba1201246` | 40,000 ETH |
| 2026-06-06 00:18:35 | `0xabed497d0ccb6916c95dd98ad4402febf5f52fe7` | 40,000 ETH |
| 2026-06-06 02:06:11 | `0xd44d1be105b5b542b780dc7e122240b93ac21b62` | 30,000 ETH |

## Main Finding

The main thing I found is that the large 2026 movement did not show up as one single transaction.

Instead, on June 6, 2026, the wallet sent three large outgoing ETH transfers:

* 40,000 ETH
* 40,000 ETH
* 30,000 ETH

Together, those three transactions add up to 110,000 ETH.

This helped explain why my earlier Week 2 query only found part of the movement. At that time, I was mainly looking for transfers around 40,000 ETH or higher, so I found the two 40,000 ETH transfers but missed the 30,000 ETH transfer.

Lowering the cutoff to 30,000 ETH gave a more complete picture of the June 6 movement.

## MakerDAO / Maker Vault Connection

In the earlier part of this investigation, I checked the receiving addresses on Etherscan.

One receiving address:

`0x22de0b5c40f012782a667ccdaa15406ba1201246`

appeared connected to Maker Vault activity.

Another receiving address:

`0xabed497d0ccb6916c95dd98ad4402febf5f52fe7`

later sent 40,000 ETH to a DSProxy address.

Because of this, I would describe the movement as MakerDAO / Maker Vault-related instead of saying the receiving addresses are directly owned by MakerDAO.

## Chart Explanation

The chart shows each large outgoing ETH transfer from the Lubin-linked wallet.

The visual makes it easier to see that the wallet had several large transfers over time, but the June 6, 2026 movement was especially important because it was split into three separate transactions that together added up to 110,000 ETH.

## Limitations

This analysis only uses normal Ethereum transactions collected through the Etherscan API.

It does not include:

* internal transactions
* ERC-20 token transfers
* deeper smart contract activity
* a full Maker Vault position analysis
* ETH/USD value at the time of each transfer

Also, Etherscan labels are useful for context, but they should not be treated as perfect proof of ownership.

## Next Step

A stronger version of this analysis would trace the receiving addresses more deeply and look closer at the Maker Vault / DSProxy activity after the ETH was sent.

For this version, the main goal was to verify the large outgoing transfers, explain the split-transfer pattern, and create a clear visual summary.
