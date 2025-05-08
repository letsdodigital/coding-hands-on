import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 13 - Adding more code to `on_change` and `submitted`

OUTLINE: This is the final push of code. We are going to get you to do several 
steps in this exercise, so watch your step.

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


def initialise():
    # initialise this to an empty string
    initialise_state = "test_data"

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
    if "hospital_number_input" not in st.session_state:
        return

    hospital_number_input = st.session_state.hospital_number_input

    if hospital_number_input in hospital_numbers:
        # Delete this line of code
        st.write("Valid hospital number")

        # You are now going to create code that fills in the patient demographic
        # fields.
        # 1. Use a `for` loop to loop through `patients.data` and have a loop
        # variable of `patient`.
        # 2. Within this loop, check if the key "hospital_number" of the
        # dictionary `patient` is equal to `hospital_number_input`.
        # 3. If the above is true, then set the session states relating to the
        # patient demographics to the values in found in the database. We have
        # done the first 3 for you. You will need to do the other 3. Uncomment
        # to use them. The full list of database fields are:
        # "id", "hospital_number", "first_name", "last_name", "date_of_birth",
        # "email".

        #       st.session_state.patient_id = patient["id"]
        #       st.session_state.hospital_number_state = hospital_number_input
        #       st.session_state.first_name_state = patient["first_name"]

        # Add a break here.

    elif hospital_number_input == "":
        # Delete this line of code
        st.write("empty hospital number field")

        # Of all the session states that you have just modified above, set them
        # all to empty strings in this `elif` section.
    else:
        st.error("Invalid hospital number. Please try again.")

    return


def on_change_intervention(consent_types):

    if "intervention_input" not in st.session_state:
        return

    for intervention in consent_types.data:
        if intervention["type"] == st.session_state.intervention_input:
            # Delete this line of code.
            st.write("An intervention was selected")

            # You are going to use similar code to the previous function. You are
            # going to set the session states for the intervention fields which
            # then will be used to automatically fill in the intervention fields.
            # Update the session states for the intervention to values from the
            # database. We have done the first 3 for you. You need to do the
            # other 2. Uncomment to use this code.

            # st.session_state.intervention_id = intervention["id"]
            # st.session_state.intervention_state = (st.session_state.intervention_input)
            # st.session_state.full_description_state = intervention["full_description"]

            break
    else:
        # Delete this line of code.
        st.write("Intervention deselected")

        # Update all of the sessions states relating to the intervention to
        # empty strings. However, `intervention_id` should be updated to 0.

    return


def user_id_get(users, user_name):
    for user in users.data:
        if user["user_name"] == user_name:
            return user["id"]
    return 0


def main():
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
        on_change=lambda: on_change_hospital_number(
            patients, hospital_numbers
        ),
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=lambda: on_change_intervention(consent_types),
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
            all_fields_filled = all(value != "" for value in fields.values())

            if not all_fields_filled:
                st.error("All fields need to be filled.")
                error_placeholder.error("All fields need to be filled.")
                fields.clear()
                return

            # Remove the else statement (eg 2 lines) below.
            else:
                st.write("All fields in the form are filled")
                fields.clear()

            # THIS IS THE FINAL PUSH!

            # 1. Create a dictionary called `consent_final_data`. Add the values
            # for the keys `patient_id`, `consent_type_id` and `user_id`.
            # HINT: use the `user_id_get()` function for the user_id value.

            # 2. Write to the browser the value of the `consent_final_data`.

            # 3. If the above output to the browser looks good, delete the
            # write to browser line.

            # 4. Now update the "submitted_consents" table with the values of
            # the `consent_final_data` dictionary. Store the return value to a
            # variable called `consent_result`.

            # 5. Write to the browser the value of the `consent_result`.

            # 6. If the above output to the browser looks good, delete the
            # write to browser line.

            # 7. Clear all of the values in the session state
            # HINT: use a `for loop` and `del`. You will need to get each key
            # using `st.session_state.keys()` and also use the list() function
            # to convert the keys to a list.

            # 8. Update the session state submitted_consent_id with the first
            # element of the `consent_update_result` variable (eg element 0)
            # and the key "id".

            # 9. Switch to the page `final_consent_form`.

    return


if __name__ == "__main__":
    initialise()
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
