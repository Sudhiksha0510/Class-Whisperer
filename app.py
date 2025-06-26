import streamlit as st

# Dummy user data (replace with DB later)
USER_CREDENTIALS = {
    "student1": "pass123",
    "teacher1": "teachme"
}

# Page config
st.set_page_config(page_title="Class Whisperer Login", page_icon="🔐")

# Title
st.title("🔐 Login to Class Whisperer")

# Check if user already logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login form
if not st.session_state.logged_in:
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.success(f"Welcome, {username}!")
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Invalid username or password.")

else:
    st.success(f"You are logged in as {st.session_state.username}")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()