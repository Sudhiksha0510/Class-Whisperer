# home_page.py
import streamlit as st
from pages.attendance import show_attendance  # import from new file

def main_app():
    # Page configuration
    st.set_page_config(page_title="Class Whisperer", layout="wide", initial_sidebar_state="expanded")

    # Custom style
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #0d0d0f;
            color: white;
        }

        section[data-testid="stSidebar"] {
            background-color: #1e1e2f;
            padding: 1rem;
        }

        button[kind="secondary"] {
            all: unset;
            display: block;
            width: 100%;
            text-align: left;
            padding: 0.6rem 1rem;
            margin-bottom: 0.4rem;
            border-radius: 6px;
            font-size: 1rem;
            color: white;
            cursor: pointer;
            transition: 0.3s;
        }

        button[kind="secondary"]:hover {
            background-color: #3a3aff;
        }

        .active {
            background-color: #3a3aff !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navigation items
    pages = {
        "Home": "🏠 Home",
        "Attendance": "📅 Attendance",
        "Alerts": "🚨 Alerts",
        "Class Notes": "📓 Class Notes",
        "Progress": "📈 Progress",
        "Teachers Feedback": "📝 Teachers Feedback",
        "Ask Doubts": "❓ Ask Doubts",
        "Assistant Bot": "🤖 Assistant Bot"
    }

    # Set default page
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    # Sidebar
    with st.sidebar:
        st.markdown("## 📚 Class Whisperer")
        for key, label in pages.items():
            is_active = st.session_state.current_page == key
            btn = st.button(label, key=key)
            if btn:
                st.session_state.current_page = key
            if is_active:
                st.markdown(f"""
                    <script>
                    var btns = parent.document.querySelectorAll('button[kind="secondary"]');
                    btns.forEach(b => {{
                        if (b.innerText === "{label}") {{
                            b.classList.add("active");
                        }}
                    }});
                    </script>
                """, unsafe_allow_html=True)

    # Page-specific logic
    def show_home():
        st.markdown("## 👋 Home")
        st.write("Welcome to the dashboard.")

    def show_alerts():
        st.markdown("## 🚨 Alerts")
        st.write("Latest alerts and messages.")

    def show_notes():
        st.markdown("## 📓 Class Notes")
        st.write("Access or upload class notes.")

    def show_progress():
        st.markdown("## 📈 Progress")
        st.write("Monitor academic progress.")

    def show_feedback():
        st.markdown("## 📝 Teachers Feedback")
        st.write("Share or view feedback.")

    def show_doubts():
        st.markdown("## ❓ Ask Doubts")
        st.write("Post and answer questions.")

    def show_bot():
        st.markdown("## 🤖 Assistant Bot")
        st.write("Interact with your assistant bot.")

    # Page display map
    page_functions = {
        "Home": show_home,
        "Attendance": show_attendance,
        "Alerts": show_alerts,
        "Class Notes": show_notes,
        "Progress": show_progress,
        "Teachers Feedback": show_feedback,
        "Ask Doubts": show_doubts,
        "Assistant Bot": show_bot
    }

    # Display selected
    page_functions[st.session_state.current_page]()
