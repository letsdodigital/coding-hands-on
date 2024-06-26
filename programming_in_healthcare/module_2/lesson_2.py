"""Lesson 2

Here you get to build a digital consent app
"""

import streamlit as st
from st_supabase_connection import SupabaseConnection


"""Exercise 1 - Hello World!
Run the app using the command:
    $ streamlit run lesson_2.py

OUTLINE: In this exercise, we are getting you to run a very basic web app
that says "Hello World", one of the essential programs in anyone's coding
education ;o).

NOTES: You will either need to manually reload the webpage after every code change, 
or you can select "Always rerun" from the browser to do so automatically.
If there is an error in your code, you will need to manually refresh in the 
browser after fixing the code.
"""


def main():
    st.title("Hello")
    st.text("Hello World!")

    return


if __name__ == "__main__":
    main()

# Did this work? if so, move on to the next exercise. If not, as a tutor for
# help.


"""Exercise 2 - Application Process Interface (API) testing
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: here we are going to get you to use an API. What is an API? Think of
as a means for you to communicate with another computer program running on your
own computer or even elsewhere over the internet. 

NOTES: Look back at the lecture notes for how to connect to the database for this 
project via its API and also other code you need for displaying things in the web
browser.
"""

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
"""

"""Exercise 3 - Write to the database
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: So you have read some data from the database in the cloud, now it is
time for you to write some data to the database.

NOTES: Use the datetime library to add a date and time string to your data if you
like
"""

"""
def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

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
"""

"""Exercise 4 - Read what you wrote to the database
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: Here you will read back from the database what you wrote to it, print
it to the screen and also add a button.
"""

"""
def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    test_data = {"test_data": "Some test data"}

    result = (
        conn.table("test_upload").insert([test_data], count="None").execute()
    )

    # Read the "test_upload" table and store in a variable

    st.title("API call test")

    st.header("API test results - users")

    for user in users.data:
        st.write(user)

    # Make a header named "Update return"

    # Write to browser the results of the database update

    # Make a header named "Last record of test_data"

    # Write to browser the last record in "test_data" data you received

    # Create a button to refresh the screen

    return


if __name__ == "__main__":
    main()
"""

"""Exercise 5 - Create some input fields
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: Now you will create some input fields for patient demographics.

NOTES: You will need to create a date field for date of birth (obvious, but
worth noting).
"""

"""
import datetime


def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    test_data = {"test_data": f"Some test data - { current_time }"}

    update_result = (
        conn.table("test_upload").insert([test_data], count="None").execute()
    )

    test_data_all_data = conn.query(
        "*", table="test_upload", ttl="10m"
    ).execute()

    # Change the title to "My Digital Consent Form"
    st.title("API call test")

    # Create a header named "Patient details"

    # Create a text field with a name of "Hospital number"

    # Create a text field with a name of "First name"

    # Create a text field with a name of "Last name"

    # Create a DATE field with a name of "Date of birth"

    # Create a text field with a name of "Email"

    st.header("API test results - users")

    for user in users.data:
        st.write(user)

    st.header("Update return")
    st.write(update_result)

    st.header("Last record of test_data")
    st.write(list(test_data_all_data.data)[-1])

    st.button("Refresh")

    return


if __name__ == "__main__":
    main()
"""

"""Exercise 6 - Add some more fields
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: Now we are going to get you to delete some lines of code, change the
title and add some input fields for interventions, this time with two 
selectboxes.
"""

"""
import datetime

