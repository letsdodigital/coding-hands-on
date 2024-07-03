import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 10 - A reward!

NOTES: So you have worked hard to get to this point, so we thought you could do
with a little reward. We have done most of the work for you in this next section.
Have a look at what we did. We added a new dictionary (can you find its name?) 
and added something to the input fields. All you need to add is some code to 
check that the button has been pressed.

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


def initialise():
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
    # We have added this here for you
    fields = {}

    conn = st.connection("supabase", type=SupabaseConnection)

    users = execute_query(conn.table("users").select("*"), ttl="10m")

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = execute_query(
        conn.table("patient_demographics").select("*"), ttl="10m"
    )

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
        # We have added the `field` dictionary with keys here for you.
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )
        fields["first_name"] = st.text_input("First name")
        fields["last_name"] = st.text_input("Last name")
        fields["date_of_birth"] = st.date_input("Date of birth", None)
        fields["patient_email"] = st.text_input("Email")

        st.header("Intervention")
        fields["intervention"] = st.text_input("Intervention", disabled=True)
        fields["full_description"] = st.text_input(
            "Full description", disabled=True
        )
        fields["intended_benefits"] = st.text_input(
            "Intended benefits", disabled=True
        )
        fields["potential_risks"] = st.text_input(
            "Potential risks", disabled=True
        )

        st.header("Signature")

        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        # Test if submitted is true and then write to the browser
        # "Button pressed"

    return


if __name__ == "__main__":
    # Add a call to the `initialise` function
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
