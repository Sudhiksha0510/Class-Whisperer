import streamlit as st
import datetime

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must log in to view this page.")
    st.stop()

# --- Prevent unauthenticated access ---
if "role" not in st.session_state:
    st.error("You must log in first.")
    st.stop()

# --- Initialize Doubts and Answers Store ---
if "doubts" not in st.session_state:
    st.session_state.doubts = []

# --- Word Filter Setup ---
ALLOWED_KEYWORDS = [
    "exam", "assignment", "topic", "lecture", "subject",
    "doubt", "question", "marks", "syllabus", "practical",
    "lab", "program", "unit", "deadline", "notes", "teacher"
]

def contains_allowed_keywords(text):
    return any(word in text.lower() for word in ALLOWED_KEYWORDS)

# --- Submit Doubt ---
st.markdown("## ❓ Ask a Doubt")

with st.form("ask_form"):
    doubt_text = st.text_area("Enter your doubt anonymously:", max_chars=500)
    uploaded_file = st.file_uploader("Attach file/image (optional)", type=["png", "jpg", "jpeg", "pdf"])
    submit = st.form_submit_button("Post Doubt")

    if submit:
        if not contains_allowed_keywords(doubt_text):
            st.warning("Please make sure your doubt is meaningful and subject-related.")
        elif len(doubt_text.strip()) < 10:
            st.warning("Your doubt is too short. Try to be more descriptive.")
        else:
            st.success("✅ Doubt posted anonymously!")
            st.session_state.doubts.append({
                "text": doubt_text.strip(),
                "file": uploaded_file.read() if uploaded_file else None,
                "filename": uploaded_file.name if uploaded_file else None,
                "answers": [],
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            })

# --- Display Doubts ---
st.markdown("---")
st.markdown("### 💬 Existing Doubts")

if len(st.session_state.doubts) == 0:
    st.info("No doubts have been posted yet.")

for idx, doubt in enumerate(reversed(st.session_state.doubts)):
    st.markdown(f"#### ❔ Doubt {len(st.session_state.doubts) - idx}")
    st.write(doubt["text"])
    st.caption(f"🕒 Posted on {doubt['timestamp']}")

    if doubt["file"]:
        if doubt["filename"].endswith((".png", ".jpg", ".jpeg")):
            st.image(doubt["file"], width=300)
        else:
            st.download_button("📎 Download Attachment", data=doubt["file"], file_name=doubt["filename"], key=f"download_{idx}")

    # Show answers
    if doubt["answers"]:
        st.markdown("**💡 Answers:**")
        for ans in doubt["answers"]:
            st.success(f"- {ans}")
    else:
        st.info("No answers yet. Be the first to reply!")

    # Answer input
    with st.form(f"answer_form_{idx}"):
        reply = st.text_input("Reply to this doubt:", key=f"input_{idx}")
        reply_btn = st.form_submit_button("Submit Answer")
        if reply_btn and reply.strip():
            doubt["answers"].append(reply.strip())
            st.success("Answer submitted!")

    st.markdown("---")

