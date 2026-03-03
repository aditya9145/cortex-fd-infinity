import networkx as nx
import random

def graph_model(df):

    G = nx.Graph()
    accounts = df["account_id"].unique()

    for acc in accounts:
        G.add_node(acc)

    for _ in range(len(accounts)//2):
        a = random.choice(accounts)
        b = random.choice(accounts)
        if a != b:
            G.add_edge(a, b)

    centrality = nx.pagerank(G)

    df["graph_risk"] = df["account_id"].apply(
        lambda x: centrality.get(x, 0)
    )

    df["graph_conf"] = 0.75

    return df
