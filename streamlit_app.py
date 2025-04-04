import streamlit as st

pages= {
    "Exercise":[
    st.Page("home.py", title ="🏠Home"),
    st.Page("BMI.py", title="🚵BMI tracker"),
    st.Page("Workout.py", title="💪Workout Logger"),
    st.Page("Progress.py", title="🏃‍♂️‍➡️Progress Tracker")
    ]

}
pg= st.navigation(pages)
pg.run()
    
