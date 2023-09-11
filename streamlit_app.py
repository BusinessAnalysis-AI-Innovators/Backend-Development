import streamlit as st

# Set the title and page icon
st.set_page_config(page_title="TeleHealth-Ease App", page_icon="🌡️")

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
st.title("Welcome to TeleHealth-Ease")

# Add an introduction for patients
st.write("Empowering You with Easy Access to Quality Healthcare Services")

# Add buttons for different features
if st.button("User Registration & Login"):
    st.write("User Registration & Login Feature Selected")
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line
    
if st.button("Profile Management"):
    st.write("Profile Management Feature Selected")
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

if st.button("Appointment Scheduling"):
    st.write("Appointment Scheduling Feature Selected")
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

if st.button("Medical Records Access"):
    st.write("Medical Records Access Feature Selected")
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

if st.button("Symptom Checker"):
    st.write("Symptom Checker Feature Selected")
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

