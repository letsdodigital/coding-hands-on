import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query
import datetime

"""Exercise 5 - Create some input fields

OUTLINE: Now you will create some input fields for patient demographics.

NOTES: You will need to create a date field for date of birth (obvious, but
worth noting).

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = execute_query(conn.table("users").select("*"), ttl="10m")

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    test_data = {"test_data": f"Some test data - { current_time }"}

    update_result = execute_query(
        conn.table("test_upload").insert([test_data], count="None")
    )

    test_data_all_data = execute_query(
        conn.table("test_upload").select("*"), ttl="10m"
    )

    # Change the title to "My Digital Consent Form"
    st.title("API call test")

    # Create a header named "Patient details"

    # Create a text_input field with a label of "Hospital number"

    # Create a text_input field with a label of "First name"

    # Create a text_input field with a label of "Last name"

    # Create a date_input field with a label of "Date of birth"

    # Create a text_input field with a label of "Email"

    st.header("API test results - users")

    for user in users.data:
        st.write(user)

    st.header("Update return")
    st.write(update_result)

    st.header("Last record of test_data")
    st.write(list(test_data_all_data.data)[-1])

    st.button("Refresh")

    return


if __name__ == "__main__":
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
