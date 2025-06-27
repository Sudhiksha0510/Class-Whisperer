import streamlit as st

# --- Fake attendance storage (later replace with DB or file) ---
if "attendance_data" not in st.session_state:
    st.session_state.attendance_data = {}

# --- Section to Student Mapping ---
sections = {
    "Section A": ["student_a1", "student_a2"],
    "Section B": ["student_b1", "student_b2"],
    "Section C": ["student_c1", "student_c2"]
}

st.markdown("## 📅 Attendance")

# --- ROLE: Admin/Teacher ---
if st.session_state.role in ["admin", "teacher"]:
    subject = st.selectbox("Select Subject", ["Math", "Physics", "Chemistry"])
    section = st.selectbox("Select Section", list(sections.keys()))
    student = st.selectbox("Select Student", sections[section])
    status = st.radio("Status", ["Present", "Absent"], horizontal=True)

    if st.button("✅ Submit Attendance"):
        st.session_state.attendance_data.setdefault(student, []).append(
            {"subject": subject, "status": status}
        )
        st.success(f"{student} marked as {status} in {subject}.")

# --- ROLE: Student ---
elif st.session_state.role == "student":
    student_name = st.session_state.username
    st.markdown(f"### 👋 Hello, **{student_name}**")
    
    if student_name in st.session_state.attendance_data:
        st.markdown("### 📊 Your Attendance")
        for record in st.session_state.attendance_data[student_name]:
            st.write(f"- **{record['subject']}** → `{record['status']}`")
    else:
        st.info("No attendance records found yet.")
