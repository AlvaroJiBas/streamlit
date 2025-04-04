import streamlit as st
import pandas as pd
if 'workout' not in st.session_state:
    st.session_state['workout']= pd.DataFrame(pd.read_csv("workout.csv"))

st.title("💪Workout Logger")
title = st.text_input("Exercise Name")
sets = st.number_input("Sets",min_value=1,value=1)
reps = st.number_input("Reps",min_value=1,value=1)
weight = st.number_input("Weight (kg)",min_value=1,value=10)
if st.button("Log Workout", type="primary" ):
    new_row = {"exercise" : title, "sets" : sets, "reps" : reps, "weight": weight}
    st.session_state['workout'] = pd.concat([st.session_state['data'], pd.DataFrame([new_row])], ignore_index=True)
    dataframe =pd.DataFrame( st.session_state['workout'])
    dataframe.to_csv("workout.csv")
st.subheader("🏋️‍♀️Workout history")
st.write(st.session_state['workout'])
