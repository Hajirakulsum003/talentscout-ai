import random


def parse_jd(jd_text):
    jd_text = jd_text.lower()

    skills = []

    if "python" in jd_text:
        skills.append("Python")
    if "sql" in jd_text:
        skills.append("SQL")
    if "machine learning" in jd_text or "ml" in jd_text:
        skills.append("ML")
    if "nlp" in jd_text:
        skills.append("NLP")

    return {
        "skills": skills
    }


def simulate_interest(candidate, jd_text):
    jd_text = jd_text.lower()
    skills = candidate['skills'].lower()

    score = 0.5

    if "python" in jd_text and "python" in skills:
        score += 0.2
    if "ml" in jd_text and "ml" in skills:
        score += 0.2
    if "sql" in jd_text and "sql" in skills:
        score += 0.1

    score = min(score + random.uniform(-0.1, 0.1), 1.0)

    if score > 0.7:
        response = "Yes, I am very interested in this role."
    elif score > 0.5:
        response = "I might be interested, can you share more details?"
    else:
        response = "Not very interested at the moment."

    return round(score, 2), response
