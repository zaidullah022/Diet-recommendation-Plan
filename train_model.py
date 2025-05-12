import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Load Dataset
data = pd.read_csv("diet_dataset.csv")
print("Dataset Preview:\n", data.head())

# Data Preprocessing
preference_map = {'veg': 0, 'non-veg': 1}
goal_map = {'weight loss': 0, 'muscle gain': 1}

data['diet_preference'] = data['diet_preference'].map(preference_map)
data['diet_goal'] = data['diet_goal'].map(goal_map)

data['height'] = data['height'].replace(0, 1)  # Avoid division by zero
data['bmi'] = data['weight'] / (data['height'] / 100) ** 2

# Features and Target
X = data[['age', 'weight', 'height', 'bmi', 'diet_preference', 'diet_goal']]
y = data['calories']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save Model
pickle.dump(model, open('diet_model.pkl', 'wb'))
print("Model trained and saved successfully.")