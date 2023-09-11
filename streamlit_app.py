import streamlit as st

# Set the title and page icon
st.set_page_config(page_title="HealthTele-Ease", page_icon="🌡️")

# Add a title
st.title("Welcome to HealthTele-Ease")

# Add buttons for different features
if st.button("User Registration & Login"):
    st.write("User Registration & Login Feature Selected")
    
if st.button("Profile Management"):
    st.write("Profile Management Feature Selected")

if st.button("Appointment Scheduling"):
    st.write("Appointment Scheduling Feature Selected")

if st.button("Medical Records Access"):
    st.write("Medical Records Access Feature Selected")

if st.button("Symptom Checker"):
    st.write("Symptom Checker Feature Selected")

