import streamlit as st
import requests

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🤖 AI Code Reviewer")

language = st.selectbox("Select Language", ["Python", "JavaScript", "Java"])

code = st.text_area("Paste your code here", height=300)

if st.button("Review Code"):
    if not code.strip():
        st.warning("Please enter some code")
    else:
        with st.spinner("AI is reviewing your code..."):
            response = requests.post(
                "http://127.0.0.1:8000/review",
                json={
                    "language": language,
                    "code": code
                }
            )

            if response.status_code == 200:
                st.subheader("AI Review")
                data = response.json()
                st.write(data.get("review", data))
                
            else:
                st.error("Backend error")