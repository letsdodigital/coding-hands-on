import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 4 - Read what you wrote to the database

OUTLINE: Here you will read back from the database what you wrote to it, print
it to the screen and also add a button.

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = execute_query(conn.table("users").select("*"), ttl="10m")

    test_data = {"test_data": "Some test data"}

    result = execute_query(
        conn.table("test_upload").insert([test_data], count="None")
    )

    # Read the "test_upload" table and store in a variable

    st.title("API call test")

    # Remove this line
    st.header("Update results")

    # Remove this line
    st.write(update_result)

    st.header("API test results - users")

    for user in users.data:
        st.write(user)

    # Make a header named "Update return"

    # Write to browser the results of the database update

    # Make a header named "Last record of test_data"

    # Write to browser the last record in "test_data" data you received

    # Create a button to refresh the screen

    return


if __name__ == "__main__":
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
