import streamlit as st
import json

st.title("🚀 Trading Bot Dashboard")

# Load data
try:
    with open("trades.json") as f:
        trades = json.load(f)
except:
    trades = []

try:
    with open("signals.json") as f:
        signals = json.load(f)
except:
    signals = []

# -----------------------
st.subheader("📊 Signals")
st.write(signals)

# -----------------------
st.subheader("💼 Trades")
st.write(trades)

# -----------------------
st.subheader("💰 Summary")

capital = sum(t.get("shares", 0) * t.get("entry_price", 0) for t in trades)
st.metric("Invested Capital", f"₹{round(capital,2)}")
