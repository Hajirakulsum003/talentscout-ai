# 🚀 TalentScout AI – AI-Powered Talent Scouting & Engagement Agent

## 🔹 Overview

TalentScout AI is an intelligent recruitment agent that automates the candidate sourcing and engagement process.
It takes a Job Description (JD) as input, identifies suitable candidates, evaluates their skill alignment, simulates candidate interest, and produces a ranked shortlist.

This system helps recruiters **reduce manual effort** and make faster, data-driven hiring decisions.

---

## 🔹 Problem Statement

Recruiters spend significant time:

- Filtering candidate profiles manually
- Assessing skill alignment
- Following up to gauge candidate interest

This leads to inefficiency and delayed hiring.

---

## 🔹 Solution

TalentScout AI automates this pipeline by:

- Parsing job descriptions
- Matching candidates based on skills
- Simulating engagement to estimate interest
- Generating a ranked shortlist with explainability

---

## 🔹 Key Features

- 📄 **Job Description Parsing**
  Extracts relevant skills from input JD

- 🔍 **Candidate Matching Engine**
  Uses similarity-based scoring to match candidates

- 💬 **Interest Simulation Agent**
  Simulates candidate responses to evaluate interest

- 📊 **Dual Scoring System**
  - Match Score → Skill alignment
  - Interest Score → Engagement likelihood

- 📌 **Explainability**
  Displays matched skills for transparency

- 🏆 **Ranked Shortlist**
  Provides top candidates ready for recruiter action

---

## 🔹 Architecture

```
User Input (Job Description)
            ↓
     JD Parsing Module
            ↓
   Candidate Matching Engine
            ↓
   Interest Simulation Agent
            ↓
        Scoring Engine
            ↓
   Ranked Candidate Output
```

---

## 🔹 Tech Stack

- **Python**
- **FastAPI** – Backend API
- **Streamlit** – Interactive UI
- **Pandas** – Data handling
- **Scikit-learn** – Similarity computation

---

## 🔹 Scoring Logic

- **Match Score:**
  Computed using cosine similarity between JD skills and candidate skills

- **Interest Score:**
  Generated using rule-based conversational simulation

- **Final Score:**

```
Final Score = (0.6 × Match Score) + (0.4 × Interest Score)
```

---

## 🔹 Explainability

Each candidate includes a reason such as:

> “Matched skills: Python, ML”

This helps recruiters understand **why a candidate is shortlisted**.

---

## 🔹 How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run backend
python -m uvicorn app:app --reload

# Run frontend
python -m streamlit run ui.py
```

---

## 🔹 Sample Input

```
We are hiring a Python Developer with Machine Learning and SQL skills.
Experience: 0-2 years.
```

---

## 🔹 Sample Output

- Ranked list of candidates
- Match Score
- Interest Score
- Candidate response
- Reason for selection

---

## 🔹 Demo Video

link

---

## 🔹 Repository Structure

```
talentscout-ai/
│── app.py
│── agent.py
│── matcher.py
│── ui.py
│── requirements.txt
│── README.md
│── data/
│   └── candidates.csv
```

---

## 🔹 Future Improvements

- Integration with LinkedIn / job portals
- Real-time candidate communication
- LLM-based advanced conversations
- Vector database for scalable search

---

## 🔹 Conclusion

TalentScout AI demonstrates how intelligent automation can streamline recruitment workflows by combining candidate matching, engagement simulation, and explainable ranking into a single system.

---

## 👩‍💻 Author

**Hajira Kulsum**
