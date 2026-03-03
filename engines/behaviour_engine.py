from sklearn.ensemble import IsolationForest

def behaviour_model(df):

    features = df[[
        "amount_zscore",
        "geo_velocity",
        "device_entropy",
        "burst_index"
    ]]

    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(features)

    df["behaviour_risk"] = -model.decision_function(features)
    df["behaviour_conf"] = 0.9

    return df
