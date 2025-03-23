import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🎨 **Streamlit Theme Customization**
st.set_page_config(
    page_title="Resume Ranking System",
    page_icon="📄",
    layout="wide"
)

# 📌 **Header**
st.title("📄 AI-Powered Resume Ranking System")

st.markdown(
    "🚀 Upload resumes and compare them against a job description to find the best match using AI-powered similarity scoring.",
    unsafe_allow_html=True
)

st.divider()  # Adds a professional divider

# 🔹 **Layout: Job Description & Resume Upload Side by Side**
col1, col2 = st.columns([1.2, 1.8])

with col1:
    st.subheader("📝 Job Description")
    job_description = st.text_area("Enter the job description...", height=180)

with col2:
    st.subheader("📂 Upload Resumes (PDF)")
    uploaded_files = st.file_uploader("Upload multiple PDF resumes", type=["pdf"], accept_multiple_files=True)

st.divider()  # Adds a professional divider

# 📌 **Extract Text from PDF Resumes**
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = "".join([page.extract_text() or "" for page in pdf.pages])
    return text.strip()

# 📌 **Rank Resumes Using TF-IDF & Cosine Similarity**
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_desc_vector = vectors[0]
    resume_vectors = vectors[1:]
    return cosine_similarity([job_desc_vector], resume_vectors).flatten()

# 📌 **AI Suggestions for Resume Improvement**
def generate_resume_tips(score):
    if score > 80:
        return "✅ Excellent match! Resume is well-optimized."
    elif score > 60:
        return "🔹 Good match! Add more relevant keywords."
    else:
        return "⚡ Low match! Improve your skills section & use industry-specific terms."

# 📌 **Processing & Displaying Results**
if uploaded_files and job_description:
    st.subheader("📊 Resume Rankings")

    resumes = [extract_text_from_pdf(file) for file in uploaded_files]

    # 📌 **Loading Animation**
    with st.spinner("Analyzing resumes... Please wait ⏳"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)

        scores = rank_resumes(job_description, resumes)

    # 📌 **Results Dataframe**
    results_df = pd.DataFrame({
        "Resume": [file.name for file in uploaded_files],
        "Match Score (%)": (scores * 100).round(2),
        "AI Suggestion": [generate_resume_tips(score * 100) for score in scores]
    }).sort_values(by="Match Score (%)", ascending=False)

    st.success(f"✅ Ranking Complete! 🎯 Top Match: **{results_df.iloc[0]['Resume']}**")

    # 📌 **Styled Table for Professional Look**
    st.dataframe(results_df.style.format({"Match Score (%)": "{:.2f}"}))

st.markdown(
    "<br><hr><p style='text-align:center;'>© 2025 AI Resume Ranking System | Powered by NLP & Machine Learning</p>",
    unsafe_allow_html=True
)
