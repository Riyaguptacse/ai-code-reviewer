import streamlit as st
import requests

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI Code Reviewer")

language = st.selectbox("Select Language", ["Python", "JavaScript", "Java"])

code = st.text_area("Paste your code here", height=300)

def call_api():
    for i in range(3):
        try:
            r = requests.post(
                "https://ai-code-reviewer-1-n718.onrender.com/review",
                json={
                    "language": language,
                    "code": code
                },
                timeout=30
            )

            if r.status_code == 200:
                return r.json()

        except Exception:
            time.sleep(2)

    return {"review": "Server is waking up, please retry."}


if st.button("Review Code"):
    with st.spinner("Reviewing..."):
        result = call_api()
        st.subheader("AI Review")
        st.write(result.get("review"))