AI Resume Screening & Ranking System

This project is an AI-powered resume screening and ranking system built using Streamlit, scikit-learn, and PyPDF2. The application allows users to upload multiple resumes in PDF format, compare them to a given job description, and rank them based on cosine similarity using TF-IDF.  

Features: 

Upload multiple PDF resumes  
Enter a job description to compare resumes  
 Uses TF-IDF & Cosine Similarity for ranking  
Displays ranked resumes with match scores & AI suggestions
Provides resume improvement tips  

Folder Structure:

resume_screening_app/

│── .venv/

│── app.py

│── requirements.txt

│── data/

│   ├── sample_resume.pdf

│── README.md

│── .gitignore


Installation & Setup:

1.Clone the Repository 

git clone https://github.com/DuhithB/AI-powered-resume-screening-and-ranking-system

cd AI-Resume-Ranking-System

2.(Optional) Create a Virtual Environment
python -m venv .venv

Activate the virtual environment:
- Windows:
  .venv\Scripts\activate
 
- Mac/Linux: 
  source .venv/bin/activate

3.Install Dependencies
pip install -r requirements.txt

4. Run the Application
streamlit run app.py


The app will open in your default web browser at `localhost:8501`  

How It Works:

Upload PDF resumes using the file uploader.  
Enter a job description in the provided text area.  
The system extracts text from resumes using PyPDF2.  
Converts job descriptions & resumes into TF-IDF vectors.  
Computes cosine similarity between resumes & job description.  
Ranks resumes based on match score & provides AI-powered tips.  


Deployment:

Deploy on Streamlit Cloud (Free)
Push your project to GitHub.  
Go to Streamlit Cloud and log in.  
Click New App, select your GitHub repository.  
Set the file path to app.py.  
Click Deploy  

Requirements:
streamlit
PyPDF2
pandas
scikit-learn
numpy

Install all dependencies using:  
pip install -r requirements.txt


Who Can Use This?

- HR & Recruiters
- Hiring Managers  
- Job Portals
- AI Enthusiasts & Students.  

Future Enhancements:

AI-Based Scoring– Use ML/Deep Learning for more accurate ranking.  
Advanced NLP – Integrate BERT/GPT for deeper text analysis.  
Multi-Format Support – Add support for DOCX, TXT & OCR.  
Skill Matching – Extract skills & experience automatically.  
API Integration – Connect with job portals & HR systems.  

Conclusion:

This AI-powered Resume Screening & Ranking System simplifies the resume screening process by automating ranking using TF-IDF & Cosine Similarity. With PDF text extraction, real-time ranking, and easy deployment, this project provides an efficient, scalable, and user-friendly solution for recruiters, hiring managers, and job portals
