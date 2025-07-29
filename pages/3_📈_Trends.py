import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(page_title="Trends & Insights", page_icon="📈")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/data.csv")

data = load_data()

# -----------------------------
# Page Title
# -----------------------------
st.title("📈 Trends & Insights")
st.write("Discover house price trends, correlations, and top expensive houses.")

# -----------------------------
# 1. Top Expensive Houses
# -----------------------------
st.subheader("🏆 Top 5 Most Expensive Houses")
top_houses = data.sort_values(by="price", ascending=False).head(5)
st.table(top_houses[['city', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'yr_built']])

# -----------------------------
# 2. Average Price by City
# -----------------------------
st.subheader("📊 Average Price by City")
avg_price_city = data.groupby("city")["price"].mean().reset_index().sort_values(by="price", ascending=False)
fig = px.bar(avg_price_city, x="city", y="price", title="Average House Price by City", color="price")
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 3. Correlation Heatmap
# -----------------------------
st.subheader("🔗 Feature Correlation")
numeric_cols = data.select_dtypes(include=['int64', 'float64'])
corr = numeric_cols.corr()

fig2 = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    annotation_text=corr.round(2).values,
    colorscale='Viridis',
    showscale=True
)
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# 4. Price Trends Over Year Built
# -----------------------------
if "yr_built" in data.columns:
    st.subheader("📅 Price Trend by Year Built")
    yearly_avg = data.groupby("yr_built")["price"].mean().reset_index()
    fig3 = px.line(yearly_avg, x="yr_built", y="price", title="Average Price by Year Built")
    st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# 5. Sqft vs Price Bubble Chart
# -----------------------------
st.subheader("💡 Living Area vs Price")
fig4 = px.scatter(
    data, x="sqft_living", y="price", size="bedrooms", color="city",
    hover_name="city", title="Price vs Living Area (Bubble Chart)"
)
st.plotly_chart(fig4, use_container_width=True)
