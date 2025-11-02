from typing_extensions import TypedDict
from src.agents.resume_parser_agent import resume_parser_agent
from src.agents.skill_analyzer_agent import skill_analyser_agent
from src.agents.role_match_agent import role_match_agent
from src.agents.alignment_explainer_agent import alignment_explainer_agent
from src.agents.skill_project_recommender_agent import skill_project_recommender_agent
from src.agents.feedback_agent import feedback_agent

from src.utils.llm_calls import resume

from .conditional_routes import route_after_role_match, route_after_skill_analysis




from langgraph.graph import StateGraph, START, END



def graph_builder(): 
    # Graph class initialisation
    builder = StateGraph(resume)       
    
    # Add nodes
    builder.add_node("resume_parser", resume_parser_agent)
    builder.add_node("skill_analyzer", skill_analyser_agent)
    builder.add_node("role_matcher", role_match_agent)
    builder.add_node("alignment_explainer", alignment_explainer_agent)
    builder.add_node("skill_project_suggester", skill_project_recommender_agent)
    builder.add_node("final_feedback", feedback_agent)


    # Add base edges
    builder.add_edge(START, "resume_parser")
    builder.add_edge("resume_parser", "skill_analyzer")

    # Conditional edges based on analyzer output
    builder.add_conditional_edges("skill_analyzer", route_after_skill_analysis,{
            "high_match": "final_feedback",
            "needs_role_analysis": "role_matcher"
        })

    builder.add_conditional_edges("role_matcher", route_after_role_match, {
            "alignment_needed": "alignment_explainer",
            "skills_needed": "skill_project_suggester"
        })

    # Continue from middle nodes to final
    builder.add_edge("alignment_explainer", "final_feedback")
    builder.add_edge("skill_project_suggester", "final_feedback")

    builder.add_edge("final_feedback", END)

    # Compile graph
    workflow = builder.compile()

    return workflow


