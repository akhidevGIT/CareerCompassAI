from langchain_core.prompts import ChatPromptTemplate
from src.utils.llm_calls import llm, parser, resume


# Resume Parser Agent (uses LLM to extract structured info in JSON)
def resume_parser_agent(state: resume) -> resume:
  resume_text = state.get("resume_content", "")

  prompt = ChatPromptTemplate.from_template(
      f""" Extract the following fields from the resume text.
      Return only valid JSON with keys: : years_experience (float: calculate years of experience including months e.g. 2.5), experience_roles (list of job roles as short strings), skills (list of short lower-case tokens), projects (list of short strings), education (list of short strings).
      If a field is unknown or cannot be determined, set it to null or an empty list.
      Resume text:  {resume_text}
      """
  )

  chain = prompt|llm
  #llm invoke
  result = chain.invoke({"resume_text": resume_text}).content

  #parse llm JSON output
  parsed_content = parser.parse(result)

  experience_yrs = parsed_content["years_experience"]
  experience_roles = parsed_content["experience_roles"]
  education = parsed_content["education"]
  skills = parsed_content["skills"]
  projects = parsed_content["projects"]

  return {"experience_yrs": experience_yrs, "experience_roles":experience_roles, "education": education, "skills": skills, "projects": projects}

