import streamlit as st
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="📓 Class Notes", layout="wide")

# Paths
NOTES_DIR = "data/class_notes"
META_FILE = "data/class_notes_metadata.csv"

os.makedirs(NOTES_DIR, exist_ok=True)

# Load or create metadata CSV
if os.path.exists(META_FILE):
    try:
        notes_df = pd.read_csv(META_FILE)
    except pd.errors.EmptyDataError:
        notes_df = pd.DataFrame(columns=["filename", "title", "subject", "semester", "uploaded_by", "timestamp"])

else:
    notes_df = pd.DataFrame(columns=["filename", "title", "subject", "semester", "uploaded_by", "timestamp"])
    notes_df.to_csv(META_FILE, index=False)

st.title("📓 Class Notes Repository")

role = st.session_state.get("role", "guest")
username = st.session_state.get("username", "guest")

# --- TEACHER: Upload Section ---
if role == "teacher":
    st.subheader("📤 Upload New Notes")

    with st.form("upload_form"):
        uploaded_file = st.file_uploader("Upload Notes File (PDF, DOCX, etc)", type=["pdf", "docx", "png", "jpg"])
        subject = st.selectbox("Select Subject", ["Math", "Physics", "Chemistry", "Python", "C Programming"])
        semester = st.selectbox("Select Semester", ["1", "2", "3", "4", "5", "6", "7", "8"])
        title = st.text_input("Optional Title", "")
        submit_btn = st.form_submit_button("Upload")

        if submit_btn and uploaded_file:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{semester}_{subject}_{timestamp}_{uploaded_file.name}"
            filepath = os.path.join(NOTES_DIR, filename)

            with open(filepath, "wb") as f:
                f.write(uploaded_file.read())

            new_entry = {
                "filename": filename,
                "title": title or uploaded_file.name,
                "subject": subject,
                "semester": semester,
                "uploaded_by": username,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            notes_df = notes_df.append(new_entry, ignore_index=True)
            notes_df.to_csv(META_FILE, index=False)

            st.success("✅ Notes uploaded successfully!")

# --- ALL USERS: Browse Notes ---
st.subheader("📚 Browse Notes")

sem_filter = st.selectbox("📘 Filter by Semester", sorted(notes_df["semester"].unique()) if not notes_df.empty else [])
sub_filter = st.selectbox("📗 Filter by Subject", sorted(notes_df["subject"].unique()) if not notes_df.empty else [])

filtered_notes = notes_df[
    (notes_df["semester"] == sem_filter) &
    (notes_df["subject"] == sub_filter)
] if sem_filter and sub_filter else pd.DataFrame()

if not filtered_notes.empty:
    for _, row in filtered_notes.iterrows():
        st.markdown(f"**📝 {row['title']}**")
        st.markdown(f"- 📚 Subject: `{row['subject']}` | 📘 Semester: `{row['semester']}`")
        st.markdown(f"- 👤 Uploaded by: `{row['uploaded_by']}` on `{row['timestamp']}`")

        file_path = os.path.join(NOTES_DIR, row["filename"])
        with open(file_path, "rb") as file:
            btn = st.download_button(
                label="📥 Download",
                data=file,
                file_name=row["filename"],
                mime="application/octet-stream"
            )
        st.markdown("---")
else:
    st.info("No notes available for this subject & semester.")
