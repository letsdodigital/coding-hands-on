"""Lesson 2  - exercise 8 - Finished product!

    All done!

    Warning:
    This is not to be used as a real life medical app! This is for training purposes only.
"""

import streamlit as st


def calculate_egfr(creatinine, age, gender, race):
    """Calculate the Estimated Glomerular Filtration Rate (egfr)

    Calculate the estimated glomerular filtration rate (eGFR) using the CKD-EPI formula.

    Args:
        creatinine (int): Creatinine level
        age (int): Age of patient
        gender (str): "Male" or "Female"
        race (str): "Afro-Caribbean" or "Other"
    Returns:
        int: Estimated glomerular filtration rate (eGFR)

    """
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


def get_ckd_stage(egfr):
    """Get CKD stage

    Determine the stage of chronic kidney disease (CKD) based on estimated glomerular filtration rate (eGFR).

    Args:
        egfr: Estimated glomerular filtration rate (eGFR)

    Returns:
        str: CKD stage
    """
    if egfr > 90:
        return "1"
    elif 60 <= egfr <= 89:
        return "2"
    elif 45 <= egfr <= 59:
        return "3a"
    elif 30 <= egfr <= 44:
        return "3b"
    elif 15 <= egfr <= 29:
        return "4"
    else:
        return "5"


def main():
    """The main Streamlit code

    Runs the Streamlit web app
    """
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
        ckd_stage = get_ckd_stage(egfr)
        st.write(f"CKD stage { ckd_stage }")

    return


if __name__ == "__main__":
    main()

# If you are happy with the above, you can now move onto lesson 4.
