def risk_momentum(df):

    df = df.sort_values("account_id")

    df["risk_delta"] = df.groupby("account_id")["posterior_fraud_prob"].diff().fillna(0)
    df["risk_momentum"] = df["risk_delta"].rolling(5).mean().fillna(0)

    df["momentum_conf"] = 0.8

    return df
