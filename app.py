import streamlit as st
import pandas as pd
from agent import simulate_interest, parse_jd
from matcher import compute_match_scores

st.title("TalentScout AI")

jd = st.text_area("Enter Job Description")

if st.button("Run Matching"):
    df = pd.read_csv("candidates.csv")

    parsed = parse_jd(jd)
    jd_skills = " ".join(parsed["skills"])

    df = compute_match_scores(jd_skills, df)

    results = []

    for _, row in df.iterrows():
        interest_score, reply = simulate_interest(row, jd)

        final_score = 0.6 * row['match_score'] + 0.4 * interest_score

        matched_skills = []
        if "python" in row['skills'].lower() and "python" in jd.lower():
            matched_skills.append("Python")
        if "ml" in row['skills'].lower() and "ml" in jd.lower():
            matched_skills.append("ML")
        if "sql" in row['skills'].lower() and "sql" in jd.lower():
            matched_skills.append("SQL")

        reason = (
            f"Matched skills: {', '.join(matched_skills)}"
            if matched_skills else "Low skill overlap"
        )

        results.append({
            "name": row['name'],
            "final_score": round(final_score, 2),
            "reason": reason
        })

    results = sorted(results, key=lambda x: x['final_score'], reverse=True)[:3]

    st.write(results)

