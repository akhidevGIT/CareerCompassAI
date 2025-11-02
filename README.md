# 🧭 CareerCompass AI
## Your Intelligent Resume Evaluator & Career Path Guide

**CareerCompass AI** is a multi-agent career assistant that analyzes your resume, identifies your skill alignment with a desired role, and offers personalized insights such as:

- Experience categorization (Entry / Mid / Senior level)
- Role match scoring
- Top matching roles
- Projects to help your resume stand out
- Skills to improve for your target role

This project showcases the power of LangGraph, Groq LLMs, and Streamlit in building an intelligent agent system that can reason, make conditional decisions, and provide contextual feedback dynamically.

## Key Features
- AI-Powered Resume Analysis — Automatically parses your uploaded resume and evaluates your experience level.
- Role Match Reasoning — Compares your skills with the target job role and provides a match score.
- Dynamic Agent Workflow — Agents collaborate and decide which steps to take next (e.g., skip improvement suggestions if score is high).
- Personalized Career Feedback — Suggests projects, skill upgrades, and role alignment explanations.
- Clean Streamlit UI — Upload your resume and get an instant feedback report.

## Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **LLM Backend** | Groq API |
| **Agent Framework** | LangGraph |

## Agent Roles

| Agent | Purpose |
|------------|-------------|
| Resume Parser | Extracts clean text and key info (skills, experience) from the uploaded resume |
| Skill Analyzer | Evaluates candidate’s experience level and computes an initial role match score |
| Role Matcher | Suggests top roles based on resume skills and target role |
| Alignment Explainer | Explains skill gaps or why the resume might not fit the desired role |
| Skill & Project Recommender | Suggests standout projects and skill improvements |
| Feedback Agent | Compiles all results into a structured, human-readable feedback summary |

## Installation

```bash
# Clone the repo
git clone https://github.com/akhidevGIT/CareerCompassAI.git
cd CareerCompassAI

# Create environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

## Environment Setup
Create a .env file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key
MODEL=your_llm_model_name
```
## Run Locally
Launch streamlit UI locally
```bash
streamlit run app/app.py
```
## 💡 How It Works

1. Upload your resume (PDF or TXT).

2. Enter your desired role (e.g., “Data Scientist”).

3. Click “Analyze”.

4. The agents collaboratively process your resume, evaluate your profile, and decide:
    - whether to suggest improvements
    - whether to explain skill alignment
    - or skip straight to final feedback.
5. Results are displayed with expanders in the Streamlit dashboard.

## Future Enhancements
- Use vector search for skill-role matching. Enhancing your system’s reasoning by storing roles and their required skills in a vector database, and matching user resume embeddings to the most relevant roles or job descriptions — rather than relying purely on LLM text matching.

Example Flow:

```scss
Resume → Extracted skills → Vector Embedding
                    ↓
             Vector Search (FAISS)
                    ↓
        Top matching roles → LLM Refinement
                    ↓
          “Your best-fit roles are: Data Analyst, ML Engineer, BI Specialist”
```          


## 🧑‍💻 Author

Akhila Devarapalli
Data Scientist | GenAI Enthusiast




