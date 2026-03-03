def sequence_model(df):

    df = df.sort_values("account_id")

    df["amount_shift"] = df.groupby("account_id")["amount"].diff().fillna(0)
    df["volatility"] = abs(df["amount_shift"]) / (df["amount"] + 1)

    df["sequence_risk"] = df["volatility"].rolling(5).mean().fillna(0)
    df["sequence_conf"] = 0.8

    return df
