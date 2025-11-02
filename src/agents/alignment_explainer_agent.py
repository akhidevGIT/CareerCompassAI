from langchain_core.prompts import ChatPromptTemplate
from src.utils.llm_calls import llm, parser, resume

def alignment_explainer_agent(state: resume) -> resume:
    resume_text = state.get("resume_content", "")
    desired_role = state.get("desired_role", "")
    top_roles = state.get("top_roles", [])

    prompt = ChatPromptTemplate.from_template(
        f"""
        You are a recruiter AI. The candidate applied for the role "{desired_role}",
        but your analysis shows their top suggested roles are: {top_roles}.

        Explain clearly *why* their resume: {resume_text}  may not align well with the desired role,
        and what they can change (skills, keywords, or experience emphasis)
        to improve their alignment.

        Return only plain text feedback (no JSON).
        """
    )

    chain = prompt | llm
    # llm invoke
    feedback = chain.invoke({"resume_text": resume_text, "desired_role": desired_role, "top_roles": top_roles}).content
    return {"final_feedback": feedback}
