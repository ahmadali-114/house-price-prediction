import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Explorer", page_icon="📊")

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
st.title("📊 Data Explorer")
st.write("Use filters below to explore the house price dataset interactively.")

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Options")

# City Filter
cities = st.sidebar.multiselect("Select City:", options=data['city'].unique(), default=data['city'].unique())

# Price Range Filter
min_price = int(data['price'].min())
max_price = int(data['price'].max())
price_range = st.sidebar.slider("Select Price Range:", min_price, max_price, (min_price, max_price))

# Bedroom Filter
bedrooms = st.sidebar.multiselect("Select Bedrooms:", options=sorted(data['bedrooms'].unique()), default=sorted(data['bedrooms'].unique()))

# Apply Filters
filtered_data = data[
    (data['city'].isin(cities)) &
    (data['price'] >= price_range[0]) &
    (data['price'] <= price_range[1]) &
    (data['bedrooms'].isin(bedrooms))
]

st.subheader("Filtered Dataset")
st.write(f"Showing **{len(filtered_data)}** records after applying filters.")
st.dataframe(filtered_data.head(20))

# -----------------------------
# Plotly Visualizations
# -----------------------------
st.subheader("Price Distribution")
fig = px.histogram(filtered_data, x="price", nbins=30, title="Price Distribution")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Price vs. Square Footage")
fig2 = px.scatter(filtered_data, x="sqft_living", y="price", color="bedrooms",
                  title="Price vs. Living Area", hover_data=["city"])
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Average Price by City")
avg_price = filtered_data.groupby("city")["price"].mean().reset_index()
fig3 = px.bar(avg_price, x="city", y="price", title="Average House Price by City", color="price")
st.plotly_chart(fig3, use_container_width=True)
