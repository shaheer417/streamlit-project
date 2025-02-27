import streamlit as st
import pandas as pd

st.title("BMI Calculator")
height = st.slider("enter your height in cm :", 100, 250, 175)
weight = st.slider("enter your weight in kg :", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)
st.write(f"your BMI is {bmi:.2f}:")

st.write("#### BMI Catgeories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI of 30 or more")