import streamlit as st

# Dummy user credentials
USER_CREDENTIALS = {
    "student1": "pass123",
    "teacher1": "teachme"
}

# Page setup
st.set_page_config(page_title="Class Whisperer", layout="wide")

# Custom CSS for layout and design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #0d0d0f;
        color: white;
    }

    .login-box {
        background-color: #1c1c3c;
        padding: 3rem 2rem;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(0,0,0,0.3);
        width: 350px;
        text-align: center;
        margin: auto;
    }

    .avatar {
        width: 90px;
        margin-bottom: 1.5rem;
        border-radius: 50%;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    .login-button {
        background-color: #1a1aff;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.75rem;
        width: 100%;
        border-radius: 6px;
        margin-top: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .login-button:hover {
        background-color: #0000cc;
    }

    input {
        background-color: #2e2e4d !important;
        color: white !important;
        border: 1px solid #555 !important;
    }

    .welcome-box {
        padding: 3rem;
        max-width: 500px;
        margin-left: 40px;
        margin-top: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# Layout with two columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    # ✅ Avatar only, centered above login box
    st.markdown(
        '<img class="avatar" src="https://cdn-icons-png.flaticon.com/512/10542/10542844.png" alt="User Icon">',
        unsafe_allow_html=True
    )

    st.markdown("#### Login to Class Whisperer")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_btn = st.form_submit_button("Login")

            if login_btn:
                if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                    st.success(f"Welcome, {username}!")
                    st.session_state.logged_in = True
                    st.session_state.username = username
                else:
                    st.error("Invalid username or password.")

        st.markdown('<button class="login-button">Login</button>', unsafe_allow_html=True)

    else:
        st.success(f"Logged in as {st.session_state.username}")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
    st.markdown("### 👋 Welcome to Class Whisperer")
    st.write(
        "Class Whisperer is a safe space for students to give honest feedback to faculty—"
        "anonymously and easily. Our goal is to help improve classroom experiences and "
        "build trust between students and teachers."
    )
    st.markdown('</div>', unsafe_allow_html=True)
