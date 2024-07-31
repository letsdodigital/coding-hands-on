import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 14 - All done

You have now completed all the exercises in this lesson. Well done! You have
learnt how to read and write to a database in the cloud, and how to use Streamlit
to create a web app. You have also learnt how to use the Streamlit session state
to store data between pages. You have also learnt how to use the Streamlit form 
to create a form that can be submitted to the database.

We have added some docstrings to the functions in this exercise.
"""


def initialise():
    """Initialise the session state.

    Initialises the session state.
    """
    initialise_state = ""

    st.session_state.submitted_consent_id = 0

    if "patient_id" not in st.session_state:
        st.session_state.patient_id = 0
    if "hospital_number_state" not in st.session_state:
        st.session_state.hospital_number_state = initialise_state
    if "first_name_state" not in st.session_state:
        st.session_state.first_name_state = initialise_state
    if "last_name_state" not in st.session_state:
        st.session_state.last_name_state = initialise_state
    if "date_of_birth_state" not in st.session_state:
        st.session_state.date_of_birth_state = initialise_state
    if "patient_email_state" not in st.session_state:
        st.session_state.patient_email_state = initialise_state
    if "intervention_id" not in st.session_state:
        st.session_state.intervention_id = 0
    if "intervention_state" not in st.session_state:
        st.session_state.intervention_state = initialise_state
    if "full_description_state" not in st.session_state:
        st.session_state.full_description_state = initialise_state
    if "intended_benefits_state" not in st.session_state:
        st.session_state.intended_benefits_state = initialise_state
    if "potential_risks_state" not in st.session_state:
        st.session_state.potential_risks_state = initialise_state

    return


def on_change_hospital_number(patients, hospital_numbers):
    """Retrieve patient details from the hospital number.

    Retrieves the patient details from the hospital number.

    Args:
        patients (dict): The patients data.
        hospital_numbers (list): The list of hospital numbers
    """
    if "hospital_number_input" not in st.session_state:
        return

    hospital_number_input = st.session_state.hospital_number_input

    if hospital_number_input in hospital_numbers:
        for patient in patients.data:
            if patient["hospital_number"] == hospital_number_input:
                st.session_state.patient_id = patient["id"]
                st.session_state.hospital_number_state = hospital_number_input
                st.session_state.first_name_state = patient["first_name"]
                st.session_state.last_name_state = patient["last_name"]
                st.session_state.date_of_birth_state = patient["date_of_birth"]
                st.session_state.patient_email_state = patient["email"]
                break
    elif hospital_number_input == "":
        st.session_state.patient_id = ""
        st.session_state.hospital_number_state = ""
        st.session_state.first_name_state = ""
        st.session_state.last_name_state = ""
        st.session_state.date_of_birth_state = ""
        st.session_state.patient_email_state = ""
    else:
        st.error("Invalid hospital number. Please try again.")

    return


def on_change_intervention(consent_types):
    """Retrieve intervention details from the intervention type.

    Retrieves the intervention details from the intervention type.

    Args:
        consent_types (dict): The consent types data.
    """
    if "intervention_input" not in st.session_state:
        return

    for intervention in consent_types.data:
        if intervention["type"] == st.session_state.intervention_input:
            st.session_state.intervention_id = intervention["id"]
            st.session_state.intervention_state = (
                st.session_state.intervention_input
            )
            st.session_state.full_description_state = intervention[
                "full_description"
            ]
            st.session_state.intended_benefits_state = intervention[
                "intended_benefits"
            ]
            st.session_state.potential_risks_state = intervention[
                "potential_risks"
            ]
            break
    else:
        st.session_state.intervention_id = 0
        st.session_state.intervention_state = ""
        st.session_state.full_description_state = ""
        st.session_state.intended_benefits_state = ""
        st.session_state.potential_risks_state = ""

    return


def user_id_get(users, user_name):
    """Get the user ID from the user name.

    Returns the user ID from the user name.

    Args:
        users (dict): The users data.
        user_name (str): The user name.
    Returns:
        int: The user ID.
    """

    for user in users.data:
        if user["user_name"] == user_name:
            return user["id"]
    return 0


def main():
    """The main function"""
    error_placeholder = st.empty()
    fields = {}

    conn = st.connection("supabase", type=SupabaseConnection)

    users = execute_query(conn.table("users").select("*"), ttl="10m")

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = execute_query(
        conn.table("patient_demographics").select("*"), ttl="10m"
    )

    hospital_numbers = [
        patient["hospital_number"]
        for patient in patients.data
        if "hospital_number" in patient
    ]

    consent_types = execute_query(
        conn.table("consent_types").select("*"), ttl="10m"
    )

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    st.text_input(
        'Hospital number (eg "HN001")',
        key="hospital_number_input",
        on_change=on_change_hospital_number(patients, hospital_numbers),
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=on_change_intervention(consent_types),
    )

    with st.form("consent_form"):
        st.header("Patient details")
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )
        fields["first_name"] = st.text_input(
            "First name", st.session_state.first_name_state, disabled=True
        )
        fields["last_name"] = st.text_input(
            "Last name", st.session_state.last_name_state, disabled=True
        )
        fields["date_of_birth"] = st.text_input(
            "Date of birth",
            st.session_state.date_of_birth_state,
            disabled=True,
        )
        fields["patient_email"] = st.text_input(
            "Email", st.session_state.patient_email_state, disabled=True
        )

        st.header("Intervention")
        fields["intervention"] = st.text_input(
            "Intervention",
            st.session_state.intervention_state,
            disabled=True,
        )
        fields["full_description"] = st.text_area(
            "Full description",
            st.session_state.full_description_state,
            disabled=True,
        )
        fields["intended_benefits"] = st.text_area(
            "Intended benefits",
            st.session_state.intended_benefits_state,
            disabled=True,
        )
        fields["potential_risks"] = st.text_area(
            "Potential risks",
            st.session_state.potential_risks_state,
            disabled=True,
        )

        st.header("Signature")
        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        if submitted:
            all_fields_filled = all(value for value in fields.values())

            if not all_fields_filled:
                st.error("All fields need to be filled.")
                error_placeholder.error("All fields need to be filled.")
                return

            consent_final_data = {
                "patient_id": st.session_state.patient_id,
                "consent_type_id": st.session_state.intervention_id,
                "user_id": user_id_get(users, fields["signed_by"]),
            }

            result = (
                conn.table("submitted_consents")
                .insert([consent_final_data], count="None")
                .execute()
            )

            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.submitted_consent_id = result.data[0]["id"]

            st.switch_page("pages/final_consent_form.py")
    return


if __name__ == "__main__":
    initialise()
    main()