def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    # Remove the below code up to "STOP1"
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    test_data = {"test_data": f"Some test data - { current_time }"}

    update_result = (
        conn.table("test_upload").insert([test_data], count="None").execute()
    )

    test_data_all_data = conn.query(
        "*", table="test_upload", ttl="10m"
    ).execute()

    # STOP1 deleting up to here

    # Change the title to "My Digital Consent Form"
    st.title("API call test")

    st.header("Patient details")
    hospital_number = st.text_input("Hospital number")
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    date_of_birth = st.date_input("Date of birth", None)
    patient_email = st.text_input("Email")

    # Create a header named "Intervention"

    # Add a selectbox with the name "Intervention", a few intervention names in a list

    # Create a text field with a name of "Full description"

    # Create a text field with a name of "Intended benefits"

    # Create a text field with a name of "Potential risks"

    # Create a header named "Signature"

    # Add a selectbox with the name "Signed off by" and a few human names in a list

    # Remove the below code up to "STOP2"
    st.header("API test results - users")

    for user in users.data:
        st.write(user)

    st.header("Update return")
    st.write(update_result)

    st.header("Last record of test_data")
    st.write(list(test_data_all_data.data)[-1])

    # STOP2 deleting up to here

    st.button("Refresh")

    return


if __name__ == "__main__":
    main()
"""

"""Exercise 7 - Getting data from other tables
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: So, you need data from more than one database table to successfully 
create your consent form and submit it. We will now get you to query the
`patients` and `consent_types` tables and output the results to the browser.
"""

"""
def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    # Perform a query to get all records from the "patients" table

    # Perform a query to get all records from the "consent_types" table

    st.title("My Digital Consent Form")

    st.header("Patient details")
    st.text_input("Hospital number")
    st.text_input("First name")
    st.text_input("Last name")
    st.date_input("Date of birth", None)
    st.text_input("Email")

    st.header("Intervention")
    st.selectbox(
        "Intervention", ["", "Below knee amputation", "Cannula"]
    )
    st.text_input("Full description")
    st.text_input("Intended benefits")
    st.text_input("Potential risks")

    st.header("Signature")
    st.selectbox("Signed off by", ["", "Dr Smith", "Nurse Jones"])

    st.button("Refresh")

    # Create a header named "Users"

    # Write all users to the browser

    # Create a header named "Patients"

    # Write all patients to the browser

    # Create a header named "Consent types"

    # Write all consent_types to the browser

    return


if __name__ == "__main__":
    main()
"""

"""Exercise 8 - List comprehension and updating selectboxes
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: OK, so you have lots of fields that you have to manually add data too.
This is time consuming and not using the power of grabbing most of this data
from pre-stored data, for example in database. You are now going to grab data
from the queries you have made of the database queries and then use this data
in your selectboxes.

NOTES: Go look up list comprehension if you are not comfortable with this yet.
"""

"""
def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    # Create a list of "user_names" from the users query (list comprehension 
    # might help).

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()  

    # Create a list called "intervention_types" of "types" found in the 
    # "consent_types" query above.

    st.title("My Digital Consent Form")

    st.header("Patient details")
    st.text_input("Hospital number")
    st.text_input("First name")
    st.text_input("Last name")
    st.date_input("Date of birth", None)
    st.text_input("Email")

    st.header("Intervention")

    # Update the below line to use "intervention_types" (newly created above), 
    # instead of the static list already used below.
    st.selectbox(
        "Intervention", ["", "Below knee amputation", "Cannula"]
    )
    st.text_input("Full description", disabled=True)
    st.text_input("Intended benefits", disabled=True)
    st.text_input("Potential risks", disabled=True)

    st.header("Signature")
    # Update the below line to use "user_names" (newly created above), 
    # instead of the static list already used below
    st.selectbox("Signed off by", ["", "Dr Smith", "Nurse Jones"])

    st.button("Refresh")

    st.header("Users")
    for user in users.data:
        st.write(user)

    st.header("Patients")
    for patient in patients.data:
        st.write(patient)

    st.header("Consent_types")
    for consent_type in consent_types.data:
        st.write(consent_type)
    return


if __name__ == "__main__":
    main()
"""

"""Exercise 9 - Time for a proper form and saving of state
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: We are going to get you to create some functions. Next we will get you
to create a form that can be submitted and then start the outline of 
functionality needed around these forms. We will also get you to remove some code
that is no longer needed.

NOTES: Look up how to create functions in the lecture notes if you are not
comfortable with them yet. You might need to look up forms as well.
"""

"""
# Create a function called `initialise`, that takes no arguments and returns 
# nothing

