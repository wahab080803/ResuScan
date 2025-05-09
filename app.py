# import streamlit as st
# import PyPDF2
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import re

# # Predefined skill keywords for comparison (you can expand this list)
# SKILL_KEYWORDS = [
#     "html", "css", "javascript", "react", "node", "express", "mongodb", "git", 
#     "github", "typescript", "next.js", "vue", "angular", "python", "java", 
#     "aws", "firebase", "graphql", "docker", "ci/cd", "restful", "apis", 
#     "seo", "agile", "scrum", "ui/ux", "responsive", "performance", "debugging"
# ]

# # Function to extract text from uploaded resume
# def extract_text_from_pdf(uploaded_file):
#     text = ""
#     reader = PyPDF2.PdfReader(uploaded_file)
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# # Function to analyze resume against job description
# def analyze_resume(job_desc, resume_text):
#     vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = vectorizer.fit_transform([job_desc, resume_text])
#     similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

#     # Extracting skills from job description and resume
#     job_keywords = set(re.findall(r'\b\w+\b', job_desc.lower()))
#     resume_keywords = set(re.findall(r'\b\w+\b', resume_text.lower()))

#     # Extract common skills from predefined skills list
#     matched_skills = set(SKILL_KEYWORDS).intersection(resume_keywords)
#     missing_skills = set(SKILL_KEYWORDS).difference(resume_keywords)

#     strengths = job_keywords.intersection(resume_keywords)
#     weaknesses = job_keywords.difference(resume_keywords)

#     return {
#         "score": round(similarity * 100, 2),
#         "strengths": list(strengths),
#         "weaknesses": list(weaknesses),
#         "matched_skills": list(matched_skills),
#         "missing_skills": list(missing_skills)
#     }

# # Streamlit UI
# st.title("📄 Smart Resume Analyzer")
# st.write("Analyze how well your resume matches a job description and highlight key skills.")

# job_description = st.text_area("🔍 Paste the Job Description Here")

# uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF)", type=["pdf"])

# if st.button("Analyze"):
#     if uploaded_file and job_description.strip():
#         with st.spinner("Analyzing..."):
#             resume_text = extract_text_from_pdf(uploaded_file)
#             result = analyze_resume(job_description, resume_text)

#         st.subheader("✅ Resume Match Score:")
#         st.progress(result["score"] / 100)
#         st.success(f"Score: {result['score']}%")

#         st.subheader("💪 Strengths Key (Matched Skills):")
#         if result["matched_skills"]:
#             st.write(", ".join(result["matched_skills"]))
#         else:
#             st.warning("No relevant skills found in the resume.")

#         st.subheader("⚠️Missing Skills (🛠 Weaknesses):")
#         if result["missing_skills"]:
#             st.write(", ".join(result["missing_skills"]))
#         else:
#             st.success("All relevant skills are covered in your resume!")

#     else:
#         st.error("Please upload a resume and paste a job description.")
