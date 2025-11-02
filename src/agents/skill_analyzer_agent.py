from langchain_core.prompts import ChatPromptTemplate
from src.utils.llm_calls import llm, parser, resume


# Skill Analyzer Agent
def skill_analyser_agent(state:resume) -> resume:
  resume_text = state.get("resume_content", "")
  desired_role = state.get("desired_role", "")

  prompt = ChatPromptTemplate.from_template(
      f"""
        You are an expert career coach AI.

        Analyze the following resume and evaluate the candidate's experience level and suitability for a target job role.

        ### Resume:
        {resume_text}

        ### Target Role:
        {desired_role}

        Your tasks:
        1. **Categorize** the candidate as one of:
          - "Entry-level" → 0–2 years experience or mostly academic/internship experience
          - "Mid-level" → 2–6 years experience or mix of independent and collaborative work
          - "Senior-level" → 6+ years experience or leadership/project ownership

        2. **Estimate a Match Score (0–100)** that reflects how well this resume aligns with the target role, based on skills, experience, and context.

        3. Keep the output concise and structured in **JSON** format with two keys:

            "experience_level": "<Entry-level | Mid-level | Senior-level>",
            "match_score": <number between 0 and 100>

          """
        )
  chain = prompt | llm
  # llm invoke
  result = chain.invoke({"resume_text": resume_text, "desired_role": desired_role}).content
  # parse llm JSON output
  skill_analysis = parser.parse(result)

  return {"experience_level": skill_analysis["experience_level"], "match_score": skill_analysis["match_score"]}