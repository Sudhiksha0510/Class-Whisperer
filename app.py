# app.py
import streamlit as st
from login_app import login

# This ensures login state is checked first
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login()
    st.stop()
else:
    # Redirect to home page
    st.switch_page("pages/home_page.py")

