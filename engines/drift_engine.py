from config import DRIFT_WINDOW

def drift_model(df):

    baseline = df["amount"].mean()
    current = df["amount"].tail(DRIFT_WINDOW).mean()

    drift = abs(current - baseline) / (baseline + 1)

    df["drift_penalty"] = drift
    df["drift_conf"] = 0.7

    return df
