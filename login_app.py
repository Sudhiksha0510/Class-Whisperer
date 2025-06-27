# login_app.py
import streamlit as st

USER_CREDENTIALS = {
    "admin1": {"password": "adminpass", "role": "admin"},
    "teacher1": {"password": "teacherpass", "role": "teacher"},
    "student1": {"password": "studentpass", "role": "student"}
}

def login():
    st.set_page_config(page_title="Class Whisperer Login", layout="wide")

    st.markdown("""
        <style>
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #0d0d0f;
            color: white;
        }
        .stTextInput input, .stTextInput label {
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
            st.experimental_rerun()  # ✅ immediately reloads app.py, which shows home_page
        else:
            st.error("Invalid credentials. Try again.")
