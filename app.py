# app.py
import streamlit as st
from login_app import login
from home_page import main_app

# Check login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Show login or dashboard
if not st.session_state.logged_in:
    login()
else:
    main_app()