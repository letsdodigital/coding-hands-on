"""Lesson 2 - exercise 7 - Don't forget about the stages!

    Let's build a clinical web app. Some useful links:

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
    if gender == "Male":
        gender_factor = 1
    elif gender == "Female":
        gender_factor = 0.742
    else:
        raise ValueError(
            "Invalid gender. Please specify 'Male' for male or 'Female' for female."
        )

    if race == "Afro-Caribbean":
        race_factor = 1.212
    elif race == "Other":
        race_factor = 1
    else:
        raise ValueError(
            "Invalid race. Please specify 'Afro-Caribbean' or 'other'."
        )

    egfr = (
        175
        * ((creatinine * 0.011312) ** (-1.154))
        * (age ** (-0.203))
        * gender_factor
        * race_factor
    )
    return int(egfr)


# Create a function that takes in the argument eGFR and returns the CKD stage.
# See 'https://www.nhs.uk/conditions/kidney-disease/diagnosis/' for these stages.


def main():
    st.title("eGFR calculator")

    creatinine = st.number_input("Creatinine:", step=1)
    age = st.number_input("Age:", step=1)
    gender = st.selectbox("Gender:", ["", "Male", "Female"])
    race = st.selectbox("Race:", ["", "Afro-Caribbean", "Other"])

    try:
        egfr = calculate_egfr(creatinine, age, gender, race)
    except Exception as e:
        st.write(f"Awaiting appropriate inputs")
    else:
        st.write(f"eGFR: { egfr }")
        # call the ckd stage function and print to the browser the CKD stage.
    return


if __name__ == "__main__":
    main()

# Run the above code and make see if a sensible eGFR is displayed in the browser.

# If that worked, please move on to exercise 8.
