"""Lesson 2 - exercise 5 - Time for some input!

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


def main():
    st.title("eGFR calculator")

    # Convert 'creatinine and age' into input fields for the web browser.
    # Hint: use 'variable_name = st.number_input("Label name:", step=1)'.

    creatinine = 110
    age = 55

    # Convert 'gender and race' into selection fields for the web browser.
    # Hint: use 'variable_name = st.selectbox("Label name:", ["", "option 1", "option 2"])'.

    gender = "Male"
    race = "Afro-Caribbean"
    egfr = calculate_egfr(creatinine, age, gender, race)
    st.write(f"{ egfr }")

    return


if __name__ == "__main__":
    main()

# Run the above code and make see if a sensible eGFR is displayed in the browser
# after entering some data. If you get errors in the terminal and the browser for
# certain data entered, do not worry, we will fix these in the next exercise.

# If that worked, please move on to exercise 6.
