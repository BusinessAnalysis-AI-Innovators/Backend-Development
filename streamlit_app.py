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

# Create a selectbox for feature selection
selected_feature = st.selectbox("Select a Feature:", [
    "User Registration & Login",
    "Profile Management",
    "Appointment Scheduling",
    "Medical Records Access",
    "Symptom Checker",
])

# Display feature details or registration/login area
if selected_feature == "User Registration & Login":
    st.subheader("User Registration / Login Area:")
    username = st.text_input("Username", "")
    password = st.text_input("Password", "", type="password")
    registration_button = st.button("Register")
    login_button = st.button("Login")
    
    # Center the buttons
    st.write("", "", text_align="center")
    if registration_button:
        st.success("Registration Successful!")
    if login_button:
        st.success("Login Successful!")
