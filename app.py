import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_analyzer import analyze_resume
from utils.resume_utils import extract_resume_skills

st.sidebar.title("🤖 AI Resume Analyzer")

st.sidebar.write("### Built With")

st.sidebar.write("""
- Python
- Streamlit
- Google Gemini AI
- PyPDF2
""")

st.sidebar.write("---")

st.sidebar.info(
    "Upload your resume and compare it with any job description."
)

st.title("🤖 AI Resume Analyzer")

st.caption(
    "Analyze your resume against any job description using Google Gemini AI."
)
st.write ("Upload resume and paste a job description")
st.subheader("Upload Resume")

resume = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)
st.subheader("Job Description")

job_description = st.text_area(
    "Paste the job description here"
)

if st.button(
    "Analyze Resume",
    use_container_width=True
):
    if resume is None:
        st.warning ("please upload a resume")
    elif job_description == "":
        st.warning ("Please enter a job description")
    else:
        resume_text = extract_text_from_pdf(resume)
        resume_skills = extract_resume_skills(resume_text)

        st.success("Resume uploaded successfully!")

        with st.expander("View Extracted Resume Text"):
            st.text_area(
                "Resume Text",
                resume_text,
                height=300
            )

        
        st.subheader("Skills Found")

        if len(resume_skills) > 0:
            for skill in resume_skills:
                st.write(f"{skill.title()}")
        else:
            st.info("No matching skills found.")
        
        st.divider()
        st.subheader("AI Resume Analysis")

        with st.spinner("🤖 Gemini AI is analyzing your resume..."):

            analysis = analyze_resume(
            resume_text,
            job_description
        )
        st.success("Analysis Complete!")    

        st.write(analysis)

st.markdown("---")

st.caption(
    "Made by Priyanka Mohan | Powered by Python, Streamlit & Gemini AI 🤖"
)        