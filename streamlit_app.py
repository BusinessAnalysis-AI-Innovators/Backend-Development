import streamlit as st

# Set the background color to blue
st.markdown(
    """
    <style>
    body {
        background-color: #3498db;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a heading
st.header("HealthTele-Ease")

# Create buttons in a horizontal row
button_col1, button_col2, button_col3, button_col4, button_col5 = st.beta_columns(5)

# Button 1: User Registration & Login
if button_col1.button("User Registration & Login"):
    # Add your code for this button's functionality here
    pass

# Button 2: Profile Management
if button_col2.button("Profile Management"):
    # Add your code for this button's functionality here
    pass

# Button 3: Appointment Scheduling
if button_col3.button("Appointment Scheduling"):
    # Add your code for this button's functionality here
    pass

# Button 4: Medical Records Access
if button_col4.button("Medical Records Access"):
    # Add your code for this button's functionality here
    pass

# Button 5: Symptom Checker
if button_col5.button("Symptom Checker"):
    # Add your code for this button's functionality here
    pass

