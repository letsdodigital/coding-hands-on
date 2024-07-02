import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query
import datetime

"""Exercise 6 - Add some more fields

OUTLINE: Now we are going to get you to delete some lines of code, change the
title and add some input fields for interventions, this time with two 
selectboxes.
"""


def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = execute_query(conn.table("users").select("*"), ttl="10m")

    # Remove the below code up to "STOP1"
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    test_data = {"test_data": f"Some test data - { current_time }"}

    update_result = execute_query(
        conn.table("test_upload").insert([test_data], count="None")
    )

    test_data_all_data = execute_query(conn.table("test_upload").select("*"), ttl="10m")

    # STOP1 deleting up to here

    # Change the title to "My Digital Consent Form"
    st.title("API call test")

    st.header("Patient details")
    hospital_number = st.text_input("Hospital number")
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    date_of_birth = st.date_input("Date of birth", None)
    patient_email = st.text_input("Email")

    # Create a header named "Intervention"

    # Add a selectbox with the name "Intervention", a few intervention names in a list

    # Create a text field with a name of "Full description"

    # Create a text field with a name of "Intended benefits"

    # Create a text field with a name of "Potential risks"

    # Create a header named "Signature"

    # Add a selectbox with the name "Signed off by" and a few human names in a list

    # Remove the below code up to "STOP2"
    st.header("API test results - users")

    for user in users.data:
        st.write(user)

    st.header("Update return")
    st.write(update_result)

    st.header("Last record of test_data")
    st.write(list(test_data_all_data.data)[-1])

    # STOP2 deleting up to here

    st.button("Refresh")

    return


if __name__ == "__main__":
    main()
