from langchain_core.prompts import ChatPromptTemplate

from src.utils.llm_calls import llm, parser, resume

#Skill and Project Suggester Agent (uses LLM to suggest skills and projects to close skill gaps)
def skill_project_recommender_agent(state:resume) -> resume:
  resume_text = state.get("resume_content", "")
  desired_role = state.get("desired_role", "")

  prompt = ChatPromptTemplate.from_template(
      f"""
      You are an expert career mentor AI helping candidates improve their resumes for specific roles.

      Analyze the following information and give actionable suggestions.

      ### Resume:
      {resume_text}

      ### Target Role:
      {desired_role}

      Your tasks:
      1. Review the candidate’s resume to understand their current skills, experience, and domain knowledge.
      2. Compare their profile with the typical expectations for the target role.
      3. Suggest:
        - **3 Projects** the candidate can build or contribute to that would make their portfolio stand out for this role.
        - **3 Skills** they should improve or learn to strengthen their fit.

      Format the output in **JSON** format with two keys in this exact structure:

      "recommended_projects": [<project 1>, <project 2>, <project 3>],
      "skills_to_improve": [<skill 1>, <skill 2>, <skill 3>]

      """
  )

  chain = prompt | llm
  #llm invoke
  result = chain.invoke({"resume_text": resume_text, "desired_role": desired_role}).content
  #parse JSON output
  skill_projects_recom = parser.parse(result)

  return {"recommended_projects": skill_projects_recom["recommended_projects"], "skills_to_improve": skill_projects_recom["skills_to_improve"]}

