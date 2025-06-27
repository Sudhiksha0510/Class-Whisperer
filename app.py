import streamlit as st
from login_app import login
from home_page import show_home

# Page configuration
st.set_page_config(page_title="Class Whisperer", layout="wide")

# If not logged in, show login
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login()

else:
    # Sidebar
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.username.title()}")
        st.markdown(f"**Role:** `{st.session_state.role}`")
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.experimental_rerun()
        st.markdown("---")
        st.markdown("🏠 Home")

    # Show Home Page
    show_home()
