
def generate_alerts(df):

    df["risk_band"] = df["final_risk"].apply(risk_band)
    df["recommended_action"] = df["risk_band"].apply(action_map)
    df["compliance_tag"] = df.apply(compliance_tag, axis=1)

    required_cols = []

    if "user_id" in df.columns:
        required_cols.append("user_id")

    if "final_risk" in df.columns:
        required_cols.append("final_risk")

    required_cols += ["risk_band", "recommended_action", "compliance_tag"]

    alerts = df[df["risk_band"].isin(["CRITICAL","HIGH"])]

    alerts = alerts[required_cols].sort_values(
        "final_risk",
        ascending=False
    )

    return alerts.head(50)
