import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

"""Exercise 1 - Hello World!

Run the app using the command:
    $ streamlit run exercise_1.py

OUTLINE: In this exercise, we are getting you to run a very basic web app
that says "Hello World", one of the essential programs in anyone's coding
education ;o).

NOTES: You will either need to manually reload the webpage after every code change, 
or you can select "Always rerun" from the browser to do so automatically.
If there is an error in your code, you may need to manually refresh in the 
browser after fixing the code.

See https://letsdodigital.org/learn/learn-python/module-2/ to help you if you
get stuck.
"""


def main():
    # Change the title to "Bonjour"
    st.title("Hello")
    # Change the below code to print "Salut le monde!" to the browser
    st.text("Hello World!")

    return


if __name__ == "__main__":
    main()

# Did this work? if so, move on to the next exercise. If not, ask a tutor for
# help.
