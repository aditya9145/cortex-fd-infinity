import uuid
from config import HIGH_RISK_PERCENTILE

def generate_alerts(df):

    threshold = df["final_risk"].quantile(HIGH_RISK_PERCENTILE)

    alerts = []

    for _, row in df.iterrows():
        if row["final_risk"] >= threshold:
            alerts.append({
                "case_id": str(uuid.uuid4())[:8],
                "account": row["account_id"],
                "risk": row["final_risk"],
                "fraud_type": row["fraud_type"],
                "action": "STEP-UP AUTH"
            })

    return alerts
