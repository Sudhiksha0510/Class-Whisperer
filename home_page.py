import streamlit as st

def main_app():
    st.set_page_config(page_title="Class Whisperer", layout="wide")

    def show_alerts():
    # Import alert logic dynamically from the alerts.py file
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

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.username.title()}")
        st.markdown(f"**Role:** `{st.session_state.role}`")
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.rerun()

        st.markdown("---")
        nav_choice = st.radio(
            "Navigation",
            list(pages.values()),
            label_visibility="collapsed"
        )

        # Get the internal key from the value
        for key, label in pages.items():
            if label == nav_choice:
                st.session_state.current_page = key

    if st.session_state.current_page == "Home":
        st.markdown("## 👋 Home")
        st.write("Welcome to the Class Whisperer dashboard.")
    elif st.session_state.current_page == "Attendance":
        st.switch_page("pages/attendance.py")
    elif st.session_state.current_page=="Alerts":
        st.switch_page("pages/alerts.py")
    else:
        st.markdown(f"## {pages[st.session_state.current_page]}")
        st.info(f"This page ({st.session_state.current_page}) is under construction.")