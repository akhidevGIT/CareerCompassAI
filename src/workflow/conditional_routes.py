from .graph_builder import resume


# Define route functions
def route_after_skill_analysis(state: resume):
    """
    Route decisions after the skill analyzer agent.
    If score or experience level indicates strong fit → skip deeper analysis.
    Otherwise → go to role_matcher for further evaluation.
    """
    score = state.get("match_score", 0)
    level = state.get("experience_level", "")

    if score >= 80 or "Senior-level" in level:
        return "high_match"

    return "needs_role_analysis"

def route_after_role_match(state: resume):
    """
    Route decisions after the role matcher agent.
    If desired role is not in top roles → explain alignment.
    Otherwise → recommend skill & project improvements.
    """
    desired = state.get("desired_role", "").lower()
    top_roles = [r.lower() for r in state.get("top_roles", [])]
    if desired not in top_roles:
        return "alignment_needed"
    return "skills_needed"

