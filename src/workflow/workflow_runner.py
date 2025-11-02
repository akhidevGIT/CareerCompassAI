from .graph_builder import graph_builder

# compiled graph
graph_workflow = graph_builder()


def run_resume_screening(cv: str, role: str):
  
  results = graph_workflow.invoke({"resume_content" : cv, "desired_role": role})

  return {
    "experience_yrs": results.get('experience_yrs', 0),
    "education": results.get('education', []),
    "skills": results.get('skills', []),
    "projects": results.get('projects', []),
    "desired_role": results.get('desired_role',""),
    "experience_level": results.get('experience_level', ""),
    "match_score": results.get('match_score', 0),
    "recommended_projects": results.get('recommended_projects', []),
    "skills_to_improve": results.get('skills_to_improve', []),
    "top_roles": results.get('top_roles', []),
    "final_feedback": results.get('final_feedback', "")
  }