# Create a function called `on_change_hospital_number`, which takes no arguments
# and writes to the browser the value of the field created later in this 
# exercise below with the key `hospital_number_input`. Hint, you need to
# use `st.session_state`.

# Create a function called `on_change_intervention`, which takes no arguments
# and writes to the browser the value of field created later in this exercise
# below with the key `intervention_input`.

def main():
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    # Add a text input field for inputting a hospital number. Give it an 
    # appropriate label, a key of "hospital_number_input" and the function to
    # call on change should be `on_change_hospital_number` (created above).

    # Add a selectbox field for intervention selection, much like 
    # `SELECTBOX I` below. This needs an appropriate label, to take a list of 
    # interventions, a key of "intervention_input" and call the function
    # `on_change_intervention` on change (created above).

    # create a form from here up until "END OF FORM" using 
    # `st.form("consent_form"):`
    st.header("Patient details")
    st.text_input("Hospital number")
    st.text_input("First name")
    st.text_input("Last name")
    st.date_input("Date of birth", None)
    st.text_input("Email")

    st.header("Intervention")
    
    # SELECTBOX I: Convert the below line to a "text_input", remove the list 
    # argument and disable the field
    st.selectbox("Intervention", intervention_types)
    st.text_input("Full description", disabled=True)
    st.text_input("Intended benefits", disabled=True)
    st.text_input("Potential risks", disabled=True)

    st.header("Signature")
    st.selectbox("Signed off by", user_names)

    # Convert this to 'form_submit_button' and change the label to "Submit"
    st.button("Refresh")

    # END OF FORM

    # Remove the below code up to "STOP"
    st.header("Users")
    for user in users.data:
        st.write(user)

    st.header("Patients")
    for patient in patients.data:
        st.write(patient)

    st.header("Consent_types")
    for consent_type in consent_types.data:
        st.write(consent_type)

    # STOP deleting here

    return

    # See how the web form works.
    # See what happens when you press submit (probably nothing at the moment)


if __name__ == "__main__":
    main()
"""


"""Exercise 10 - A reward!
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

NOTES: So you have worked hard to get to this point, so we thought you could do
with a little reward. We have done most of the work for you in this next section.
Have a look at what we did. We added a new dictionary (can you find its name?) 
and added something to the input fields. All you need to add is some code to 
check that the button has been pressed.
"""

"""
def initialise():
    return


def on_change_hospital_number():
    st.write(
        f"Hospital number changed to: { st.session_state.hospital_number_input }"
    )

    return


def on_change_intervention():
    st.write(
        f"Intervention changed to: { st.session_state.intervention_input }"
    )

    return


def main():
    # We have added this here for you
    fields = {}
    
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    st.text_input(
        'Hospital number (eg "HN001")',
        key="hospital_number_input",
        on_change=on_change_hospital_number,
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=on_change_intervention,
    )

    with st.form("consent_form"):
        st.header("Patient details")
        # We have added the `field` dictionary with keys here for you.
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )
        fields["first_name"] = st.text_input("First name")
        fields["last_name"] = st.text_input("Last name")
        fields["date_of_birth"] = st.date_input("Date of birth", None)
        fields["patient_email"] = st.text_input("Email")

        st.header("Intervention")
        fields["intervention"] = st.text_input("Intervention", disabled=True)
        fields["full_description"] = st.text_input("Full description", disabled=True)
        fields["intended_benefits"] = st.text_input("Intended benefits", disabled=True)
        fields["potential_risks"] = st.text_input("Potential risks", disabled=True)

        st.header("Signature")

        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        # Test if submitted is true and then write to the browser
        # "Button pressed"

    return


if __name__ == "__main__":
    # Add a call to the `initialise` function
    main()
"""

"""Exercise 11 - It is a question of state
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

NOTES: So now you are going to add a lot of code to manage state. Start at the
line START HERE. After that, go back to the beginning and carry out the rest of
the tasks required.
"""

"""
def initialise():
    # We added this line for you
    initialise_state = "test_data"

    # Now you need to initialise all of your state keys, checking if they have 
    # been initialised already. We have done the first one for you.
    if "intervention_state" not in st.session_state:
        st.session_state.intervention_state = initialise_state
    return


