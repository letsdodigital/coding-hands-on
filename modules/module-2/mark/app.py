import streamlit as st


"""Exercise 1 - Hello World!
Run the app using the command:
$ streamlit run .py
"""

"""def main():
    st.title("Hello")
    st.text("Hello World!")

    return


if __name__ == "__main__":
    main()"""

"""Exercise 2 - Application Process Interface (API) testing
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""from st_supabase_connection import SupabaseConnection
def main():
    st.title("API call test")

    # Initialize connection.
    conn = st.connection("supabase",type=SupabaseConnection)

    # Perform query.
    rows = conn.query("*", table="User", ttl="10m").execute()

    st.header("API test results")
    st.write(rows)
    return

if __name__ == "__main__":
    main()"""

"""Exercise 3

"""

from st_supabase_connection import SupabaseConnection
def main():
    st.title("My consent form")

    st.header("Patient details")
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    hospital_number = st.text_input("Hospital number")
    date_of_birth = st.date_input("Date of birth", None)
    patients_email = st.text_input("Email")

    st.header("Intervention")
    intervention = st.selectbox("Intervention", ["", "Below knee amputation", "Cannula"])
    full_description = st.text_input("Full description", disabled=True)
    intended_benefits = st.text_input("Intended benefits", disabled=True)
    potential_risks = st.text_input("Potential risks", disabled=True)

    st.header("Signature")
    signed_by = st.selectbox("Signed off by", ["", "Dr Smith", "Nurse Jones"])

    # Initialize connection.
    conn = st.connection("supabase",type=SupabaseConnection)

    # Perform query.
    users = conn.query("*", table="users", ttl="10m").execute()
    patients = conn.query("*", table="patient_demographics", ttl="10m").execute()
    consent_types = conn.query("*", table="consent_types", ttl="10m").execute()

    test_data = {
        "test_data": "Some test data"
    }

    result = conn.table("test_upload").insert([test_data], count="None").execute()
    

    st.header("API test results")
    st.write(users)
    st.write(patients)
    st.write(consent_types)
    return

if __name__ == "__main__":
    main()