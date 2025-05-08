import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query
from datetime import datetime


class QueryConsentForm:
    def __init__(self, main_table_name):
        self.main_table_name = main_table_name
        self.conn = st.connection("supabase", type=SupabaseConnection)
        self.main_table = execute_query(
            self.conn.table(main_table_name).select("*"), ttl="0"
        )
        return

    def created_at(self):
        """Get date opf creation.

        Returns the created at date.

        Returns:
            datetime: The created at date.
        """
        main_table_data_single = [
            foreign_data
            for foreign_data in self.main_table.data
            if foreign_data["id"] == st.session_state["submitted_consent_id"]
        ]

        created_at_date = datetime.fromisoformat(
            main_table_data_single[0]["created_at"]
        )

        return created_at_date

    def execute(self, foreign_table_name, field):
        """Get the data from the foreign table.

        Returns the data from the foreign table.

        Args:
            foreign_table_name (str): The name of the foreign table.
            field (str): The field to match the data.
        Returns:
            dict: The data from the foreign table.
        """
        foreign_table_data_all = execute_query(
            self.conn.table(foreign_table_name).select("*"), ttl="0"
        )

        main_table_data_single = [
            foreign_data
            for foreign_data in self.main_table.data
            if foreign_data["id"] == st.session_state["submitted_consent_id"]
        ]

        if not main_table_data_single:
            raise ValueError(
                "No matching data found in the main table after 5 attempts."
            )

        main_table_data_single = [
            foreign_data
            for foreign_data in self.main_table.data
            if foreign_data["id"] == st.session_state["submitted_consent_id"]
        ]

        foreign_table_data_all = [
            foreign_table_data_all
            for foreign_table_data_all in foreign_table_data_all.data
            if foreign_table_data_all["id"] == main_table_data_single[0][field]
        ]

        return foreign_table_data_all[0]


def main():
    """The main function"""

    st.title("Your completed consent form")

    if (
        "submitted_consent_id" not in st.session_state
        or st.session_state["submitted_consent_id"] == 0
    ):
        st.write("A consent form has not been submitted")
        return

    query = QueryConsentForm("submitted_consents")

    patient = query.execute("patient_demographics", "patient_id")

    date_of_birth_str = patient["date_of_birth"]
    date_of_birth_object = datetime.strptime(
        date_of_birth_str, "%Y-%m-%d"
    ).date()

    consent_type = query.execute("consent_types", "consent_type_id")

    user = query.execute("users", "user_id")

    st.header("Patient details")
    st.text_input("First name", value=patient["first_name"], disabled=True)
    st.text_input("Last name", value=patient["last_name"], disabled=True)
    st.text_input(
        "Hospital number", value=patient["hospital_number"], disabled=True
    )
    st.date_input("Date of birth", value=date_of_birth_object, disabled=True)
    st.text_input("Email", value=patient["email"], disabled=True)

    st.header("Intervention")
    st.text_input("Intervention", value=consent_type["type"], disabled=True)
    st.text_area(
        "Full description",
        value=consent_type["full_description"],
        disabled=True,
    )
    st.text_area(
        "Intended benefits",
        value=consent_type["intended_benefits"],
        disabled=True,
    )
    st.text_area(
        "Potential risks",
        value=consent_type["potential_risks"],
        disabled=True,
    )

    st.header("Signature")
    st.text_input(
        "Signed off by",
        value=f"{ user['first_name'] } { user['last_name'] }",
        disabled=True,
    )
    st.date_input("Date signed", query.created_at(), disabled=True)

    return


if __name__ == "__main__":
    main()
