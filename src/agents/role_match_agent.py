from langchain_core.prompts import ChatPromptTemplate

from src.utils.llm_calls import llm, parser, resume


# Role Matcher Agent
def role_match_agent(state:resume) -> resume:
  resume_text = state.get("resume_content", "")

  prompt = ChatPromptTemplate.from_template(
      f"""
      You are a career coach AI. Analyze this resume and suggest top 3 job roles
      that fit the candidate based on their skills and experience.

      Resume summary:
      {resume_text}

      Return only valid JSON with key:  top_roles (list of 3 job titles as short strings)

      """
  )
  chain = prompt|llm
  #llm invoke
  role_match_content = chain.invoke({"resume_text": resume_text}).content
  #parse llm JSON output
  parsed_content = parser.parse(role_match_content)


  return {"top_roles": parsed_content['top_roles']}

