import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import joblib
import os

# Load your actual closet data
csv_path = "data/closet_items.csv"
df = pd.read_csv(csv_path)

# Features and target
X = df.drop("wear_frequency", axis=1)
y = df["wear_frequency"]

# Define feature types
categorical_features = ["brand", "type", "fit", "color"]
binary_features = ["trendy"]
numeric_features = ["comfort_level", "revealing_level", "fabric_quality"]

# Preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("bin", "passthrough", binary_features),  # passthrough 0/1 columns
        ("num", StandardScaler(), numeric_features)  # scale numeric ratings
    ]
)

# Pipeline
model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model_pipeline.fit(X_train, y_train)

# Evaluate
predictions = model_pipeline.predict(X_test)
mse = mean_squared_error(y_test, predictions)

#tells how far off the predictions are from the actual values
print(f"Mean Squared Error: {mse:.4f}")

# Save the trained model
os.makedirs("model", exist_ok=True)
joblib.dump(model_pipeline, "model/closet_model.pkl")
print("\nModel saved to 'model/closet_model.pkl'")
