import streamlit as st
import pandas as pd
st.title("🚵BMI tracker")

if 'data' not in st.session_state:
     st.session_state['data']= pd.DataFrame(pd.read_csv("BMI.csv"))
weight = st.number_input("Enter your weight (kg)",min_value=1,value=50)
height = st.number_input("Enter your height (cm)",min_value=1,value=100)
if st.button("Calculate your BMI", type="primary" ):
    BMI = weight / height * height
    new_row = {"weight" : weight, "height" : height, "BMI" : BMI}
    st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([new_row])], ignore_index=True)
    dataframe =pd.DataFrame( st.session_state['data'])
    dataframe.to_csv("BMI.csv")
    st.success(f"Your BMI is: {BMI}")
    st.write("✌️ BMI recor saved")
st.subheader("🏋️‍♀️BMI progress")
st.line_chart(st.session_state['data'], y="BMI")

st.session_state['data']