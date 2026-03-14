
import streamlit as st
import pickle

st.title("Student Pass Prediction")

model = pickle.load(open("model.pkl","rb"))

hours = st.number_input("Enter Study Hours",0,24)

if st.button("Predict"):
    result = model.predict([[hours]])

    if result[0] == 1:
        st.success("Student will PASS")
    else:
        st.error("Student will FAIL")
