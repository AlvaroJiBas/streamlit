import streamlit as st
import pandas as pd
if 'workout' not in st.session_state:
    st.session_state['workout']= pd.DataFrame(pd.read_csv("workout.csv"))
if 'data' not in st.session_state:
     st.session_state['data']= pd.DataFrame(pd.read_csv("BMI.csv"))   

st.title("🏃‍♂️‍➡️Progress Tracker")
st.subheader("Weight lifted over time")
st.line_chart(st.session_state['workout'], y="weight")
st.subheader("🏋️‍♀️BMI over time")
st.line_chart(st.session_state['data'], y="BMI")