def on_change_hospital_number():
    st.write(
        f"Hospital number changed to: { st.session_state.hospital_number_input }"
    )

    return


def on_change_intervention():
    st.write(
        f"Intervention changed to: { st.session_state.intervention_input }"
    )

    return


def main():
    fields = {}
    
    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    # Get a list of valid hospital numbers from the patients.data
    # variable. Call the resulting list `hospital_numbers`.

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    st.text_input(
        'Hospital number (eg "HN001")',
        key="hospital_number_input",
        on_change=on_change_hospital_number,
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=on_change_intervention,
    )

    with st.form("consent_form"):
        st.header("Patient details")

        # START HERE
        # To each input field (EXCEPT the "Signed off by" field) add the second
        # argument, which is `value`, as a session state variable. This should 
        # match the key in the field dictionary, but with a suffix of "_state".
        # Please also disable the field. We have already done all of the changes
        # for the first field "hospital_number" below. Complete for the rest.
        
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )

        fields["first_name"] = st.text_input("First name")
        fields["last_name"] = st.text_input("Last name")
        # Also convert this line from date to text
        fields["date_of_birth"] = st.date_input("Date of birth", None)
        fields["patient_email"] = st.text_input("Email")

        st.header("Intervention")
        fields["intervention"] = st.text_input("Intervention", disabled=True)
        fields["full_description"] = st.text_input("Full description", disabled=True)
        fields["intended_benefits"] = st.text_input("Intended benefits", disabled=True)
        fields["potential_risks"] = st.text_input("Potential risks", disabled=True)

        st.header("Signature")

        # DO NOT alter this field
        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write("Button pressed")

    return


if __name__ == "__main__":
    # Add a call to the `initialise` function
    main()
"""

"""Exercise 12 - Updating functions and managing the submit button
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: We are now going to get you to bulk out the functions you have already
written and then write a new one. We are also going to get you to check that 
all fo the fields within the form (there will be a black thin border around 
these fields) are all filled with data.
"""

"""
# Initialise the global lists `consent_types`, `hospital_numbers` and `patients`


def initialise():
    # Add a global call to `consent_types`

    initialise_state = "test_data"

    # Initialise a session state called `submitted_consent_id` to 0. You do NOT
    # need to check if it exists already as this needs to reset every time the
    # script runs.

    # Add a session state called `patient_id` and initialise to 0. This DOES
    # need to be checked to see if it exists already.

    if "hospital_number_state" not in st.session_state:
        st.session_state.hospital_number_state = initialise_state
    if "first_name_state" not in st.session_state:
        st.session_state.first_name_state = initialise_state
    if "last_name_state" not in st.session_state:
        st.session_state.last_name_state = initialise_state
    if "date_of_birth_state" not in st.session_state:
        st.session_state.date_of_birth_state = initialise_state
    if "patient_email_state" not in st.session_state:
        st.session_state.patient_email_state = initialise_state

    # Add a session state called `intervention_id` and initialise to 0. This
    # DOES need to be checked to see if it exists already.

    if "intervention_state" not in st.session_state:
        st.session_state.intervention_state = initialise_state
    if "full_description_state" not in st.session_state:
        st.session_state.full_description_state = initialise_state
    if "intended_benefits_state" not in st.session_state:
        st.session_state.intended_benefits_state = initialise_state
    if "potential_risks_state" not in st.session_state:
        st.session_state.potential_risks_state = initialise_state

    # Start another connection to the database

    # Query the `consent_types` table and store the results in the
    # `consent_types` list.

    return


def on_change_hospital_number():
    # Delete this line of code
    st.write(
        f"Hospital number changed to: { st.session_state.hospital_number_input }"
    )

    # Create a variable called `hospital_number_input` and initialise it with
    # the value of the session state `hospital_number_input`.

    # Now create some conditional code. Firstly, check if the value of
    # `hospital_number_input` is inside the list `hospital_numbers`. Write to
    # the browser "Valid hospital number" if the hospital number is valid.

    # Use `elif` to check if `hospital_number_input` is an empty string (eg
    # ""). Write to the browser "empty hospital number field" if this is true.

    # Use an "else" statement that writes to the browser an error message
    # (using `st.error`) that the hospital number is not valid.

    return


