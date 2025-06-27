import streamlit as st

# --- Initial Attendance Data Setup (replace later with DB or persistent storage) ---
if "attendance_data" not in st.session_state:
    st.session_state.attendance_data = {}

# --- Section Roll Number Mapping ---
section_rolls = {
    f"Section {chr(65+i)}": [f"245624733{str(j).zfill(3)}" for j in range(1+i*64, 1+(i+1)*64)]
    for i in range(6)
}

# --- Student Full Names (for display) ---
def get_full_name(roll):
    return f"Student {roll[-3:]}"

# --- Style Tweaks for Compact Layout ---
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
    }
    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: 0.2rem;
    }
    div[data-testid="stHorizontalBlock"] > div {
        align-items: center;
    }
    div[data-baseweb="radio"] {
        margin-top: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI Start ---
st.markdown("## 🗕️ Attendance")

# --- TEACHER VIEW ---
if st.session_state.role in ["admin", "teacher"]:
    subject = st.selectbox("Select Subject", [
        "Basic Electrical Engineering", "Mathematics",
        "Scientific Programming", "Scientific Programming Lab",
        "Basic Electrical Engineering Lab"
    ])

    section = st.selectbox("Select Section", list(section_rolls.keys()))
    rolls = section_rolls[section]

    # Button to mark all present
    if "mark_all" not in st.session_state:
        st.session_state.mark_all = {}

    if st.button("✅ Mark All Present"):
        for r in rolls:
            st.session_state.mark_all[r] = "Present"

    st.write("### Mark Attendance:")

    # Table headers
    col1, col2 = st.columns([5, 3])
    col1.markdown("**Roll Number & Name**")
    col2.markdown("**Status**")

    for roll in rolls:
        col1, col2 = st.columns([5, 3])
        with col1:
            st.markdown(f"{roll} - {get_full_name(roll)}")
        with col2:
            st.radio(
                label="",
                options=["Present", "Absent"],
                key=f"status_{roll}",
                horizontal=True,
                index=0 if st.session_state.mark_all.get(roll) == "Present" else 1,
                label_visibility="collapsed"
            )

    if st.button("📅 Submit Attendance"):
        for roll in rolls:
            status = st.session_state.get(f"status_{roll}", "Absent")
            st.session_state.attendance_data.setdefault(roll, []).append({
                "subject": subject,
                "status": status
            })
        st.success(f"Attendance submitted for {section} in {subject}.")

# --- STUDENT VIEW ---
elif st.session_state.role == "student":
    student_roll = st.session_state.username  # assume login username is roll number
    st.markdown(f"### 👋 Hello, **{get_full_name(student_roll)}**")

    records = st.session_state.attendance_data.get(student_roll, [])
    if records:
        st.markdown("### 📊 Your Attendance")
        subject_attendance = {}
        for record in records:
            subject = record["subject"]
            subject_attendance.setdefault(subject, []).append(record["status"])

        for subject, statuses in subject_attendance.items():
            total = len(statuses)
            present_count = statuses.count("Present")
            st.write(f"- **{subject}**: {present_count}/{total} present")
    else:
        st.info("No attendance records found yet.")

# --- Other roles or errors ---
else:
    st.error("You are not authorized to view this page.")
