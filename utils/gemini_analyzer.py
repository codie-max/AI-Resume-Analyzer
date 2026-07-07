import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are a Senior HR Recruiter and ATS Resume Screening Expert with over 15 years of experience.

Your task is to compare the candidate's resume with the provided job description.

Resume:
{resume_text}

Job Description:
{job_description}

Evaluate the resume using the following ATS scoring criteria:

1. Skills Match (40 points)
2. Projects & Experience (25 points)
3. Education & Certifications (15 points)
4. Keyword Match (10 points)
5. Resume Quality & Clarity (10 points)

Calculate the total ATS Score out of 100.

Return the result in Markdown format.

Use the following structure:

# ATS Score
- Overall Score: XX/100

## Score Breakdown
- Skills Match: XX/40
- Projects & Experience: XX/25
- Education & Certifications: XX/15
- Keyword Match: XX/10
- Resume Quality: XX/10

Briefly explain why each score was given.

# Matching Skills

# Missing Skills

# Missing Keywords

# Strengths

# Weaknesses

# Resume Improvements
Suggest at least five actionable improvements.

# Final Recommendation

# Interview Probability

Estimate the probability of getting shortlisted for an interview.

Choose one:

🟢 High (80–100%)

🟡 Medium (50–79%)

🔴 Low (Below 50%)

Briefly explain your reasoning.

Choose ONLY one:
- Highly Recommended
- Recommended
- Needs Improvement
- Not Recommended

Keep the response concise, professional, and use bullet points wherever possible.
"""

    response = model.generate_content(prompt)

    return response.text