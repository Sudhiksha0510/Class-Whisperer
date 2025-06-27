import streamlit as st
import streamlit.web.cli as stcli
import sys
from login_app import login

import streamlit as st

# 👇 Add this line to remove Streamlit's default page selector
st.set_page_config(
    page_title="Class Whisperer",
    layout="wide",
    initial_sidebar_state="collapsed",  # Optional: collapse sidebar on load
    menu_items={"About": None, "Get help": None, "Report a bug": None}
)

# Hide multipage navigation from sidebar
st.markdown("""
    <style>
    section[data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)


# Hide multipage selector
if __name__ == "__main__" or st._is_running_with_streamlit:
    sys.argv = ["streamlit", "run", "app.py", "--"]

# Check login state
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login()
    st.stop()
else:
    from home_page import main_app
    main_app()
