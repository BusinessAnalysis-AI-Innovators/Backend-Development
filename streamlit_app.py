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
    .divider {
        border-left: 1px solid black; /* Black vertical line */
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a title
st.title("Welcome to TeleHealth-Ease")

# Add an introduction for patients
st.write("Empowering You with Easy Access to Quality Healthcare Services")

# Create a sidebar for buttons with a divider
with st.sidebar:
    st.subheader("Select a Feature:")
    if st.button("User Registration & Login"):
        st.write("User Registration & Login Feature Selected")
        st.subheader("User Registration / Login Area:")
        username = st.text_input("Username", "")
        password = st.text_input("Password", "", type="password")
        registration_button = st.button("Register")
        login_button = st.button("Login")
        if registration_button:
            st.success("Registration Successful!")
        if login_button:
            st.success("Login Successful!")

# Add an empty space with a black vertical line
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Display feature details or registration/login area
feature_selected = st.session_state.get("feature_selected", "")

if feature_selected == "User Registration & Login":
    st.write("This is where the User Registration / Login Area details will appear.")
else:
    st.write("This is where the selected feature details will appear.")

# Update the selected feature based on the button clicked
if st.button("User Registration & Login"):
    st.session_state.feature_selected = "User Registration & Login"
elif st.button("Profile Management"):
    st.session_state.feature_selected = "Profile Management"
elif st.button("Appointment Scheduling"):
    st.session_state.feature_selected = "Appointment Scheduling"
elif st.button("Medical Records Access"):
    st.session_state.feature_selected = "Medical Records Access"
elif st.button("Symptom Checker"):
    st.session_state.feature_selected = "Symptom Checker"
