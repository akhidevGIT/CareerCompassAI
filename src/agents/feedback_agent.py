from langchain_core.prompts import ChatPromptTemplate
from src.utils.llm_calls import llm, parser, resume


#Feedback Agent (compose final textual feedback using LLM)
def feedback_agent(state: resume) -> resume:

    resume_text = state.get("resume_content","")
    desired_role = state.get("desired_role","")
    experience_level = state.get("experience_level", "")
    top_roles = state.get("top_roles", [])
    match_score = state.get("match_score", 0)
    projects = state.get("recommended_projects", [])
    skills_plan = state.get("skills_to_improve", [])
    explanation = state.get("final_feedback", "")  # might contain alignment feedback if previous step

    # ----- Dynamic prompt construction ------
    prompt_text = f"""
    You are an expert career coach. Summarize the candidate’s resume evaluation
    and generate a clear, short feedback report in bullet points.

    ### Resume Summary:
    {resume_text}

    ### Target Role:
    {desired_role}

    ### Profile Summary:
    - Experience Level: {experience_level}
    - Resume Match Score: {match_score if match_score else "N/A"}
    - Suggested Roles: {top_roles if top_roles else "Not determined"}

    """

    # Add dynamic context depending on flow
    if match_score and match_score >= 80:
        prompt_text += """
        The candidate is already a strong fit for this role.
        Highlight their strengths and reassure them that their profile aligns well.
        Suggest any final polish tips or portfolio improvements.
        """

    elif "Senior-level" in experience_level.lower() and match_score and match_score >= 50:
        prompt_text += """
        The candidate is senior-level.
        Focus feedback on leadership visibility, mentoring, and impact demonstration.
        """

    elif explanation:
        prompt_text += f"""
        There was some role alignment feedback generated:
        {explanation}
        Please integrate this insight into the summary.
        """

    else:
        prompt_text += f"""
        Provide improvement recommendations and skill-building actions.
        If available, include these project and skill suggestions:
        - Projects: {projects}
        - Skills to improve: {skills_plan}
        """

    prompt_text += """
    Format the output as:
    **Strengths**
    - ...
    **Areas to Improve**
    - ...
    **Actionable Suggestions**
    - ...
    Keep it under 200 words.
    """

    # ---- LLM Call ----
    prompt = ChatPromptTemplate.from_template(prompt_text)
    chain = prompt | llm
    feedback_text = chain.invoke({"resume_text": resume_text, "desired_role": desired_role}).content

    return {"final_feedback": feedback_text}
