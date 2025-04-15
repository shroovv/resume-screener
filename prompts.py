def resume_screening_prompt(resume_text, job_description):
    return f"""
You are an AI hiring assistant.

Your task is to read the following job description and resume, and respond by listing:
1. Positives: Clear matches between the resume and the job description
2. Negatives: Skills or experience required in the job description that are missing or weak in the resume

You must strictly respond in this format:
[Positives]
- Point 1
- Point 2
...

[Negatives]
- Point 1
- Point 2
...

Only use the information present in the resume. Do not make assumptions.

Job Description:
{job_description}

Resume:
{resume_text}
"""
