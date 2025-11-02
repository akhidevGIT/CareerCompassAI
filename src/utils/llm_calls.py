from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
import os
from typing_extensions import TypedDict

# environment variables
from dotenv import load_dotenv
load_dotenv()
MODEL = os.getenv("MODEL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM definition
llm = ChatGroq(
    model = MODEL, temperature=0.7, api_key= GROQ_API_KEY)

# JSON output parser from llm
parser = JsonOutputParser()

# state definition of your graph
class resume(TypedDict):
    resume_content: str
    experience_yrs: float
    education: list
    skills: list
    projects: list
    experience_roles: list
    desired_role: str
    experience_level: str
    match_score: float
    recommended_projects: list
    skills_to_improve: list
    top_roles: list
    final_feedback: str