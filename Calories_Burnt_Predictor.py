import streamlit as st
import pickle
import numpy as np

# ✅ Set Page Config
st.set_page_config(page_title="🔥 Calorie Burn Predictor", layout="centered")

# ✅ Load Models
model_files = {
    "XGBoost Regressor": "model_1.pkl",
    "Linear Regression": "model_2.pkl",
    "Decision Tree Regressor": "model_3.pkl",
    "Random Forest Regressor": "model_4.pkl",
}

# ✅ Custom CSS for a Light Blue Theme
st.markdown(f"""
    <style>
        /* 🔹 Light Blue Background */
        .stApp {{
            background-color: #F0F8FF; /* Light Blue */
            font-family: 'Inter', sans-serif;
        }}

        /* 🔹 Title Styling - Dark Blue */
        .title-box {{
            text-align: center;
            font-size: 44px;
            font-weight: 900;
            color: #003366; /* Dark Blue */
            margin-bottom: 30px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }}

        /* 🔹 Text & Label Styling */
        label, .stSelectbox label, .stNumberInput label {{
            color: #003366 !important; /* Dark Blue for Readability */
            font-weight: 600;
        }}

        /* ✅ Input Fields - Light Blue with Dark Text */
        .stTextInput, .stNumberInput, .stSelectbox {{
            background-color: #ADD8E6 !important; /* Light Blue */
            color: #000000 !important; /* Black Text */
            border-radius: 8px !important;
            border: 1px solid #4682B4 !important; /* Steel Blue Border */
            padding: 12px !important;
        }}

        /* ✅ Button - Gradient Blue */
        .stButton>button {{
            width: 100%;
            background: linear-gradient(135deg, #4682B4, #1E90FF); /* Steel Blue to Dodger Blue */
            color: white !important;
            font-size: 18px;
            font-weight: bold;
            border-radius: 12px;
            padding: 14px;
            transition: 0.3s;
            border: none;
        }}
        .stButton>button:hover {{
            background: linear-gradient(135deg, #1E90FF, #4682B4);
        }}

        /* ✅ Prediction Box - Blue */
        .prediction-box {{
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
            background: #1E90FF; /* Dodger Blue */
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0px 4px 15px rgba(30, 144, 255, 0.3);
        }}
    </style>
""", unsafe_allow_html=True)

# ✅ Title (Now Clearly Visible in Dark Blue)
st.markdown('<h1 class="title-box" style="color: #008000;">🔥 CALORIE BURN PREDICTOR</h1>', unsafe_allow_html=True)

# ✅ Model Selection Dropdown
selected_model = st.selectbox("Select Prediction Model", list(model_files.keys()))

# ✅ Grid Layout for Inputs
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    age = st.number_input("Age (years)", min_value=0, step=1, value=25)
    height = st.number_input("Height (cm)", step=1.0, value=170.0)
    weight = st.number_input("Weight (kg)", step=1.0, value=70.0)

with col2:
    exercise_duration = st.number_input("Activity Duration (mins)", step=1.0, value=30.0)
    heart_rate = st.number_input("Heart Rate (bpm)", step=1.0, value=90.0)
    body_temp = st.number_input("Body Temperature (°C)", step=0.1, value=36.5)

# ✅ Predict Button
if st.button("💪 Calculate Calories Burned", key="predict"):
    user_input = np.array([[gender, age, height, weight, exercise_duration, heart_rate, body_temp]])

    # Load the selected model
    model_path = model_files[selected_model]
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    # Make prediction
    prediction = model.predict(user_input)[0]

    # ✅ Show Prediction in Styled Blue Box
    st.markdown(f'<div class="prediction-box">🔥 Estimated Calories Burnt using {selected_model}: {prediction:.2f} kcal</div>', unsafe_allow_html=True)
