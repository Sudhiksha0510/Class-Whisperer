import streamlit as st

def show():
    st.title("🏠 Home")
    st.write("Welcome to the Class Whisperer Home Page!")


# Configure Streamlit page
st.set_page_config(page_title="Class Whisperer", layout="wide")

def main_app():
    # --- Define Pages ---
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

        st.markdown("---")
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.rerun()

        st.markdown("### 📂 Navigation")
        for page_key, label in pages.items():
            if st.button(label):
                st.session_state.current_page = page_key
                st.rerun()

    # --- Page Routing ---
    current = st.session_state.current_page
    if current == "Home":
        st.markdown("## 👋 Home")
        st.write("Welcome to the Class Whisperer dashboard.")
    elif current == "Attendance":
        st.switch_page("pages/attendance.py")
    elif current == "Alerts":
        st.switch_page("pages/alerts.py")
    elif current == "Teachers Feedback":
        st.switch_page("pages/teacher_feedback.py")
    elif current == "Ask Doubts":
        st.switch_page("pages/ask_doubts.py")
    elif current == "Progress":
        st.switch_page("pages/progress.py")
    elif current == "Assistant Bot":
        st.markdown("## 🤖 Assistant Bot (Coming Soon!)")
        st.info("ClassMate is still under training 🧠💬. Stay tuned for launch!")
    elif current == "Class Notes":
        st.switch_page("pages/notes.py")
    else:
        st.markdown(f"## {pages[current]}")
        st.info(f"This page ({current}) is under construction.")
