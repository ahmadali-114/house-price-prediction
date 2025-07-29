
# 🏠 House Price Prediction Web App

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-brightgreen)](https://ahmadali-114-house-price-prediction-app-chccdi.streamlit.app/)

This project is a **House Price Prediction Web Application** built using **Python, Streamlit, and Machine Learning**.  
The app allows users to explore housing data, visualize price trends, and predict house prices based on input features.

---

## 🚀 **Live Demo**
Access the live app here:  
**[https://ahmadali-114-house-price-prediction-app-chccdi.streamlit.app/](https://ahmadali-114-house-price-prediction-app-chccdi.streamlit.app/)**

---

## 📌 **Features**
- **Dashboard Homepage**  
  Displays key statistics (total houses, average price, highest & lowest price) with a modern UI.

- **Data Explorer Page**  
  Filter dataset by city, price range, and bedrooms. View interactive **Plotly** visualizations.

- **Prediction Page**  
  Input custom house details (bedrooms, bathrooms, sqft, etc.) and get a **predicted price** instantly.

- **Trends & Insights Page**  
  Visualize **price distributions**, **correlation heatmaps**, and **average price by city**.

---

## 🛠 **Tech Stack**
- **Python 3**
- **Streamlit**
- **Pandas, NumPy**
- **Scikit-learn**
- **Plotly (for interactive visualizations)**

---

## 📂 **Project Structure**
```
house-price-prediction/
│
├── app.py                     # Main dashboard homepage
├── pages/                     # Streamlit multi-page structure
│   ├── 1_📊_Data_Explorer.py
│   ├── 2_🔮_Prediction.py
│   └── 3_📈_Trends.py
├── model/
│   └── model.pkl              # Trained Linear Regression model
├── data/
│   └── data.csv               # Dataset used for predictions
└── requirements.txt           # Required Python packages
```

---

## 💻 **How to Run Locally**
1. **Clone the repository**  
   ```bash
   git clone https://github.com/ahmadali-114/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```

---

## 📸 **Screenshots**
- **Homepage Dashboard**  
  ![Homepage Screenshot](screenshots/homepage.png)

- **Prediction Page**  
  ![Prediction Screenshot](screenshots/prediction.png)

- **Trends & Insights**  
  ![Trends Screenshot](screenshots/trends.png)

---

## 🔮 **Future Improvements**
- Add **advanced ML models** (Random Forest, XGBoost).
- Improve **feature engineering** (e.g., age of house, location clustering).
- Deploy on a **custom domain**.

---

## 👤 **Author**
**Ahmad Ali**  
- [GitHub](https://github.com/ahmadali-114)
- [LinkedIn](https://www.linkedin.com/) *(Add your LinkedIn link)*

