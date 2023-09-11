import streamlit as st

# Set the title and page icon
st.set_page_config(page_title="HealthTele-Ease", page_icon="🌡️")

# Add custom CSS to change the background color to blue
st.markdown(
    """
    <style>
    body {
        background-color: #0074e4; /* Blue color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a title
st.title("Welcome to HealthTele-Ease")

# Create a vertical column layout for the buttons
col1, col2, col3, col4, col5 = st.beta_columns(5)

# Add buttons for different features in a vertical row
with col1:
    if st.button("User Registration & Login"):
        st.write("User Registration & Login Feature Selected")

with col2:
    if st.button("Profile Management"):
        st.write("Profile Management Feature Selected")

with col3:
    if st.button("Appointment Scheduling"):
        st.write("Appointment Scheduling Feature Selected")

with col4:
    if st.button("Medical Records Access"):
        st.write("Medical Records Access Feature Selected")

with col5:
    if st.button("Symptom Checker"):
        st.write("Symptom Checker Feature Selected")
