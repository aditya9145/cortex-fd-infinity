def stability_index(df):

    volatility = df["posterior_fraud_prob"].std()
    stability = 1 / (1 + volatility)

    df["stability_factor"] = stability

    return df
