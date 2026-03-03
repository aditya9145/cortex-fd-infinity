def fuse_risk(df):

    risk_components = [
        ("behaviour_risk","behaviour_conf"),
        ("sequence_risk","sequence_conf"),
        ("graph_risk","graph_conf"),
        ("posterior_fraud_prob","posterior_conf"),
        ("risk_momentum","momentum_conf"),
        ("propagation_risk","propagation_conf")
    ]

    numerator = 0
    denominator = 0

    for r,c in risk_components:
        numerator += df[r] * df[c] * df["stability_factor"]
        denominator += df[c]

    df["final_risk"] = numerator / denominator

    return df
