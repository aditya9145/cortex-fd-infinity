from config import BASE_FRAUD_PRIOR

def bayesian_update(df):

    df["posterior_fraud_prob"] = (
        BASE_FRAUD_PRIOR +
        df["behaviour_risk"] * 0.3 +
        df["sequence_risk"] * 0.2 +
        df["graph_risk"] * 0.2
    )

    df["posterior_conf"] = 0.85

    return df
