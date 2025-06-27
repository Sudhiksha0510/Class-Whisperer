import streamlit as st
from datetime import datetime

# Initialize alerts store
if "alerts" not in st.session_state:
    st.session_state.alerts = []

# Role and username from session
role = st.session_state.get("role", "")
username = st.session_state.get("username", "")

st.markdown("## 🚨 Alerts")

# -----------------------
# Alert Creation (Admin/Teacher Only)
# -----------------------
if role in ["admin", "teacher"]:
    st.subheader("➕ Create New Alert")

    alert_text = st.text_input("Alert Message")
    section = st.selectbox("Target Section", ["All", "Section A", "Section B", "Section C"])
    subject = st.selectbox("Related Subject", ["All", "Maths", "Physics", "BEE", "English"])
    date = datetime.now().strftime("%Y-%m-%d")

    if st.button("Add Alert"):
        if alert_text:
            st.session_state.alerts.append({
                "text": alert_text,
                "section": section,
                "subject": subject,
                "date": date,
                "created_by": username
            })
            st.success("Alert added successfully.")
        else:
            st.warning("Alert message cannot be empty.")

# -----------------------
# Filters
# -----------------------
st.subheader("📌 Alerts Feed")

filter_subject = st.selectbox("Filter by Subject", ["All", "Maths", "Physics", "BEE", "English"], key="filter_subject")
filter_section = st.selectbox("Filter by Section", ["All", "Section A", "Section B", "Section C"], key="filter_section")
filter_date = st.date_input("Filter by Date (optional)", value=None, key="filter_date")

# -----------------------
# Show Alerts (based on role)
# -----------------------
visible_alerts = []

for alert in st.session_state.alerts:
    if filter_subject != "All" and alert["subject"] != filter_subject:
        continue
    if filter_section != "All" and alert["section"] != filter_section:
        continue
    if filter_date and alert["date"] != filter_date.strftime("%Y-%m-%d"):
        continue

    # Students see only section/subject relevant ones
    if role == "student":
        student_section = "Section A"  # 💡 Replace this with actual logic if stored
        if alert["section"] not in ["All", student_section]:
            continue
        # Optional: filter_subject already applied above

    visible_alerts.append(alert)

if visible_alerts:
    for i, alert in enumerate(visible_alerts):
        with st.container():
            st.markdown(f"""
                #### 🔔 {alert['text']}
                - 📚 Subject: `{alert['subject']}`
                - 📆 Date: `{alert['date']}`
                - 🎯 Section: `{alert['section']}`
                - 👤 Posted by: `{alert['created_by']}`
            """)
            # Allow delete only for admin/teacher
            if role in ["admin", "teacher"]:
                if st.button(f"❌ Delete", key=f"delete_{i}"):
                    st.session_state.alerts.remove(alert)
                    st.rerun()
else:
    st.info("No alerts to show for selected filters.")
