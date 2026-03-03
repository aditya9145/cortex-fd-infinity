def fraud_archetype(df):

    df["fraud_type"] = "Normal"

    df.loc[df["geo_velocity"] > 3, "fraud_type"] = "Geo-Switch Fraud"
    df.loc[df["device_entropy"] > 0.8, "fraud_type"] = "Device Takeover Fraud"
    df.loc[df["risk_momentum"] > 0.05, "fraud_type"] = "Rapid Escalation Fraud"
    df.loc[df["propagation_risk"] > 0.5, "fraud_type"] = "Fraud Ring Exposure"

    return df
