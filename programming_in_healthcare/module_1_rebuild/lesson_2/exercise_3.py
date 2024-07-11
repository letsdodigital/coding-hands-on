"""Lesson 2 - exercise 3

Let's build a clinical web app. Some useful links:

https://pathlabs.rlbuht.nhs.uk/eGFRcalculator.htm
https://www.nhs.uk/conditions/kidney-disease/diagnosis/

Gotten stuck, look at the slides at:
https://letsdodigital.org/learn/learn-python/module-1/4-lets-build.html

Warning:
This is not to be used as a real life medical app! This is for training purposes only.
"""

import streamlit as st


"""Exercise 3 - time for some arguments
1. Follow the steps below
"""


# Add arguments 'creatinine, age, gender, race' to function below
def calculate_egfr():
    egfr = 45
    return  # Return a string with 'creatinine, age, gender, race and egfr'


def main():
    st.title("eGFR calculator")
    # Create variables 'creatinine, age, gender, race' with some initial values.
    # Pass arguments 'creatinine, age, gender, race' to the function call below.
    return_string = calculate_egfr()
    st.write(f"{ return_string }")
    return


if __name__ == "__main__":
    main()

# Run the above code and make see if all 'creatinine, age, gender, race and egfr' are in the browser.

# If that worked, please move on to exercise 4
# You also need to stop streamlit using CTRL / CMD - C
# Remember to change the file name in the command line as well, eg
# $ streamlit run exercise_4.py
