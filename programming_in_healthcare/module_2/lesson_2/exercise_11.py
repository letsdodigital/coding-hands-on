import streamlit as st
from st_supabase_connection import SupabaseConnection

"""Exercise 11 - It is a question of state

NOTES: So now you are going to add a lot of code to manage state. Start at the
line START HERE. After that, go back to the beginning and carry out the rest of
the tasks required.
"""

def initialise():
    # We added this line for you
    initialise_state = "test_data"

    # Now you need to initialise all of your state keys, checking if they have 
    # been initialised already. We have done the first one for you.
    if "intervention_state" not in st.session_state:
        st.session_state.intervention_state = initialise_state
    return


def on_change_hospital_number():
    st.write(
        f"Hospital number changed to: { st.session_state.hospital_number_input }"
    )

    return


def on_change_intervention():
    st.write(
        f"Intervention changed to: { st.session_state.intervention_input }"
    )

    return


def main():
    fields = {}
    
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    # Get a list of valid hospital numbers from the patients.data
    # variable. Call the resulting list `hospital_numbers`.

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    st.text_input(
        'Hospital number (eg "HN001")',
        key="hospital_number_input",
        on_change=on_change_hospital_number,
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=on_change_intervention,
    )

    with st.form("consent_form"):
        st.header("Patient details")

        # START HERE
        # To each input field (EXCEPT the "Signed off by" field) add the second
        # argument, which is `value`, as a session state variable. This should 
        # match the key in the field dictionary, but with a suffix of "_state".
        # Please also disable the field. We have already done all of the changes
        # for the first field "hospital_number" below. Complete for the rest.
        
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )

        fields["first_name"] = st.text_input("First name")
        fields["last_name"] = st.text_input("Last name")
        # Also convert this line from date to text
        fields["date_of_birth"] = st.date_input("Date of birth", None)
        fields["patient_email"] = st.text_input("Email")

        st.header("Intervention")
        fields["intervention"] = st.text_input("Intervention", disabled=True)
        fields["full_description"] = st.text_input("Full description", disabled=True)
        fields["intended_benefits"] = st.text_input("Intended benefits", disabled=True)
        fields["potential_risks"] = st.text_input("Potential risks", disabled=True)

        st.header("Signature")

        # DO NOT alter this field
        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write("Button pressed")

    return


if __name__ == "__main__":
    # Add a call to the `initialise` function
    main()
