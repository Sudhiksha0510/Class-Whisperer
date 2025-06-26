import streamlit as st

# Set page configuration
st.set_page_config(page_title="Class Whisperer", layout="wide")

# Custom CSS to style the sidebar buttons
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #0d0d0f;
        color: white;
    }

    .sidebar .css-1d391kg {
        background-color: #1e1e2f;
        padding: 1rem;
    }

    .menu-button {
        width: 100%;
        text-align: left;
        margin: 0.3rem 0;
        background-color: #2a2a40;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.6rem 1rem;
        font-weight: 500;
        transition: 0.3s;
        cursor: pointer;
    }

    .menu-button:hover {
        background-color: #3a3aff;
    }

    .active-button {
        background-color: #3a3aff;
    }
    </style>
""", unsafe_allow_html=True)

# Session state to track current page
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Sidebar with individual buttons
with st.sidebar:
    st.markdown("## 📚 Class Whisperer")
    
    if st.button("🏠 Home", key="home"):
        st.session_state.current_page = "Home"
    if st.button("📅 Attendance", key="attendance"):
        st.session_state.current_page = "Attendance"
    if st.button("🚨 Alerts", key="alerts"):
        st.session_state.current_page = "Alerts"
    if st.button("📓 Class Notes", key="notes"):
        st.session_state.current_page = "Class Notes"
    if st.button("📈 Progress", key="progress"):
        st.session_state.current_page = "Progress"
    if st.button("📝 Teachers Feedback", key="feedback"):
        st.session_state.current_page = "Teachers Feedback"
    if st.button("❓ Ask Doubts", key="doubts"):
        st.session_state.current_page = "Ask Doubts"
    if st.button("🤖 Assistant Bot", key="bot"):
        st.session_state.current_page = "Assistant Bot"

# Main content area
st.markdown(f"## 👋 {st.session_state.current_page}")

if st.session_state.current_page == "Home":
    st.write("Welcome to the dashboard.")
elif st.session_state.current_page == "Attendance":
    st.write("Track attendance here.")
elif st.session_state.current_page == "Alerts":
    st.write("Latest alerts and messages.")
elif st.session_state.current_page == "Class Notes":
    st.write("Access or upload class notes.")
elif st.session_state.current_page == "Progress":
    st.write("Monitor academic progress.")
elif st.session_state.current_page == "Teachers Feedback":
    st.write("Share or view feedback.")
elif st.session_state.current_page == "Ask Doubts":
    st.write("Post and answer questions.")
elif st.session_state.current_page == "Assistant Bot":
    st.write("Interact with your assistant bot.")
