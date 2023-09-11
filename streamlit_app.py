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


if selected_feature == "Appointment Scheduling":
    st.subheader("Book an Appointment with a Doctor")

    # Add appointment scheduling form fields
    doctor = st.text_input("Doctor's Name")
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    symptoms = st.text_area("Symptoms")
    get_location = st.button("Get Location (GPS)")

    # Create a button to submit the appointment booking
    book_appointment_button = st.button("Book Appointment")

    # Display appointment details
    if book_appointment_button:
        st.success("Appointment booked successfully!")
        st.write("Doctor:", doctor)
        st.write("Appointment Date:", appointment_date)
        st.write("Appointment Time:", appointment_time)
        st.write("Symptoms:", symptoms)
        if get_location:
            st.write("GPS Location: [Insert GPS coordinates here]")

if selected_feature == "Medical Records Access":
    st.subheader("Access Your Medical Records")

    # Add a file uploader for medical records
    st.write("Upload your medical records file:")
    st.write("Your medical records will be securely stored and cross-referenced with the WHO database to provide you with the best healthcare recommendations.")
    uploaded_file = st.file_uploader("Choose a file...", type=["pdf", "jpg", "png"])
    
    # Display the uploaded file
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        st.write("File Name:", uploaded_file.name)
        st.write("File Size:", uploaded_file.size, "bytes")

if selected_feature == "Symptom Checker":
    st.subheader("Symptom Checker")

    # Create a form for symptom checking
    with st.form("Symptom Checker"):
        st.write("Please select the symptoms you are experiencing:")
        symptom_fever = st.checkbox("Fever")
        symptom_cough = st.checkbox("Cough")
        symptom_breathing_difficulty = st.checkbox("Difficulty Breathing")
        symptom_headache = st.checkbox("Headache")
        symptom_fatigue = st.checkbox("Fatigue")
        symptom_loss_of_taste_or_smell = st.checkbox("Loss of Taste or Smell")
        
        # Create a button to check symptoms
        check_symptoms_button = st.form_submit_button("Check Symptoms")

    # Display symptom checking results
    if check_symptoms_button:
        st.subheader("Symptom Checker Results")
        st.write("Based on your selected symptoms, it is recommended to consult a healthcare professional.")
