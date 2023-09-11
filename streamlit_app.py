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
    
if selected_feature == "Profile Management":
    st.subheader("Manage Your Health Information")

    # Create form to manage health information
    with st.form("Health Information"):
        # Add form fields for health information
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        age = st.number_input("Age", min_value=0)
        gender = st.radio("Gender", ("Male", "Female", "Other"))

        # Add a textarea for additional comments
        comments = st.text_area("Additional Comments")

        # Create a button to submit the form
        submit_button = st.form_submit_button("Save Information")

    # Display the submitted information
    if submit_button:
        st.success("Health information saved successfully!")
        st.write("First Name:", first_name)
        st.write("Last Name:", last_name)
        st.write("Age:", age)
        st.write("Gender:", gender)
        st.write("Additional Comments:", comments)
