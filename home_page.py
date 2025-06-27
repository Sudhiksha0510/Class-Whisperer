import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import datetime

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
    st.markdown("## 🚨 Alerts & Class Exchanges")
    st.write("All important announcements and class reschedules will appear here.")

    # Simulated role — change this to "student" to test view-only
    role = "admin"  # or "teacher" or "student"

    # Session state for alert storage
    if "alert_list" not in st.session_state:
        st.session_state.alert_list = [
            {"title": "Mid-Sem Exam Scheduled", "body": "Starts July 22.", "type": "info", "by": "Admin", "time": "2025-06-27 11:30"},
            {"title": "DS Class Exchange", "body": "DS class moved from Mon 3PM to Wed 10AM", "type": "warning", "by": "Prof. Mehta", "time": "2025-06-27 10:00"},
        ]

    # Only admins/teachers can post
    if role in ["admin", "teacher"]:
        with st.expander("➕ Post New Alert / Class Exchange"):
            title = st.text_input("Title")
            body = st.text_area("Message")
            alert_type = st.selectbox("Type", ["info", "warning", "success"])
            author = st.text_input("Your Name", value="Admin" if role == "admin" else "Teacher")
            if st.button("Post Alert"):
                new_alert = {
                    "title": title,
                    "body": body,
                    "type": alert_type,
                    "by": author,
                    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                st.session_state.alert_list.insert(0, new_alert)
                st.success("✅ Alert posted!")

    # Alert color mapping
    colors = {
        "info": "#3a3aff",
        "warning": "#ff914d",
        "success": "#4caf50"
    }

    # Display all alerts
    for alert in st.session_state.alert_list:
        st.markdown(f"""
            <div style='background-color: {colors[alert['type']]}; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; color: white;'>
                <h4 style='margin-bottom: 0.3rem;'>{alert['title']}</h4>
                <p style='margin: 0.2rem 0;'>{alert['body']}</p>
                <p style='font-size: 0.85rem; color: #ddd;'>By {alert['by']} • {alert['time']}</p>
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
