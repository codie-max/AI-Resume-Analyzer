from utils.skills import skill_keywords

def extract_resume_skills(resume_text):
    resume_text_lower = resume_text.lower()

    resume_skills = []

    for skill in skill_keywords:
        if skill in resume_text_lower:
            resume_skills.append(skill)

    return resume_skills