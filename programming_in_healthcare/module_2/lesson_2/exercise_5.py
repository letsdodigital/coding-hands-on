import streamlit as st
from st_supabase_connection import SupabaseConnection
import datetime

"""Exercise 5 - Create some input fields

OUTLINE: Now you will create some input fields for patient demographics.

NOTES: You will need to create a date field for date of birth (obvious, but
worth noting).
"""

def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    test_data = {"test_data": f"Some test data - { current_time }"}

    update_result = (
        conn.table("test_upload").insert([test_data], count="None").execute()
    )

    test_data_all_data = conn.query(
        "*", table="test_upload", ttl="10m"
    ).execute()

    # Change the title to "My Digital Consent Form"
    st.title("API call test")

    # Create a header named "Patient details"

    # Create a text field with a name of "Hospital number"

    # Create a text field with a name of "First name"

    # Create a text field with a name of "Last name"

    # Create a DATE field with a name of "Date of birth"

    # Create a text field with a name of "Email"

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
