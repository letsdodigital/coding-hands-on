"""Lesson 2 - exercise 1 - 'Hello world!' web app style!

    Let's build a clinical web app. Some useful links:

    https://pathlabs.rlbuht.nhs.uk/eGFRcalculator.htm
    https://www.nhs.uk/conditions/kidney-disease/diagnosis/

    Run the app using the command:
    
    $ streamlit run exercise_1.py

    Gotten stuck, look at the slides at:
    https://letsdodigital.org/learn/learn-python/module-1/4-lets-build.html

    Warning:
    This is not to be used as a real life medical app! This is for training purposes only.
"""

import streamlit as st


def main():
    st.title("My first web app")
    st.write("Hello world!")
    return


if __name__ == "__main__":
    main()

# If that worked, please move on to exercise 2
# You also need to stop streamlit using CTRL / CMD - C
# Remember to change the file name in the command line as well, eg
# $ streamlit run exercise_2.py
