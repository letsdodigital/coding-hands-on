import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 3 - Write to the database

OUTLINE: So you have read some data from the database in the cloud, now it is
time for you to write some data to the database.

NOTES: Use the datetime library to add a date and time string to your data if you
like.

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = execute_query(conn.table("users").select("*"), ttl="10m")

    # Create a dictionary called "test_data" with a key of "test_data",
    # and any value you like. If you add the time including seconds you
    # can see updated values better later in these exercises.

    # Update the database with the data in the "test_data" dictionary

    st.title("API call test")

    st.header("API test results - users")

    for user in users.data:
        st.write(user)

    return


if __name__ == "__main__":
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
