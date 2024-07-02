import streamlit as st
from st_supabase_connection import SupabaseConnection

"""Exercise 7 - Getting data from other tables

OUTLINE: So, you need data from more than one database table to successfully 
create your consent form and submit it. We will now get you to query the
`patients` and `consent_types` tables and output the results to the browser.
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
