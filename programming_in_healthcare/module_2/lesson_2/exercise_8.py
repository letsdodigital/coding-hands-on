import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 8 - List comprehension and updating selectboxes

OUTLINE: OK, so you have lots of fields that you have to manually add data too.
This is time consuming and not using the power of grabbing most of this data
from pre-stored data, for example in database. You are now going to grab data
from the queries you have made of the database queries and then use this data
in your selectboxes.

NOTES: Go look up list comprehension if you are not comfortable with this yet.
"""

def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = execute_query(conn.table("users").select("*"), ttl="10m")

    # Create a list of "user_names" from the users query (list comprehension 
    # might help).

    patients = execute_query(conn.table("patient_demographics").select("*"), ttl="10m")

    consent_types = execute_query(conn.table("consent_types").select("*"), ttl="10m")

    # Create a list called "intervention_types" of "types" found in the 
    # "consent_types" query above.

    st.title("My Digital Consent Form")

    st.header("Patient details")
    st.text_input("Hospital number")
    st.text_input("First name")
    st.text_input("Last name")
    st.date_input("Date of birth", None)
    st.text_input("Email")

    st.header("Intervention")

    # Update the below line to use "intervention_types" (newly created above), 
    # instead of the static list already used below.
    st.selectbox(
        "Intervention", ["", "Below knee amputation", "Cannula"]
    )
    st.text_input("Full description", disabled=True)
    st.text_input("Intended benefits", disabled=True)
    st.text_input("Potential risks", disabled=True)

    st.header("Signature")
    # Update the below line to use "user_names" (newly created above), 
    # instead of the static list already used below
    st.selectbox("Signed off by", ["", "Dr Smith", "Nurse Jones"])

    st.button("Refresh")

    st.header("Users")
    for user in users.data:
        st.write(user)

    st.header("Patients")
    for patient in patients.data:
        st.write(patient)

    st.header("Consent_types")
    for consent_type in consent_types.data:
        st.write(consent_type)
    return


if __name__ == "__main__":
    main()
