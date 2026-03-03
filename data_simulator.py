import pandas as pd
import numpy as np
import random

def generate_data(n=5000):

    rows = []

    for _ in range(n):
        account = random.randint(10000, 10300)
        amount = np.random.lognormal(8, 1)
        hour = random.randint(0, 23)
        geo_velocity = abs(np.random.normal(1, 0.8))
        device_entropy = np.random.uniform(0, 1)
        tx_gap = abs(np.random.normal(30, 10))

        rows.append([
            account,
            amount,
            hour,
            geo_velocity,
            device_entropy,
            tx_gap
        ])

    cols = [
        "account_id","amount","hour",
        "geo_velocity","device_entropy","tx_gap"
    ]

    return pd.DataFrame(rows, columns=cols)
