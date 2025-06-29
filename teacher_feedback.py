import streamlit as st
import pandas as pd
import os
from textblob import TextBlob
import plotly.express as px

def show():
    st.title("📝 Teacher Feedback")
    st.write("Provide or view teacher feedback here.")

st.set_page_config(page_title="Teachers Feedback", layout="wide")

# --- Ensure data folder exists ---
os.makedirs("data", exist_ok=True)
FEEDBACK_FILE = "data/teacher_feedback.csv"

# --- Role Restriction ---
if "role" not in st.session_state:
    st.error("You must be logged in.")
    st.stop()

# --- Header ---
st.markdown("## 📜 Teachers Feedback")

# --- Load existing feedback ---
if os.path.exists(FEEDBACK_FILE):
    feedback_df = pd.read_csv(FEEDBACK_FILE)
else:
    feedback_df = pd.DataFrame(columns=["teacher", "subject", "feedback", "clarity", "supportiveness", "punctuality"])

# --- Feedback Input (Only students can submit) ---
if st.session_state.role == "student":
    st.markdown("### ✍️ Submit Feedback")
    teacher = st.selectbox("Select Teacher", ["Mr. Sharma", "Ms. Reddy", "Dr. Khan", "Mrs. Patel"])
    subject = st.selectbox("Subject Taught", ["Math", "Physics", "BEE", "Chemistry"])
    feedback = st.text_area("Your Review", max_chars=500)

    st.markdown("### ⭐ Rate the Teacher (1-5 Stars)")
    clarity = st.radio("Clarity of Explanation", [1, 2, 3, 4, 5], index=2, horizontal=True)
    supportiveness = st.radio("Supportiveness", [1, 2, 3, 4, 5], index=2, horizontal=True)
    punctuality = st.radio("Punctuality", [1, 2, 3, 4, 5], index=2, horizontal=True)

    if st.button("Submit Feedback") and feedback:
        new_entry = pd.DataFrame([[teacher, subject, feedback, clarity, supportiveness, punctuality]], 
                                 columns=["teacher", "subject", "feedback", "clarity", "supportiveness", "punctuality"])
        feedback_df = pd.concat([feedback_df, new_entry], ignore_index=True)
        feedback_df.to_csv(FEEDBACK_FILE, index=False)
        st.success("Thank you for your feedback!")

# --- Helper: Filter Positive Feedback ---
def clean_and_analyze(df):
    if df.empty:
        return pd.DataFrame()

    df = df.copy()
    df["sentiment"] = df["feedback"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df["label"] = df["sentiment"].apply(lambda x: "Nice" if x > 0.2 else "Ignored")
    return df[df["label"] == "Nice"]

# --- Display Graph ---
st.markdown("---")
st.markdown("### 📊 Teacher Feedback Summary")

filtered_df = clean_and_analyze(feedback_df)

if not filtered_df.empty:
    numeric_cols = ["clarity", "supportiveness", "punctuality"]
    filtered_df[numeric_cols] = filtered_df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    chart_data = filtered_df.groupby(["teacher", "subject"]).size().reset_index(name="count")
    fig = px.bar(chart_data, x="teacher", y="count", color="subject", barmode="group",
                 title="Positive Feedback Count per Teacher and Subject")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📊 Average Ratings")
    avg_ratings = filtered_df.groupby("teacher")[numeric_cols].mean().reset_index()

    # ✅ Fix: Format only numeric columns
    numeric_only = avg_ratings.select_dtypes(include='number').columns
    st.dataframe(avg_ratings.style.format({col: "{:.2f}" for col in numeric_only}))

    st.markdown("#### All Positive Reviews")
    for _, row in filtered_df.iterrows():
        st.info(f"**{row['teacher']} ({row['subject']}):** {row['feedback']}")
else:
    st.warning("No positive feedback available yet. Encourage students to submit!")
