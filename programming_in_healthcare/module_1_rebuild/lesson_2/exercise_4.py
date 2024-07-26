"""Lesson 2 - exercise 4 - You like maths right?

You will be using the below equation for calculating the eGFR:

eGFR = 175 x ((creatinine x 0.011312) ^ (-1.154)) x (age ^ (-0.203))
    x (0.742 if female) x (1.212 if Afro-Caribbean)

Some useful links:

https://pathlabs.rlbuht.nhs.uk/eGFRcalculator.htm
https://www.nhs.uk/conditions/kidney-disease/diagnosis/

Follow the instructions in the comments below.

Gotten stuck, look at the slides at:
https://letsdodigital.org/learn/learn-python/module-1/4-lets-build.html

Warning:
This is not to be used as a real life medical app! This is for training purposes only.
"""

import streamlit as st


def calculate_egfr(creatinine, age, gender, race):
    # Calculate a 'gender_factor' which is 1 for 'Males' and 0.742 for 'Females'
    # If gender is not "Male" or "Female" (python is capitalisation sensitive)
    # then raise an error with:
    # raise ValueError("Your error message")

    # Calculate a 'race_factor' which is 1.212 for 'Afro-Caribbean' and 1 for 'other'
    # If race is not "Afro-Caribbean" or "Other" (python is capitalisation sensitive)
    # then raise an error with:
    # raise ValueError("Your error message")

    # Calculate eGFR using the equation mentioned above
    # Remember to use brackets to ensure the correct order of operations
    # Use * for multiplication and ** for power
    egfr = 0

    # Return egfr as an integer (hint use 'int(variable)')
    return egfr


def main():
    st.title("eGFR calculator")
    creatinine = 110
    age = 55
    gender = "Male"
    race = "Afro-Caribbean"
    egfr = calculate_egfr(creatinine, age, gender, race)
    st.write(f"{ egfr }")
    return


if __name__ == "__main__":
    main()

# Run the above code and make see if a sensible eGFR is displayed in the browser.
# Hopefully you got a result of '73' in the browser for your eGFR.

# If that worked, please move on to exercise 5
