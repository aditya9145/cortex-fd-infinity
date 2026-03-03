import pandas as pd
import numpy as np

def risk_band(score):
    if score >= 0.85:
        return "CRITICAL"
    elif score >= 0.70:
        return "HIGH"
    elif score >= 0.50:
        return "MEDIUM"
    else:
        return "LOW"

def action_map(band):
    if band == "CRITICAL":
        return "AUTO_FREEZE + LEVEL_3_ESCALATION"
    elif band == "HIGH":
        return "STEP_UP_AUTH + FRAUD_REVIEW_QUEUE"
    elif band == "MEDIUM":
        return "REALTIME_MONITORING"
    else:
        return "NO_ACTION"

def compliance_tag(row):
    tags = []

    if row.get("drift_score",0) > 0.7:
        tags.append("MODEL_DRIFT")

    if row.get("graph_risk",0) > 0.8:
        tags.append("NETWORK_EXPOSURE")

    if row.get("momentum_score",0) > 0.75:
        tags.append("RISK_ACCELERATION")

    if row.get("stability_score",1) < 0.3:
        tags.append("BEHAVIOURAL_INSTABILITY")

    if not tags:
        tags.append("STANDARD_MONITORING")

    return "|".join(tags)

def generate_alerts(df):

    df["risk_band"] = df["final_risk"].apply(risk_band)
    df["recommended_action"] = df["risk_band"].apply(action_map)
    df["compliance_tag"] = df.apply(compliance_tag, axis=1)

    alerts = df[df["risk_band"].isin(["CRITICAL","HIGH"])][
        ["user_id","final_risk","risk_band","recommended_action","compliance_tag"]
    ].sort_values("final_risk", ascending=False)

    return alerts.head(50)
