import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -----------------------------
# 1. Load Dataset
# -----------------------------
# Change this path if needed (keep CSV in ../data/data.csv relative to this file)
data_path = r"E:\House Price Prediction Model\data\data.csv"  
data = pd.read_csv(data_path)

# -----------------------------
# 2. Basic Preprocessing
# -----------------------------
# Fill missing values with 0 or as per your notebook
data = data.fillna(0)

# Select features (based on your dataset columns)
features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'yr_built']
target = 'price'

X = data[features]
y = data[target]

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 4. Train Linear Regression
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 5. Save the Model
# -----------------------------
model_path = r"E:\House Price Prediction Model\model\model.pkl"
with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model trained successfully and saved at: {model_path}")
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -----------------------------
# 1. Load Dataset
# -----------------------------
# Change this path if needed (keep CSV in ../data/data.csv relative to this file)
data_path = r"E:\House Price Prediction Model\data\data.csv"  
data = pd.read_csv(data_path)

# -----------------------------
# 2. Basic Preprocessing
# -----------------------------
# Fill missing values with 0 or as per your notebook
data = data.fillna(0)

# Select features (based on your dataset columns)
features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'yr_built']
target = 'price'

X = data[features]
y = data[target]

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 4. Train Linear Regression
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 5. Save the Model
# -----------------------------
model_path = r"E:\House Price Prediction Model\model\model.pkl"
with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model trained successfully and saved at: {model_path}")
