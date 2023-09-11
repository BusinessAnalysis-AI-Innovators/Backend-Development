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

    if st.button("Profile Management"):
        st.write("Profile Management Feature Selected")

    if st.button("Appointment Scheduling"):
        st.write("Appointment Scheduling Feature Selected")

    if st.button("Medical Records Access"):
        st.write("Medical Records Access Feature Selected")

    if st.button("Symptom Checker"):
        st.write("Symptom Checker Feature Selected")

# Add an empty space with a black vertical line
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.write("This is where the selected feature details will appear.")

