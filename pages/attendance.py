# pages/attendance.py
import streamlit as st

DEFAULT_SUBJECTS = [
    "Basic Electrical Engineering",
    "Mathematics",
    "Scientific Programming",
    "Scientific Programming Lab",
    "Basic Electrical Engineering Lab"
]

def show_attendance():
    st.markdown("## 📅 Attendance")

    if "subjects" not in st.session_state:
        st.session_state.subjects = DEFAULT_SUBJECTS.copy()

    role = st.session_state.get("role", "student")

    selected_subject = st.selectbox("Select Subject", st.session_state.subjects)

    st.markdown("### Mark Attendance")
    col1, col2 = st.columns(2)
    with col1:
        student_name = st.text_input("Student Name")
    with col2:
        status = st.selectbox("Status", ["Present", "Absent"])

    if st.button("Submit Attendance"):
        if student_name:
            st.success(f"Marked **{status}** for **{student_name}** in **{selected_subject}**.")
        else:
            st.error("Please enter a student name.")

    if role == "teacher":
        st.markdown("---")
        st.markdown("### 🛠️ Manage Subjects")

        new_subject = st.text_input("Add New Subject")
        if st.button("Add Subject"):
            if new_subject and new_subject not in st.session_state.subjects:
                st.session_state.subjects.append(new_subject)
                st.success(f"Added subject: **{new_subject}**")
            else:
                st.warning("Subject already exists or is empty.")

        remove_subject = st.selectbox("Remove Subject", [""] + st.session_state.subjects)
        if st.button("Remove Selected Subject"):
            if remove_subject:
                st.session_state.subjects.remove(remove_subject)
                st.success(f"Removed subject: **{remove_subject}**")
