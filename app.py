from fastapi import FastAPI
import pandas as pd
from agent import simulate_interest, parse_jd
from matcher import compute_match_scores

app = FastAPI()


@app.post("/run-agent/")
def run_agent(jd: str):
    df = pd.read_csv("data/candidates.csv")

    parsed = parse_jd(jd)
    jd_skills = " ".join(parsed["skills"])

    df = compute_match_scores(jd_skills, df)

    results = []

    for _, row in df.iterrows():
        interest_score, reply = simulate_interest(row, jd)

        # improved scoring
        final_score = 0.6 * row['match_score'] + 0.4 * interest_score

        # explainability
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
            "match_score": float(row['match_score']),
            "interest_score": interest_score,
            "final_score": round(final_score, 2),
            "response": reply,
            "reason": reason
        })

    return sorted(results, key=lambda x: x['final_score'], reverse=True)[:3]
