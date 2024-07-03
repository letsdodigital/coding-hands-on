import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 2 - Application Process Interface (API) testing

OUTLINE: here we are going to get you to use an API. What is an API? Think of 
this as a means for you to communicate with another computer program running on 
your own computer or even elsewhere over the internet. 

NOTES: Look back at the lecture notes for how to connect to the database for this 
project via its API and also other code you need for displaying things in the web
browser.

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


def main():
    # Initialise a connection to the cloud database

    # Perform a query to get all records from the "users" table

    # Change the title to "API call test"
    st.title("Hello")

    # Create a header named "API test results"

    # Delete the below line
    st.text("Hello World!")

    # Write the results of the above query to the browser using a for loop

    return


if __name__ == "__main__":
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
