import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 12 - Updating functions and managing the submit button

OUTLINE: We are now going to get you to bulk out the functions you have already
written and then write a new one. We are also going to get you to check that 
all fo the fields within the form (there will be a black thin border around 
these fields) are all filled with data.

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


# Initialise the global lists `consent_types`, `hospital_numbers` and `patients`


def initialise():
    # Add a global call to `consent_types`

    initialise_state = "test_data"

    # Initialise a session state called `submitted_consent_id` to 0. You do NOT
    # need to check if it exists already as this needs to reset every time the
    # script runs.

    # Add a session state called `patient_id` and initialise to 0. This DOES
    # need to be checked to see if it exists already.

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

    # Add a session state called `intervention_id` and initialise to 0. This
    # DOES need to be checked to see if it exists already.

    if "intervention_state" not in st.session_state:
        st.session_state.intervention_state = initialise_state
    if "full_description_state" not in st.session_state:
        st.session_state.full_description_state = initialise_state
    if "intended_benefits_state" not in st.session_state:
        st.session_state.intended_benefits_state = initialise_state
    if "potential_risks_state" not in st.session_state:
        st.session_state.potential_risks_state = initialise_state

    # Start another connection to the database

    # Query the `consent_types` table and store the results in the
    # `consent_types` list.

    return


def on_change_hospital_number():
    # Delete this line of code
    st.write(
        f"Hospital number changed to: { st.session_state.hospital_number_input }"
    )

    # Create a variable called `hospital_number_input` and initialise it with
    # the value of the session state `hospital_number_input`.

    # Now create some conditional code. Firstly, check if the value of
    # `hospital_number_input` is inside the list `hospital_numbers`. Write to
    # the browser "Valid hospital number" if the hospital number is valid.

    # Use `elif` to check if `hospital_number_input` is an empty string (eg
    # ""). Write to the browser "empty hospital number field" if this is true.

    # Use an "else" statement that writes to the browser an error message
    # (using `st.error`) that the hospital number is not valid.

    return


def on_change_intervention():
    # Delete this line of code
    st.write(
        f"Intervention changed to: { st.session_state.intervention_input }"
    )

    # Create a `for loop`. This needs to loop through `consent_types.data` and
    # have a loop variable called `intervention`.

    # Within the above `for loop`, add an `if` statement, checking if the key
    # "type" inside the dictionary `intervention` is equal to the session state
    # `intervention_input`. If the `if` statement is true, write to the
    # browser "An intervention was selected". Add a `break` after this to stop
    # looping through the for loop further.

    # Add a `else` statement, associated with the for loop, that writes to the
    # browser "Intervention deselected".

    return


# 1. Create another function called `user_id_get`. Now this function takes two
# arguments, the first `users` and the second `user_name`.
# 2. This function should loop over `users.data` with the loop variable being
# `user`.
# 3. Within this loop, check if the key "user_name" in the dictionary `user` is
# equal to `user_name`.
# 4. If this last statement is true, return `user["id"]`.
# 5. The last line of code for the function, outside of the for loop needs to
# return 0.


def main():
    # add a global statement for `hospital_numbers` and `patients`

    # We added this placeholder to display errors messages that we have
    # raise later.
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
            "Intervention", st.session_state.intervention_state, disabled=True
        )
        fields["full_description"] = st.text_input(
            "Full description",
            st.session_state.full_description_state,
            disabled=True,
        )
        fields["intended_benefits"] = st.text_input(
            "Intended benefits",
            st.session_state.intended_benefits_state,
            disabled=True,
        )
        fields["potential_risks"] = st.text_input(
            "Potential risks",
            st.session_state.potential_risks_state,
            disabled=True,
        )

        st.header("Signature")
        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        if submitted:
            # Remove this line
            st.write("Button pressed")

            # 1. Use an `all` statement to check if all the field dictionary
            # values are not empty. This should pass as `initialise_state =
            # "test_data"` (see the initialisation function above).
            # 2. You can check what happens by changing `initialise_state` to
            # an empty string, eg "".
            # 3. Use the `all` statement to store the result in a variable
            # called `all_fields_filled` and then use an `if` statement to check
            # this variable.
            # 4. If all of the fields are not filled, use `st.error`
            # and `error_placeholder.error` (which links to the placeholder at
            # the beginning of the main function) to display error messages.
            # 5. Use a `return` to end the main function if not all of the
            # fields are filled.
            # 6. If all the fields are filled, write to the browser something
            # positive.

    return


if __name__ == "__main__":
    initialise()
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
