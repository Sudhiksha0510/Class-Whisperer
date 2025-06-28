import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(page_title="📊 Student Progress", layout="wide")

DATA_FILE = "data/student_progress.csv"
os.makedirs("data", exist_ok=True)

# Initialize file if missing
if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=[
        "Section", "Student", "Subject", "Semester",
        "Assignment", "Assignment_Total",
        "Tutorial", "Tutorial_Total",
        "Mid Exam", "Mid_Exam_Total"
    ])
    df_init.to_csv(DATA_FILE, index=False)

# Load data
df = pd.read_csv(DATA_FILE)

# Session check
if "role" not in st.session_state or "username" not in st.session_state:
    st.warning("Please login to access the Progress Page.")
    st.stop()

st.title("📈 Student Progress Tracker")

# -------------------------
# TEACHER VIEW
# -------------------------
if st.session_state.role == "teacher":
    st.header("🧑‍🏫 Teacher Panel")

    with st.form("progress_form", clear_on_submit=False):
        st.subheader("📥 Enter / Update Marks")

        section = st.selectbox("Select Section", ["A", "B", "C"])
        student = st.text_input("Student Name or ID")
        subject = st.text_input("Subject", placeholder="e.g., Mathematics")
        semester = st.selectbox("Semester", ["Sem 1", "Sem 2", "Sem 3", "Sem 4"])

        col1, col2 = st.columns(2)
        with col1:
            assignment = st.number_input("Assignment Marks", min_value=0)
            tutorial = st.number_input("Tutorial Marks", min_value=0)
            mid_exam = st.number_input("Mid Exam Marks", min_value=0)

        with col2:
            assignment_total = st.number_input("Assignment Out of", min_value=1)
            tutorial_total = st.number_input("Tutorial Out of", min_value=1)
            mid_exam_total = st.number_input("Mid Exam Out of", min_value=1)

        submit = st.form_submit_button("Save / Update")

        if submit:
            if not student or not subject:
                st.error("Student and Subject fields cannot be empty.")
            else:
                # Remove duplicate if exists (Section, Student, Subject, Semester)
                df = df[~((df["Section"] == section) & 
                          (df["Student"] == student) & 
                          (df["Subject"] == subject) &
                          (df["Semester"] == semester))]

                new_row = {
                    "Section": section,
                    "Student": student,
                    "Subject": subject,
                    "Semester": semester,
                    "Assignment": assignment,
                    "Assignment_Total": assignment_total,
                    "Tutorial": tutorial,
                    "Tutorial_Total": tutorial_total,
                    "Mid Exam": mid_exam,
                    "Mid_Exam_Total": mid_exam_total
                }

                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_csv(DATA_FILE, index=False)
                st.success(f"✅ Progress updated for {student} in {subject} - {semester}.")

    st.divider()
    st.subheader("🔍 Filter Progress Records")

    with st.expander("Click to filter student progress"):
        filter_section = st.selectbox("Filter by Section", ["All"] + sorted(df["Section"].unique()))
        filter_subject = st.selectbox("Filter by Subject", ["All"] + sorted(df["Subject"].dropna().unique()))
        filter_semester = st.selectbox("Filter by Semester", ["All"] + sorted(df["Semester"].dropna().unique()))
        filter_student = st.text_input("Search by Student Name or ID (optional)").strip()

        filtered_df = df.copy()
        if filter_section != "All":
            filtered_df = filtered_df[filtered_df["Section"] == filter_section]
        if filter_subject != "All":
            filtered_df = filtered_df[filtered_df["Subject"] == filter_subject]
        if filter_semester != "All":
            filtered_df = filtered_df[filtered_df["Semester"] == filter_semester]
        if filter_student:
            filtered_df = filtered_df[filtered_df["Student"].str.contains(filter_student, case=False)]

        st.dataframe(filtered_df, use_container_width=True)

        import io

# ... below the st.dataframe(filtered_df)

    if not filtered_df.empty:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            filtered_df.to_excel(writer, index=False, sheet_name="Progress Report")
        st.download_button(
            label="📥 Download as Excel",
            data=buffer,
            file_name="student_progress_export.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    from fpdf import FPDF

    if not filtered_df.empty:
        class PDF(FPDF):
            def header(self):
                self.set_font("Arial", "B", 12)
                self.cell(200, 10, "Student Progress Report", border=False, ln=True, align="C")

        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        col_names = list(filtered_df.columns)
        col_width = 190 / len(col_names)  # Page width = 210 - 10 margin on each side

    # Table Header
        for col in col_names:
            pdf.cell(col_width, 10, col, border=1)
        pdf.ln()

    # Table Rows
        for _, row in filtered_df.iterrows():
            for col in col_names:
                cell_value = str(row[col])
                pdf.cell(col_width, 10, cell_value, border=1)
            pdf.ln()

    # Save to bytes
        pdf_bytes = pdf.output(dest='S').encode('latin-1')


        st.download_button(
        label="📄 Download as PDF",
        data=pdf_bytes,
        file_name="student_progress_report.pdf",
        mime="application/pdf"
    )



# -------------------------
# STUDENT VIEW
# -------------------------
elif st.session_state.role == "student":
    st.header("🎓 Student Panel")

    student_name = st.session_state.username
    student_progress = df[df["Student"].str.lower() == student_name.lower()]

    if not student_progress.empty:
        st.success("Here's your progress by subject and semester:")

        # Subject and semester-wise display
        grouped = student_progress.groupby(["Subject", "Semester"])

        for (subject, semester), group in grouped:
            st.markdown(f"### 📘 {subject} — {semester}")

            row = group.iloc[0]

            progress_display = pd.DataFrame({
                "Category": ["Assignment", "Tutorial", "Mid Exam"],
                "Your Marks": [
                    f"{row['Assignment']} / {row['Assignment_Total']}",
                    f"{row['Tutorial']} / {row['Tutorial_Total']}",
                    f"{row['Mid Exam']} / {row['Mid_Exam_Total']}"
                ]
            })

            st.table(progress_display)

            # Chart
            marks = [
                (row['Assignment'], row['Assignment_Total']),
                (row['Tutorial'], row['Tutorial_Total']),
                (row['Mid Exam'], row['Mid_Exam_Total'])
            ]
            chart_df = pd.DataFrame({
                "Category": ["Assignment", "Tutorial", "Mid Exam"],
                "Percentage": [round((m / t) * 100, 2) for m, t in marks]
            })

            fig = px.bar(
                chart_df,
                x="Category",
                y="Percentage",
                color="Category",
                title=f"📊 {subject} - {semester}",
                range_y=[0, 100],
                text_auto=True
            )
            fig.update_layout(yaxis_title="Percentage %", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("No progress records found for you yet.")
