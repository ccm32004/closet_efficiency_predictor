import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model/closet_model.pkl")

# Example: Create a new clothing item you want to predict
new_item = pd.DataFrame([{
    "brand": "Shein",
    "type": "casual",
    "fit": "tight",
    "color": "neutrals",
    "trendy": 1,
    "comfort_level": 4,
    "revealing_level": 3,
    "fabric_quality": 1
}])

# Predict wear frequency
prediction = model.predict(new_item)
print(f"Predicted wear frequency: {prediction[0]:.2f}")
