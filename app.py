import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('linear_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.title("House Price Predictor 🏠")

size = st.number_input("Enter house size (in sqm):", min_value=10, max_value=500, value=50)

if st.button("Predict Price"):
    prediction = model.predict(np.array([[size]]))
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")
