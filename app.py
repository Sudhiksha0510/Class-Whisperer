# ✅ app.py
import streamlit as st

# Page configuration
st.set_page_config(page_title="Class Whisperer - Home", page_icon="🏠", layout="wide")

# Hide Streamlit default navigation
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] { display: none; }
    </style>
""", unsafe_allow_html=True)

# Simulated login
if "username" not in st.session_state:
    st.session_state.username = "Teacher1"
if "role" not in st.session_state:
    st.session_state.role = "Teacher"
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Sidebar
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state.username}")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.experimental_rerun()

    st.markdown("### 📁 Navigation")
    if st.button("🏠 Home"):
        st.session_state.current_page = "home"
    if st.button("📅 Attendance"):
        st.session_state.current_page = "attendance"
    if st.button("🚨 Alerts"):
        st.session_state.current_page = "alerts"
    if st.button("📚 Notes"):
        st.session_state.current_page = "notes"
    if st.button("💬 Ask Doubts"):
        st.session_state.current_page = "ask_doubts"
    if st.button("📝 Teacher Feedback"):
        st.session_state.current_page = "teacher_feedback"
    if st.button("📈 Progress"):
        st.session_state.current_page = "progress"

# Routing placeholders (you can add actual imports later)
if st.session_state.current_page == "home":
    st.title("🏠 Home")
    st.write("This is the Home Page")

elif st.session_state.current_page == "attendance":
    st.title("📅 Attendance")
    st.write("This is the Attendance Page")

elif st.session_state.current_page == "alerts":
    st.title("🚨 Alerts")
    st.write("This is the Alerts Page")

elif st.session_state.current_page == "notes":
    st.title("📚 Notes")
    st.write("This is the Notes Page")

elif st.session_state.current_page == "ask_doubts":
    st.title("💬 Ask Doubts")
    st.write("This is the Ask Doubts Page")

elif st.session_state.current_page == "teacher_feedback":
    st.title("📝 Teacher Feedback")
    st.write("This is the Teacher Feedback Page")

elif st.session_state.current_page == "progress":
    st.title("📈 Progress")
    st.write("This is the Progress Page")
