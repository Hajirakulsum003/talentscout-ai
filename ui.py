import streamlit as st
import requests

st.title("TalentScout AI")
st.caption("AI Agent for automated talent scouting and engagement")

jd = st.text_area("Enter Job Description")

if st.button("Run Agent"):
    res = requests.post("http://127.0.0.1:8000/run-agent/", params={"jd": jd})

    if res.status_code == 200:
        data = res.json()

        for r in data:
            st.subheader(f"👤 {r['name']}")

            st.progress(r['final_score'])

            col1, col2 = st.columns(2)
            col1.metric("Match Score", round(r['match_score'], 2))
            col2.metric("Interest Score", r['interest_score'])

            st.write("💬 Candidate Response:")
            st.info(r['response'])

            st.write("📌 Reason:")
            st.success(r.get("reason", "Skill match based on JD"))

            st.divider()
    else:
        st.error("Error connecting to backend")
