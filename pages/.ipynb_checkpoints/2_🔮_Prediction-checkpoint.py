import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Prediction", page_icon="🔮")

# -----------------------------
# Load Model and Data
# -----------------------------
@st.cache_resource
def load_model():
    with open("model/model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

@st.cache_data
def load_data():
    return pd.read_csv("data/data.csv")

data = load_data()

# -----------------------------
# Page Title
# -----------------------------
st.title("🔮 House Price Prediction")
st.write("Enter house details below to predict the price.")

# -----------------------------
# User Input Form
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
    floors = st.number_input("Floors", min_value=1, max_value=3, value=1)

with col2:
    sqft_living = st.number_input("Living Area (sqft)", min_value=300, max_value=10000, value=2000)
    yr_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2000)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):
    features = np.array([[bedrooms, bathrooms, sqft_living, floors, yr_built]])
    predicted_price = model.predict(features)[0]

    st.success(f"🏠 **Predicted House Price: ${predicted_price:,.2f}**")

    # -------------------------
    # Show 3 Similar Houses
    # -------------------------
    st.subheader("Similar Houses from Dataset:")
    similar_houses = data[
        (data['bedrooms'] == bedrooms) &
        (data['bathrooms'].round() == round(bathrooms))
    ].sort_values(by="price", ascending=True).head(3)

    if not similar_houses.empty:
        st.table(similar_houses[['city', 'price', 'bedrooms', 'bathrooms', 'sqft_living']])
    else:
        st.write("No similar houses found in dataset.")
