import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Sales Prediction Dashboard",
    page_icon="📈",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #0f172a
    );
}

.card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.15);
    text-align:center;
}

.big-title{
    font-size:42px;
    font-weight:bold;
    text-align:center;
    color:white;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:25px;
}

.metric-value{
    font-size:28px;
    font-weight:bold;
    color:#38bdf8;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# LOAD DATA
# ----------------------------

df = pd.read_csv("Advertising.csv")

if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

# ----------------------------
# LOAD MODEL
# ----------------------------

with open("sales_model.pkl", "rb") as f:
    model = pickle.load(f)

# ----------------------------
# HEADER
# ----------------------------

st.markdown(
    '<div class="big-title">📈 Sales Prediction Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Advertising Budget Analytics & Sales Forecasting</div>',
    unsafe_allow_html=True
)

st.divider()

# ----------------------------
# SIDEBAR
# ----------------------------

st.sidebar.title("🎯 Advertising Budget")

tv = st.sidebar.slider(
    "TV Budget",
    0.0,
    300.0,
    150.0
)

radio = st.sidebar.slider(
    "Radio Budget",
    0.0,
    50.0,
    25.0
)

newspaper = st.sidebar.slider(
    "Newspaper Budget",
    0.0,
    120.0,
    30.0
)

# ----------------------------
# PREDICTION
# ----------------------------

prediction = model.predict(
    [[tv, radio, newspaper]]
)[0]

# ----------------------------
# KPI CARDS
# ----------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class='card'>
        <h4>Predicted Sales</h4>
        <div class='metric-value'>{prediction:.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class='card'>
        <h4>TV Budget</h4>
        <div class='metric-value'>{tv}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class='card'>
        <h4>Radio Budget</h4>
        <div class='metric-value'>{radio}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class='card'>
        <h4>Newspaper Budget</h4>
        <div class='metric-value'>{newspaper}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------
# GAUGE CHART
# ----------------------------

gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=float(prediction),
    title={'text': "Predicted Sales"},
    gauge={
        'axis': {'range': [0, 35]}
    }
))

st.plotly_chart(
    gauge,
    use_container_width=True
)

# ----------------------------
# HEATMAP
# ----------------------------

st.subheader("📊 Correlation Analysis")

corr = df.corr()

heatmap = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Feature Correlation Heatmap"
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)

# ----------------------------
# SCATTER PLOTS
# ----------------------------

st.subheader("📈 Advertising Impact")

col1, col2 = st.columns(2)

with col1:

    fig1 = px.scatter(
        df,
        x="TV",
        y="Sales",
        trendline="ols",
        title="TV vs Sales"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = px.scatter(
        df,
        x="Radio",
        y="Sales",
        trendline="ols",
        title="Radio vs Sales"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

fig3 = px.scatter(
    df,
    x="Newspaper",
    y="Sales",
    trendline="ols",
    title="Newspaper vs Sales"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ----------------------------
# INSIGHTS
# ----------------------------

st.subheader("💡 Business Insights")

best_channel = df.corr()["Sales"].drop("Sales").idxmax()

st.info(
    f"""
    Best Performing Advertising Channel: {best_channel}

    Increasing investment in {best_channel}
    generally has the strongest impact on sales.

    Current Predicted Sales:
    {prediction:.2f}
    """
)

# ----------------------------
# FOOTER
# ----------------------------

st.markdown("---")

st.caption(
    "Machine Learning Sales Prediction Dashboard | Linear Regression Model"
)