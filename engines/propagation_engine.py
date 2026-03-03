import networkx as nx
import random
import pandas as pd

def propagation_risk(df):

    G = nx.Graph()
    accounts = df["account_id"].unique()

    for acc in accounts:
        G.add_node(acc)

    for _ in range(len(accounts)//2):
        a = random.choice(accounts)
        b = random.choice(accounts)
        if a != b:
            G.add_edge(a, b)

    propagation_score = {}

    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        neighbor_risk = df[df["account_id"].isin(neighbors)]["posterior_fraud_prob"].mean()
        propagation_score[node] = neighbor_risk if not pd.isna(neighbor_risk) else 0

    df["propagation_risk"] = df["account_id"].map(propagation_score)
    df["propagation_conf"] = 0.75

    return df