def on_change_intervention():
    # Delete this line of code
    st.write(
        f"Intervention changed to: { st.session_state.intervention_input }"
    )

    # Create a `for loop`. This needs to loop through `consent_types.data` and
    # have a loop variable called `intervention`.

    # Within the above `for loop`, add an `if` statement, checking if the key
    # "type" inside the dictionary `intervention` is equal to the session state
    # `intervention_input`. If the `if` statement is true, write to the
    # browser "An intervention was selected". Add a `break` after this to stop
    # looping through the for loop further.

    # Add a `else` statement, associated with the for loop, that writes to the
    # browser "Intervention deselected".

    return


# 1. Create another function called `user_id_get`. Now this function takes two
# arguments, the first `users` and the second `user_name`.
# 2. This function should loop over `users.data` with the loop variable being
# `user`.
# 3. Within this loop, check if the key "user_name" in the dictionary `user` is
# equal to `user_name`.
# 4. If this last statement is true, return `user["id"]`.
# 5. The last line of code for the function, outside of the for loop needs to
# return 0.


def main():
    # add a global statement for `hospital_numbers` and `patients`

    # We added this placeholder to display errors messages that we have
    # raise later.
    error_placeholder = st.empty()

    fields = {}

    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    hospital_numbers = [
        patient["hospital_number"]
        for patient in patients.data
        if "hospital_number" in patient
    ]

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    st.text_input(
        'Hospital number (eg "HN001")',
        key="hospital_number_input",
        on_change=on_change_hospital_number,
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=on_change_intervention,
    )

    with st.form("consent_form"):
        st.header("Patient details")
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )
        fields["first_name"] = st.text_input(
            "First name", st.session_state.first_name_state, disabled=True
        )
        fields["last_name"] = st.text_input(
            "Last name", st.session_state.last_name_state, disabled=True
        )
        fields["date_of_birth"] = st.text_input(
            "Date of birth",
            st.session_state.date_of_birth_state,
            disabled=True,
        )
        fields["patient_email"] = st.text_input(
            "Email", st.session_state.patient_email_state, disabled=True
        )

        st.header("Intervention")
        fields["intervention"] = st.text_input(
            "Intervention", st.session_state.intervention_state, disabled=True
        )
        fields["full_description"] = st.text_input(
            "Full description",
            st.session_state.full_description_state,
            disabled=True,
        )
        fields["intended_benefits"] = st.text_input(
            "Intended benefits",
            st.session_state.intended_benefits_state,
            disabled=True,
        )
        fields["potential_risks"] = st.text_input(
            "Potential risks",
            st.session_state.potential_risks_state,
            disabled=True,
        )

        st.header("Signature")
        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        if submitted:
            # Remove this line
            st.write("Button pressed")

            # 1. Use an `all` statement to check if all the field dictionary
            # values are not empty. This should pass as `initialise_state =
            # "test_data"` (see the initialisation function above).
            # 2. You can check what happens by changing `initialise_state` to
            # an empty string, eg "".
            # 3. Use the `all` statement to store the result in a variable
            # called `all_fields_filled` and then use an `if` statement to check
            # this variable.
            # 4. If all of the fields are not filled, use `st.error`
            # and `error_placeholder.error` (which links to the placeholder at
            # the beginning of the main function) to display error messages.
            # 5. Use a `return` to end the main function if not all of the
            # fields are filled.
            # 6. If all the fields are filled, write to the browser something
            # positive.

    return


if __name__ == "__main__":
    initialise()
    main()
"""

"""Exercise 13 - Adding more code to `on_change` and `submitted`
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below

OUTLINE: This is the final push of code. We are going to get you to do several 
steps in this exercise, so watch your step.
"""

"""
consent_types = []
hospital_numbers = []
patients = []


