import streamlit as st
import pandas as pd
import joblib
import os

# Load the trained model
# Dynamically build absolute path
model_path = os.path.join(os.path.dirname(__file__), "../model/closet_model.pkl")
model = joblib.load(model_path)

st.title("👗 Wear Predictor 2.0")
st.write("Predict the chance you'll actually wear a new clothing item!")

# Category options (same as your collection script)
BRANDS = ["Aritzia", "Garage", "Dynamite", "Lululemon", "Shein", "H&M", "American Eagle", "Ardene", "Hollister", "Tankair", "Other"]
TYPES = ["athleisure", "coquette", "casual", "workwear", "eveningwear", "basics", "party"]
FITS = ["tight", "oversized", "structured", "flowy"]
COLORS = ["neutrals", "pastels", "bold", "earth tones", "black/white", "patterned"]

# User input fields
brand = st.selectbox("Brand", BRANDS)
item_type = st.selectbox("Type", TYPES)
fit = st.selectbox("Fit", FITS)
color = st.selectbox("Color palette", COLORS)
trendy = st.checkbox("Is it trendy right now?")
comfort_level = st.slider("Comfort Level (1 = bad, 5 = super comfy)", 1, 5, 3)
revealing_level = st.slider("Revealing Level (1 = modest, 3 = very revealing)", 1, 3, 2)
fabric_quality = st.slider("Fabric Quality (1 = bad, 5 = luxury)", 1, 5, 3)

# Predict button
if st.button("Predict Wear Likelihood"):
    # Package the inputs into a DataFrame
    user_input = pd.DataFrame([{
        "brand": brand,
        "type": item_type,
        "fit": fit,
        "color": color,
        "trendy": 1 if trendy else 0,
        "comfort_level": comfort_level,
        "revealing_level": revealing_level,
        "fabric_quality": fabric_quality
    }])

    # Predict
    prediction = model.predict(user_input)[0]
    prediction = round(prediction * 100, 2)  # Convert back to % for user display

    st.success(f"🛍️ Estimated chance you'll wear this item: **{prediction}%**")

    # Smart Buy Indicator
    if prediction >= 75:
        st.markdown("<h2 style='color:green;'>✅ Smart Buy!</h2>", unsafe_allow_html=True)
        st.balloons()  # 🎈 Balloons for Smart Buy
    elif 40 <= prediction < 75:
        st.markdown("<h2 style='color:orange;'>🤔 Okay Buy</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color:red;'>🚫 Regret Incoming</h2>", unsafe_allow_html=True)