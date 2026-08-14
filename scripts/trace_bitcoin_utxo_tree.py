import requests
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path

BASE_URL = "https://blockstream.info/api"

# Bitcoin genesis coinbase transaction
GENESIS_TXID = "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"

# Early spendable Bitcoin transaction used for the practical UTXO trace
DEMO_TXID = "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
ANALYSIS_DIR = PROJECT_ROOT / "analyses" / "bitcoin_utxo_tree"

DATA_DIR.mkdir(exist_ok=True)
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)


def get_tx(txid):
    response = requests.get(f"{BASE_URL}/tx/{txid}", timeout=20)
    response.raise_for_status()
    return response.json()


def get_outspend(txid, output_index):
    response = requests.get(f"{BASE_URL}/tx/{txid}/outspend/{output_index}", timeout=20)
    response.raise_for_status()
    return response.json()


def short_txid(txid):
    return txid[:8] + "..." + txid[-8:]


def trace_first_spent_path(start_txid, max_hops=8):
    """
    Follows a simple forward UTXO path.

    For each transaction, the script checks all outputs and records them.
    If one or more outputs are spent, the script follows the first spent
    output as the next hop.
    """
    rows = []
    current_txid = start_txid
    visited = set()

    for hop in range(max_hops):
        if current_txid in visited:
            print(f"Stopping because this transaction was already visited: {current_txid}")
            break

        visited.add(current_txid)

        source_txid = current_txid
        tx = get_tx(source_txid)
        outputs = tx.get("vout", [])

        next_txid = None

        for output_index, output in enumerate(outputs):
            value_btc = output.get("value", 0) / 100_000_000
            outspend = get_outspend(source_txid, output_index)

            spent = outspend.get("spent", False)
            spent_by_txid = outspend.get("txid", "")

            rows.append({
                "hop": hop,
                "txid": source_txid,
                "output_index": output_index,
                "output_value_btc": value_btc,
                "spent": spent,
                "spent_by_txid": spent_by_txid
            })

            # Follow the first spent output as the next transaction in the path.
            if spent and next_txid is None:
                next_txid = spent_by_txid

        if next_txid is None:
            break

        current_txid = next_txid

    return pd.DataFrame(rows)


def make_hop_layout_graph(df, output_file, title):
    """
    Creates a cleaner UTXO graph by arranging transactions by hop number.

    Node label format:
    H0
    f4184fc5...831e9e16
    """
    graph = nx.DiGraph()
    node_hops = {}

    for _, row in df.iterrows():
        source_txid = row["txid"]
        hop = int(row["hop"])

        graph.add_node(source_txid)

        if source_txid not in node_hops:
            node_hops[source_txid] = hop
        else:
            node_hops[source_txid] = min(node_hops[source_txid], hop)

        target_txid = row["spent_by_txid"]

        if row["spent"] and isinstance(target_txid, str) and target_txid.strip() != "":
            graph.add_node(target_txid)
            graph.add_edge(source_txid, target_txid)

            if target_txid not in node_hops:
                node_hops[target_txid] = hop + 1

    # Group nodes by hop level
    levels = {}
    for node, hop in node_hops.items():
        levels.setdefault(hop, []).append(node)

    # Create manual left-to-right positions by hop
    pos = {}
    x_spacing = 4.8
    y_spacing = 3.0

    for hop, nodes in sorted(levels.items()):
        count = len(nodes)
        start_y = (count - 1) * y_spacing / 2

        for index, node in enumerate(nodes):
            x = hop * x_spacing
            y = start_y - index * y_spacing
            pos[node] = (x, y)

    labels = {
        node: f"H{node_hops.get(node, '?')}\n{short_txid(node)}"
        for node in graph.nodes()
    }

    plt.figure(figsize=(22, 11))

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=3600,
        edgecolors="black",
        linewidths=1.2
    )

    nx.draw_networkx_edges(
        graph,
        pos,
        arrows=True,
        arrowstyle="-|>",
        arrowsize=22,
        width=1.6,
        connectionstyle="arc3,rad=0.04"
    )

    nx.draw_networkx_labels(
        graph,
        pos,
        labels=labels,
        font_size=8,
        font_weight="bold",
        bbox=dict(
            facecolor="white",
            edgecolor="none",
            alpha=0.75,
            pad=0.25
        )
    )

    plt.title(title, fontsize=20)
    plt.axis("off")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()


print("Testing Bitcoin genesis transaction...")
print("--------------------------------------")

genesis_df = trace_first_spent_path(GENESIS_TXID, max_hops=8)

genesis_csv = DATA_DIR / "bitcoin_genesis_utxo_test.csv"
genesis_graph = ANALYSIS_DIR / "bitcoin_genesis_utxo_test.png"

genesis_df.to_csv(genesis_csv, index=False)
make_hop_layout_graph(
    genesis_df,
    genesis_graph,
    "Bitcoin Genesis Transaction UTXO Test"
)

print(genesis_df.to_string(index=False))
print()
print(f"Saved genesis CSV to {genesis_csv}")
print(f"Saved genesis graph to {genesis_graph}")


print()
print("Tracing early spendable Bitcoin transaction path...")
print("--------------------------------------------------")

demo_df = trace_first_spent_path(DEMO_TXID, max_hops=8)

demo_csv = DATA_DIR / "bitcoin_utxo_tree_trace.csv"
demo_graph = ANALYSIS_DIR / "bitcoin_utxo_tree.png"

demo_df.to_csv(demo_csv, index=False)
make_hop_layout_graph(
    demo_df,
    demo_graph,
    "Bitcoin UTXO Transaction Tree"
)

print(demo_df.to_string(index=False))
print()
print(f"Saved demo CSV to {demo_csv}")
print(f"Saved demo graph to {demo_graph}")


print()
print("Summary")
print("-------")
print(f"Genesis outputs checked: {len(genesis_df)}")
print(f"Genesis spent outputs: {genesis_df['spent'].sum()}")

if len(demo_df) > 0:
    print(f"Demo trace rows: {len(demo_df)}")
    print(f"Demo unique source transactions traced: {demo_df['txid'].nunique()}")
    print(f"Demo max hop reached: {demo_df['hop'].max()}")
    print(f"Demo spent outputs followed: {demo_df['spent'].sum()}")
else:
    print("Demo trace did not return any rows.")
