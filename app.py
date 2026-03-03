import streamlit as st
from data_simulator import generate_data
from engines.feature_engine import create_features
from engines.behaviour_engine import behaviour_model
from engines.sequence_engine import sequence_model
from engines.graph_engine import graph_model
from engines.drift_engine import drift_model
from engines.bayesian_engine import bayesian_update
from engines.momentum_engine import risk_momentum
from engines.propagation_engine import propagation_risk
from engines.stability_engine import stability_index
from engines.fusion_engine import fuse_risk
from engines.archetype_engine import fraud_archetype
from governance.alert_engine import generate_alerts

st.title("CORTEX-FD ∞ Enterprise Fraud Intelligence OS")

if st.button("Run Full Intelligence Stack"):

    df = generate_data(4000)

    df = create_features(df)
    df = behaviour_model(df)
    df = sequence_model(df)
    df = graph_model(df)
    df = drift_model(df)
    df = bayesian_update(df)
    df = risk_momentum(df)
    df = propagation_risk(df)
    df = stability_index(df)
    df = fuse_risk(df)
    df = fraud_archetype(df)

    alerts = generate_alerts(df)

    st.subheader("Top Risk Transactions")
    st.dataframe(df.sort_values("final_risk",ascending=False).head(20))

    st.subheader("Fraud Type Distribution")
    st.bar_chart(df["fraud_type"].value_counts())

    st.subheader("Generated Alerts")
    st.write(alerts)

    st.line_chart(df["final_risk"])
