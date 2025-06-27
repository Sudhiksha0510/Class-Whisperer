import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Convert image to base64
def image_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

# Load your uploaded image
logo_img = Image.open("class_emoji.webp")
logo_base64 = image_to_base64(logo_img)

# Page config
# CSS for clean, borderless, flat sidebar nav
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

# Page map
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

# Track selected page
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Sidebar with image logo and nav items
with st.sidebar:
    # Navigation items only (no title/logo)
    for key, label in pages.items():
        if st.button(label, key=key):
            st.session_state.current_page = key

        if st.session_state.current_page == key:
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


# Page display functions
def show_home():
    st.markdown(f"""
        <div style='display: flex; align-items: center; gap: 1rem;'>
            <img src='data:image/png;base64,{logo_base64}' width='40' style='border-radius: 6px;'/>
            <h1 style='margin: 0;'>CLASS WHISPERER</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 👋 Home")
    st.write("Welcome to the dashboard.")


def show_attendance():
    st.markdown("## 📅 Attendance")
    st.write("Track attendance here.")

def show_alerts():
    st.markdown("## 🚨 Alerts")
    st.write("Stay updated with the latest announcements from your teachers or admins.")

    # Sample alerts – this can later be dynamic
    alerts = [
        {"title": "Mid-Sem Exam Scheduled", "body": "Your mid-sem exam starts from July 22nd. Prepare accordingly.", "type": "info"},
        {"title": "Assignment Deadline", "body": "Data Structures assignment is due on July 5th. Submit via portal.", "type": "warning"},
        {"title": "New Notes Uploaded", "body": "Machine Learning lecture notes have been uploaded.", "type": "success"},
    ]

    # Style mapping
    colors = {
        "info": "#3a3aff",
        "warning": "#ff914d",
        "success": "#4caf50"
    }

    for alert in alerts:
        st.markdown(f"""
            <div style='background-color: {colors[alert['type']]}; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; color: white;'>
                <h4 style='margin-bottom: 0.3rem;'>{alert['title']}</h4>
                <p style='margin: 0;'>{alert['body']}</p>
            </div>
        """, unsafe_allow_html=True)


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

# Page render map
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

# Render selected page
page_functions[st.session_state.current_page]()
