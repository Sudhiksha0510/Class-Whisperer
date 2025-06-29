import streamlit as st

# Dummy credentials
USER_CREDENTIALS = {
    "student1": {"password": "pass123", "role": "student"},
    "teacher1": {"password": "teach123", "role": "teacher"},
    "admin1": {"password": "admin123", "role": "admin"},
}

def login():
    st.set_page_config(page_title="Class Whisperer Login", layout="wide", initial_sidebar_state="collapsed")

    st.markdown("""
        <style>
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #0d0d0f;
            color: white;
        }
        .stTextInput > div > div {
            background-color: #2a2a40;
            border-radius: 5px;
        }
        .stButton > button {
            background-color: transparent;
            border: 1px solid #ff4b4b;
            color: #ff4b4b;
        }
        /* ✅ Hide the default Streamlit multi-page nav */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        [data-testid="stSidebarNavSeparator"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🔐 Class Whisperer Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = USER_CREDENTIALS.get(username)
        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = user["role"]
            st.experimental_set_query_params(page="Home")
            st.rerun()
        else:
            st.error("Invalid credentials.")
