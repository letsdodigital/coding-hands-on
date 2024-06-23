"""Lesson 3

Let's build a clinical web app. Some useful links:

https://pathlabs.rlbuht.nhs.uk/eGFRcalculator.htm
https://www.nhs.uk/conditions/kidney-disease/diagnosis/

Gotten stuck, look at the slides at:
https://letsdodigital.org/learn/learn-python/module-1/

Warning:
This is not to be used as a real life medical app! This is for training purposes only.
"""

import streamlit as st

"""Exercise 1 - 'Hello world!' web app style!
Run the app using the command:
$ streamlit run app.py
"""


def main():
    st.title("My first web app")
    st.write("Hello world!")
    return


if __name__ == "__main__":
    main()

"""Exercise 2 - Creating your first function
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""
# Write a function named 'calculate_egfr'.
# Define a variable in this function called egfr and set it to '45'.
# Have this function return egfr.


def main():
    # Call the 'calculate_egfr' function above
    # Print the returned value to the browser
    return


if __name__ == "__main__":
    main()

# Run the above code and see if you have the number 45 in the browser window
"""

"""Exercise 3 - time for some arguments
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""
# Add arguements 'creatinine, age, gender, race' to function below
def calculate_egfr():
    egfr = 45
    return  # Return a string with 'creatinine, age, gender, race and egfr'


def main():
    st.title("eGFR calculator")
    # Create variables 'creatinine, age, gender, race' with some initial values.
    # Pass arguements 'creatinine, age, gender, race' to the function call below.
    return_string = calculate_egfr()
    st.write(f"{ return_string }")
    return


if __name__ == "__main__":
    main()

# Run the above code and make see if all 'creatinine, age, gender, race and egfr' are in the browser.

"""


"""Exercise 4 - you like maths right?
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

You will be using the below equation for calculating the eGFR:

eGFR = 175 * ((creatinine × 0.011312) ^ (-1.154)) x (age ^ (-0.203))
       x (0.742 if female) x (1.212 if Afro-Caribbean)
"""

"""
def calculate_egfr(creatinine, age, gender, race):
    # Calculate a 'gender_factor' which is 1 for 'Males' and 0.742 for 'Females'
    # If gender is not "Male" or "Female" (python is capitalisation sensitive)
    # then raise an error with:
    # raise ValueError ("Your error message")

    # Calculate a 'race_factor' which is 1.212 for 'Afro-Caribbean' and 1 for 'other'
    # If race is not "Afro-Caribbean" or "other" (python is capitalisation sensitive)
    # then raise an error with:
    # raise ValueError ("Your error message")

    # Calculate eGFR using the equation mentioned above
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
"""

"""Exercise 5 - time for some input!
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""
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
    elif race == "other":
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
    # Hint: use 'variable_name = st.number_input("Display name:", step=1)'.
    creatinine = 110
    age = 55
    # Convert 'gender and race' into selection fields for the web browser.
    # Hint: use 'variable_name = st.selectbox("Display name:", ["", "option 1", "option 2"])'.
    gender = "Male"
    race = "Afro-Caribbean"
    egfr = calculate_egfr(creatinine, age, gender, race)
    st.write(f"{ egfr }")
    return


if __name__ == "__main__":
    main()

# Run the above code and make see if a sensible eGFR is displayed in the browser 
# after entering some data. If you get errors in the terminal and the browser, do
# not worry, we will fix these in the next exercise.
"""

"""Exercise 6 - errors, you should sort them out!
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""
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
    elif race == "other":
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

    creatinine = st.number_input("Creatinine:", step=1)
    age = st.number_input("Age:", step=1)
    gender = st.selectbox("Gender:", ["", "Male", "Female"])
    race = st.selectbox("Race:", ["", "Afro-Caribbean", "other"])

    # You now need to handle the exceptions caused by erroneous input variables,
    # eg 'creatinine, age, gender, race'.
    # You do this with the 'try, except, else' exception handlers.
    # With the except clause, you should display an appropriate message to the
    # Browser.
    egfr = calculate_egfr(creatinine, age, gender, race)
    st.write(f"{ egfr }")
    return


if __name__ == "__main__":
    main()

# Run the above code and make see if a sensible eGFR is displayed in the browser.
# Make sure an appropriate message is displayed if the input data is erroneous.
"""

"""Exercise 7 - don't forget about the stages!
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""
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
    elif race == "other":
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
    race = st.selectbox("Race:", ["", "Afro-Caribbean", "other"])

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
"""

"""Exercise 8 - finished product!
1. Comment out the above code.
2. Uncomment the code below.
3. Below is the final app in working form with added docstring comments.
"""

'''
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
    elif race == "other":
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
    race = st.selectbox("Race:", ["", "Afro-Caribbean", "other"])

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
'''
