import streamlit as st
import joblib
import numpy as np
from PIL import Image  

model = joblib.load('regressor.pkl')   

st.set_page_config(page_title="Taxi Price Prediction", page_icon="🚕", layout="centered")

image = Image.open("taxi_image.jpeg")  
st.image(image, use_column_width=True)

st.title("🚖 Taxi Price Prediction App")
st.write("Estimate your taxi fare quickly and easily by providing trip details.")

st.markdown("### Enter Your Trip Details:")
trip_distance = st.number_input(
    "Trip Distance (in kilometers):", 
    min_value=0.0, 
    max_value=200.0,
    value=19.35, 
    step=0.1
)

passenger_count = st.number_input(
    "Passenger Count:", 
    min_value=1.0, 
    max_value=4.0,  
    value=3.0, 
    step=1.0
)

base_fare = st.number_input(
    "Base Fare (in your currency):", 
    min_value=0.0, 
    max_value=10.0,  
    value=3.56, 
    step=0.01
)

per_km_rate = st.number_input(
    "Rate Per Kilometer (in your currency):", 
    min_value=0.0, 
    max_value=10.0,  
    value=1.21, 
    step=0.01
)

per_minute_rate = st.number_input(
    "Rate Per Minute (in your currency):", 
    min_value=0.0, 
    max_value=10.0,  
    value=0.32, 
    step=0.01
)

trip_duration = st.number_input(
    "Trip Duration (in minutes):", 
    min_value=0.0, 
    max_value=240.0, 
    value=53.82, 
    step=0.1
)


if st.button("Calculate Fare"):
   
    input_features = np.array([[trip_distance, passenger_count, base_fare, per_km_rate, per_minute_rate, trip_duration]])
    predicted_price = model.predict(input_features)[0]


    st.success(f"Estimated Trip Price: **${predicted_price:,.2f}** 🚕")


st.markdown("---")
st.markdown("Developed by Gowtham")


st.markdown(
    """
    <style>
    .stButton>button {
        color: white;
        background-color: #007BFF;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
