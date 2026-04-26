import streamlit as st
from agent import parse_jd, simulate_interest

st.title("TalentScout AI")
st.caption("AI Agent for automated talent scouting and engagement")

jd = st.text_area("Enter Job Description")

# Dummy candidates (you can later load from DB)
candidates = [
    {"name": "Aisha", "skills": "Python"},
    {"name": "Sneha", "skills": "Python SQL"},
    {"name": "Arjun", "skills": "Python"},
]

if st.button("Run Agent"):

    jd_data = parse_jd(jd)

    results = []

    for c in candidates:
        match_score = 0

        for skill in jd_data["skills"]:
            if skill.lower() in c["skills"].lower():
                match_score += 0.3

        match_score = min(match_score, 1.0)

        interest_score, response = simulate_interest(c, jd)

        final_score = round((match_score + interest_score) / 2, 2)

        results.append({
            "name": c["name"],
            "match_score": match_score,
            "interest_score": interest_score,
            "final_score": final_score,
            "response": response,
            "reason": f"Matched skills: {c['skills']}"
        })

    # Sort by best match
    results = sorted(results, key=lambda x: x["final_score"], reverse=True)

    # Display
    for r in results:
        st.subheader(f"👤 {r['name']}")
        st.progress(r['final_score'])

        col1, col2 = st.columns(2)
        col1.metric("Match Score", round(r['match_score'], 2))
        col2.metric("Interest Score", r['interest_score'])

        st.write("💬 Candidate Response:")
        st.info(r['response'])

        st.write("📌 Reason:")
        st.success(r["reason"])

        st.divider()