def initialise():
    global consent_types

    # initialise this to an empty string
    initialise_state = "test_data"

    st.session_state.submitted_consent_id = 0

    if "patient_id" not in st.session_state:
        st.session_state.patient_id = 0
    if "hospital_number_state" not in st.session_state:
        st.session_state.hospital_number_state = initialise_state
    if "first_name_state" not in st.session_state:
        st.session_state.first_name_state = initialise_state
    if "last_name_state" not in st.session_state:
        st.session_state.last_name_state = initialise_state
    if "date_of_birth_state" not in st.session_state:
        st.session_state.date_of_birth_state = initialise_state
    if "patient_email_state" not in st.session_state:
        st.session_state.patient_email_state = initialise_state
    if "intervention_id" not in st.session_state:
        st.session_state.intervention_id = 0
    if "intervention_state" not in st.session_state:
        st.session_state.intervention_state = initialise_state
    if "full_description_state" not in st.session_state:
        st.session_state.full_description_state = initialise_state
    if "intended_benefits_state" not in st.session_state:
        st.session_state.intended_benefits_state = initialise_state
    if "potential_risks_state" not in st.session_state:
        st.session_state.potential_risks_state = initialise_state

    conn = st.connection("supabase", type=SupabaseConnection)
    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    return


def on_change_hospital_number():
    hospital_number_input = st.session_state.hospital_number_input
    if hospital_number_input in hospital_numbers:
        # Delete this line of code
        st.write("Valid hospital number")

        # 1. Use a `for` loop to loop through `patients.data` and have a loop
        # variable of `patient`.
        # 2. Within this loop, check if the key "hospital_number" of the
        # dictionary `patient` is equal to `hospital_number_input`.
        # 3. If the above is true, then set the session states relating to the
        # patient demographics to the values in found in the database. We have
        # done the first 3 for you. You will need to do the other 3. Uncomment
        # to use them.

        # st.session_state.patient_id = patient["id"]
        # st.session_state.hospital_number_state = hospital_number_input
        # st.session_state.first_name_state = patient["first_name"]

        # Add a break here.

    elif hospital_number_input == "":
        # Delete this line of code
        st.write("empty hospital number field")

        # Of all the session states that you have used modified above, set them
        # all to empty strings in this `elif` section.
    else:
        st.error("Invalid hospital number. Please try again.")

    return


def on_change_intervention():
    for intervention in consent_types.data:
        if intervention["type"] == st.session_state.intervention_input:
            # Delete this line of code.
            st.write("An intervention was selected")

            # You are going to use similar code to the previous function.
            # Update the session states for the intervention to values from the
            # data base. We have done the first 3 for you. You need to do the
            # other 2. Uncomment to use this code.

                # st.session_state.intervention_id = intervention["id"]
                # st.session_state.intervention_state = (st.session_state.intervention_input)
                # st.session_state.full_description_state = intervention["full_description"]

            break
    else:
        # Delete this line of code.
        st.write("Intervention deselected")

        # Update all of the sessions states relating to the intervention to
        # empty strings. However, `intervention_id` should be updated to 0.

    return


def user_id_get(users, user_name):
    for user in users.data:
        if user["user_name"] == user_name:
            return user["id"]
    return 0


