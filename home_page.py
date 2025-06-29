import streamlit as st
import openai

# Configure Streamlit page
st.set_page_config(page_title="Class Whisperer", layout="wide")
def main_app():

# --- Define Pages ---
    def show_alerts():
        with open("pages/alerts.py", "r", encoding="utf-8") as f:
            exec(f.read(), globals())

    pages = {
    "Home": "🏠 Home",
    "Attendance": "📅 Attendance",
    "Alerts": "🚨 Alerts",
    "Class Notes": "📓 Class Notes",
    "Progress": "📈 Progress",
    "Teachers Feedback": "📝 Teachers Feedback",
    "Ask Doubts": "❓ Ask Doubts",
    "Assistant Bot": "🤖 Assistant Bot",
}

# --- Navigation State ---
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

# --- Sidebar Navigation ---
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.get('username', 'Guest').title()}")
        st.markdown(f"**Role:** `{st.session_state.get('role', 'guest')}`")
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.rerun()

        st.markdown("---")
        nav_choice = st.radio(
        "Navigation",
            list(pages.values()),
            label_visibility="collapsed"
        )

        for key, label in pages.items():
            if label == nav_choice:
                st.session_state.current_page = key

# --- Page Routing ---
    if st.session_state.current_page == "Home":
        st.markdown("## 👋 Home")
        st.write("Welcome to the Class Whisperer dashboard.")
    elif st.session_state.current_page == "Attendance":
        st.switch_page("pages/attendance.py")
    elif st.session_state.current_page == "Alerts":
        st.switch_page("pages/alerts.py")
    elif st.session_state.current_page == "Teachers Feedback":
        st.switch_page("pages/teacher_feedback.py")
    elif st.session_state.current_page == "Ask Doubts":
        st.switch_page("pages/ask_doubts.py")
    elif st.session_state.current_page == "Progress":
        st.switch_page("pages/progress.py")
    elif st.session_state.current_page == "Assistant Bot":
        st.markdown("## 🤖 Assistant Bot (Coming Soon!)")
        st.info("ClassMate is still under training 🧠💬. Stay tuned for launch!")
    elif st.session_state.current_page == "Class Notes":
        st.switch_page("pages/notes.py")
    else:
        st.markdown(f"## {pages[st.session_state.current_page]}")
        st.info(f"This page ({st.session_state.current_page}) is under construction.")
