import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="House Price Dashboard", page_icon="🏠", layout="wide")

# -----------------------------
# Custom CSS for Cards
# -----------------------------
st.markdown("""
    <style>
    body, .block-container {
        background-color: #f4f6f9 !important;
        font-family: "Segoe UI", Roboto, Arial, sans-serif !important;
    }

    .card {
        padding: 20px;
        border-radius: 10px;
        background: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .card-title {
        font-size: 18px;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .card-value {
        font-size: 24px;
        color: #2980b9;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/data.csv")

data = load_data()

# -----------------------------
# Title
# -----------------------------
st.title("🏠 House Price Prediction Dashboard")
st.markdown("Welcome to the **House Price Prediction Web App**!")

# -----------------------------
# Key Stats
# -----------------------------
total_houses = len(data)
avg_price = data['price'].mean()
max_price = data['price'].max()
min_price = data['price'].min()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div class='card'><div class='card-title'>Total Houses</div><div class='card-value'>{total_houses}</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='card'><div class='card-title'>Average Price</div><div class='card-value'>${avg_price:,.0f}</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='card'><div class='card-title'>Most Expensive</div><div class='card-value'>${max_price:,.0f}</div></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='card'><div class='card-title'>Cheapest</div><div class='card-value'>${min_price:,.0f}</div></div>", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# Trend Preview Chart
# -----------------------------
st.subheader("📈 Average Price by City (Preview)")
avg_price_city = data.groupby("city")["price"].mean().reset_index().sort_values(by="price", ascending=False)
fig = px.bar(avg_price_city, x="city", y="price", color="price", title="Average House Price by City")
st.plotly_chart(fig, use_container_width=True, key="avg_price_city_chart")

# -----------------------------
# Go to Prediction Button
# -----------------------------
if st.button("🔮 Go to Price Prediction"):
    st.switch_page("pages/2_🔮_Prediction.py")
