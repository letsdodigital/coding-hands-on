import streamlit as st

"""def main():
    st.title("Hello")
    st.text("Hello World!")

    return


if __name__ == "__main__":
    main()"""

#
#
#

from st_supabase_connection import SupabaseConnection
def main():
    st.title("API call test")

    # Initialize connection.
    conn = st.connection("supabase",type=SupabaseConnection)

    # Perform query.
    rows = conn.query("*", table="User", ttl="10m").execute()

    st.write(rows)
    return

if __name__ == "__main__":
    main()