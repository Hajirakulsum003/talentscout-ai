import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_match_scores(jd_skills, df):
    scores = []

    for _, row in df.iterrows():
        text = [jd_skills, row['skills']]
        vectorizer = CountVectorizer().fit_transform(text)
        vectors = vectorizer.toarray()

        score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
        scores.append(score)

    df['match_score'] = scores
    return df