def main():
    global hospital_numbers, patients

    error_placeholder = st.empty()

    fields = {}

    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    hospital_numbers = [
        patient["hospital_number"]
        for patient in patients.data
        if "hospital_number" in patient
    ]

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    st.text_input(
        'Hospital number (eg "HN001")',
        key="hospital_number_input",
        on_change=on_change_hospital_number,
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=on_change_intervention,
    )

    with st.form("consent_form"):
        st.header("Patient details")
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )
        fields["first_name"] = st.text_input(
            "First name", st.session_state.first_name_state, disabled=True
        )
        fields["last_name"] = st.text_input(
            "Last name", st.session_state.last_name_state, disabled=True
        )
        fields["date_of_birth"] = st.text_input(
            "Date of birth",
            st.session_state.date_of_birth_state,
            disabled=True,
        )
        fields["patient_email"] = st.text_input(
            "Email", st.session_state.patient_email_state, disabled=True
        )

        st.header("Intervention")
        fields["intervention"] = st.text_input(
            "Intervention",
            st.session_state.intervention_state,
            disabled=True,
        )
        fields["full_description"] = st.text_area(
            "Full description",
            st.session_state.full_description_state,
            disabled=True,
        )
        fields["intended_benefits"] = st.text_area(
            "Intended benefits",
            st.session_state.intended_benefits_state,
            disabled=True,
        )
        fields["potential_risks"] = st.text_area(
            "Potential risks",
            st.session_state.potential_risks_state,
            disabled=True,
        )

        st.header("Signature")
        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        if submitted:
            all_fields_filled = all(value for value in fields.values())

            if not all_fields_filled:
                st.error("All fields need to be filled.")
                error_placeholder.error("All fields need to be filled.")
                return

            # Remove the else statement (eg 2 lines) below.
            else:
                st.write("All fields in the forma are filled")

            # THIS IS THE FINAL PUSH!

            # 1. Create a dictionary called `consent_final_data`. Add the values
            # for the keys `patient_id`, `consent_type_id` and `user_id`.
            # HINT: use the `user_id_get()` function for the user_id value.

            # 2. Write to the browser the value of the `consent_final_data`.

            # 3. If the above output to the browser looks good, delete the
            # write to browser line.

            # 4. Now update the "submitted_consents" table with the values of
            # the `consent_final_data` dictionary. Store the return value to a
            # variable called `result`.

            # 5. Clear all of the values in the session state
            # HINT: use a `for loop` and `del`.

            # 6. Update the session state submitted_consent_id with the first element of the result variable (eg element 0) and the key "id".

            # 7. Switch to the page `final_consent_form`.

    return


if __name__ == "__main__":
    initialise()
    main()
"""

"""Exercise 14 - 
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""
consent_types = []
hospital_numbers = []
patients = []


def initialise():
    global consent_types

    initialise_state = ""

    st.session_state.submitted_consent_id = 0

    if "patient_id" not in st.session_state:
        st.session_state.patient_id = 0
    if "hospital_number_state" not in st.session_state:
        st.session_state.hospital_number_state = initialise_state
    if "first_name_state" not in st.session_state:
        st.session_state.first_name_state = initialise_state
    if "last_name_state" not in st.session_state:
        st.session_state.last_name_state = initialise_state
    if "date_of_birth_state" not in st.session_state:
        st.session_state.date_of_birth_state = initialise_state
    if "patient_email_state" not in st.session_state:
        st.session_state.patient_email_state = initialise_state
    if "intervention_id" not in st.session_state:
        st.session_state.intervention_id = 0
    if "intervention_state" not in st.session_state:
        st.session_state.intervention_state = initialise_state
    if "full_description_state" not in st.session_state:
        st.session_state.full_description_state = initialise_state
    if "intended_benefits_state" not in st.session_state:
        st.session_state.intended_benefits_state = initialise_state
    if "potential_risks_state" not in st.session_state:
        st.session_state.potential_risks_state = initialise_state

    conn = st.connection("supabase", type=SupabaseConnection)
    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    return


def on_change_hospital_number():
    hospital_number_input = st.session_state.hospital_number_input
    if hospital_number_input in hospital_numbers:
        for patient in patients.data:
            if patient["hospital_number"] == hospital_number_input:
                st.session_state.patient_id = patient["id"]
                st.session_state.hospital_number_state = hospital_number_input
                st.session_state.first_name_state = patient["first_name"]
                st.session_state.last_name_state = patient["last_name"]
                st.session_state.date_of_birth_state = patient["date_of_birth"]
                st.session_state.patient_email_state = patient["email"]
                break
    elif hospital_number_input == "":
        st.session_state.patient_id = ""
        st.session_state.hospital_number_state = ""
        st.session_state.first_name_state = ""
        st.session_state.last_name_state = ""
        st.session_state.date_of_birth_state = ""
        st.session_state.patient_email_state = ""
    else:
        st.error("Invalid hospital number. Please try again.")

    return


