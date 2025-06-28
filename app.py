import streamlit as st
from login_app import login
from home_page import main_app  # ✅ this line was missing

st.set_page_config(page_title="Class Whisperer", layout="wide")

# Login check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login()
else:
    main_app()  # ✅ only works now that it's imported
