import streamlit as st
from st_supabase_connection import SupabaseConnection

"""Exercise 9 - Time for a proper form and saving of state

OUTLINE: We are going to get you to create some functions. Next we will get you
to create a form that can be submitted and then start the outline of 
functionality needed around these forms. We will also get you to remove some code
that is no longer needed.

NOTES: Look up how to create functions in the lecture notes if you are not
comfortable with them yet. You might need to look up forms as well.
"""

# Create a function called `initialise`, that takes no arguments and returns 
# nothing

# Create a function called `on_change_hospital_number`, which takes no arguments
# and writes to the browser the value of the field created later in this 
# exercise below with the key `hospital_number_input`. Hint, you need to
# use `st.session_state`.

# Create a function called `on_change_intervention`, which takes no arguments
# and writes to the browser the value of field created later in this exercise
# below with the key `intervention_input`.

def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    # Add a text input field for inputting a hospital number. Give it an 
    # appropriate label, a key of "hospital_number_input" and the function to
    # call on change should be `on_change_hospital_number` (created above).

    # Add a selectbox field for intervention selection, much like 
    # `SELECTBOX I` below. This needs an appropriate label, to take a list of 
    # interventions, a key of "intervention_input" and call the function
    # `on_change_intervention` on change (created above).

    # create a form from here up until "END OF FORM" using 
    # `st.form("consent_form"):`
    st.header("Patient details")
    st.text_input("Hospital number")
    st.text_input("First name")
    st.text_input("Last name")
    st.date_input("Date of birth", None)
    st.text_input("Email")

    st.header("Intervention")
    
    # SELECTBOX I: Convert the below line to a "text_input", remove the list 
    # argument and disable the field
    st.selectbox("Intervention", intervention_types)
    st.text_input("Full description", disabled=True)
    st.text_input("Intended benefits", disabled=True)
    st.text_input("Potential risks", disabled=True)

    st.header("Signature")
    st.selectbox("Signed off by", user_names)

    # Convert this to 'form_submit_button' and change the label to "Submit"
    st.button("Refresh")

    # END OF FORM

    # Remove the below code up to "STOP"
    st.header("Users")
    for user in users.data:
        st.write(user)

    st.header("Patients")
    for patient in patients.data:
        st.write(patient)

    st.header("Consent_types")
    for consent_type in consent_types.data:
        st.write(consent_type)

    # STOP deleting here

    return

    # See how the web form works.
    # See what happens when you press submit (probably nothing at the moment)


if __name__ == "__main__":
    main()