def on_change_intervention():
    for intervention in consent_types.data:
        if intervention["type"] == st.session_state.intervention_input:
            st.session_state.intervention_id = intervention["id"]
            st.session_state.intervention_state = (
                st.session_state.intervention_input
            )
            st.session_state.full_description_state = intervention[
                "full_description"
            ]
            st.session_state.intended_benefits_state = intervention[
                "intended_benefits"
            ]
            st.session_state.potential_risks_state = intervention[
                "potential_risks"
            ]
            break
    else:
        st.session_state.intervention_id = 0
        st.session_state.intervention_state = ""
        st.session_state.full_description_state = ""
        st.session_state.intended_benefits_state = ""
        st.session_state.potential_risks_state = ""
    return


def user_id_get(users, user_name):
    for user in users.data:
        if user["user_name"] == user_name:
            return user["id"]
    return 0


def main():
    global hospital_numbers, patients

    error_placeholder = st.empty()

    fields = {}

    conn = st.connection("supabase", type=SupabaseConnection)

    users = conn.query("*", table="users", ttl="10m").execute()

    user_names = [""] + [
        user["user_name"] for user in users.data if "user_name" in user
    ]

    patients = conn.query(
        "*", table="patient_demographics", ttl="10m"
    ).execute()

    hospital_numbers = [
        patient["hospital_number"]
        for patient in patients.data
        if "hospital_number" in patient
    ]

    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    intervention_types = [""] + [
        consent_type["type"]
        for consent_type in consent_types.data
        if "type" in consent_type
    ]

    st.title("My Digital Consent Form")

    st.text_input(
        'Hospital number (eg "HN001")',
        key="hospital_number_input",
        on_change=on_change_hospital_number,
    )

    st.selectbox(
        "Select Intervention Type",
        intervention_types,
        key="intervention_input",
        on_change=on_change_intervention,
    )

    with st.form("consent_form"):
        st.header("Patient details")
        fields["hospital_number"] = st.text_input(
            "Hospital number",
            st.session_state.hospital_number_state,
            disabled=True,
        )
        fields["first_name"] = st.text_input(
            "First name", st.session_state.first_name_state, disabled=True
        )
        fields["last_name"] = st.text_input(
            "Last name", st.session_state.last_name_state, disabled=True
        )
        fields["date_of_birth"] = st.text_input(
            "Date of birth",
            st.session_state.date_of_birth_state,
            disabled=True,
        )
        fields["patient_email"] = st.text_input(
            "Email", st.session_state.patient_email_state, disabled=True
        )

        st.header("Intervention")
        fields["intervention"] = st.text_input(
            "Intervention",
            st.session_state.intervention_state,
            disabled=True,
        )
        fields["full_description"] = st.text_area(
            "Full description",
            st.session_state.full_description_state,
            disabled=True,
        )
        fields["intended_benefits"] = st.text_area(
            "Intended benefits",
            st.session_state.intended_benefits_state,
            disabled=True,
        )
        fields["potential_risks"] = st.text_area(
            "Potential risks",
            st.session_state.potential_risks_state,
            disabled=True,
        )

        st.header("Signature")
        fields["signed_by"] = st.selectbox("Signed off by", user_names)

        submitted = st.form_submit_button("Submit")

        if submitted:
            all_fields_filled = all(value for value in fields.values())

            if not all_fields_filled:
                st.error("All fields need to be filled.")
                error_placeholder.error("All fields need to be filled.")
                return

            consent_final_data = {
                "patient_id": st.session_state.patient_id,
                "consent_type_id": st.session_state.intervention_id,
                "user_id": user_id_get(users, fields["signed_by"]),
            }

            st.write(consent_final_data)

            result = (
                conn.table("submitted_consents")
                .insert([consent_final_data], count="None")
                .execute()
            )

            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.submitted_consent_id = result.data[0]["id"]

            st.switch_page("pages/final_consent_form.py")
    return


if __name__ == "__main__":
    initialise()
    main()
"""
