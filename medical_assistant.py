import streamlit as st
import random
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_data
def load_questions(path='questions.txt'):
    with open(path, 'r') as f:
        return [q.strip() for q in f.readlines() if q.strip()]

@st.cache_data
def load_keywords(path='keywords.json'):
    with open(path, 'r') as f:
        return json.load(f)

def preprocess(text):
    return text.lower().strip()

def compute_similarity(reference, candidate):
    ref_emb = model.encode([preprocess(reference)], convert_to_tensor=True)
    cand_emb = model.encode([preprocess(candidate)], convert_to_tensor=True)
    return float(cosine_similarity(ref_emb, cand_emb)[0][0])

def keyword_penalty(answer, keywords):
    missing = [kw for kw in keywords if kw.lower() not in answer.lower()]
    penalty = (len(missing) / max(len(keywords), 1)) * 0.4
    return penalty, missing

def grade_answer(reference, candidate, keywords):
    sim = compute_similarity(reference, candidate)
    penalty, missing = keyword_penalty(candidate, keywords)
    final_score = max(sim - penalty, 0.0)
    return {
        "similarity": round(sim, 3),
        "penalty": round(penalty, 3),
        "score": round(final_score, 3),
        "missing_keywords": missing
    }

# UI
st.set_page_config(page_title="🧑‍⚕️ Medical QA Assistant", page_icon="💊")
st.title("🧠 Medical QA Assistant")
st.markdown("Answer medical questions and get graded based on meaning and keyword coverage.")

questions = load_questions()
keywords = load_keywords()
question = st.selectbox("📘 Choose a question:", questions)
user_answer = st.text_area("✍️ Type your answer here:")

if st.button("📝 Grade my answer"):
    if user_answer.strip() == "":
        st.warning("Please type an answer.")
    else:
        reference = " ".join(keywords[question])  # reference approximation
        result = grade_answer(reference, user_answer, keywords[question])

        st.success("✅ Grading Complete")
        st.markdown(f"**Similarity Score:** {result['similarity']}")
        st.markdown(f"**Keyword Penalty:** {result['penalty']}")
        st.markdown(f"**Final Score (0–1):** {result['score']}")

        if result['missing_keywords']:
            st.warning(f"⚠️ Missing keywords: `{', '.join(result['missing_keywords'])}`")
        else:
            st.info("✅ Great! You covered all the keywords.")

        with st.expander("📚 Reference Keywords"):
            st.code(", ".join(keywords[question]), language='text')
