import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("💼 Salary Prediction App")

# Simple training inside app (video-style)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([30000, 40000, 50000, 60000, 70000])

model = LinearRegression()
model.fit(X, y)

experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=20.0,
    step=0.5
)

if st.button("Predict Salary"):
    salary = model.predict([[experience]])
    st.success(f"💰 Predicted Salary: ₹ {salary[0]:,.2f}")
