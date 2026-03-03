def create_features(df):

    df["amount_zscore"] = (
        (df["amount"] - df["amount"].mean()) /
        (df["amount"].std() + 1)
    )

    df["night_flag"] = df["hour"].apply(lambda x: 1 if x < 5 else 0)
    df["burst_index"] = 1 / (df["tx_gap"] + 1)

    return df
