import sys, os

# Get the absolute path to the project root (one level up from /app)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



import streamlit as st
import tempfile
import fitz
from src.workflow.workflow_runner import run_resume_screening


# ------ set streamlit page config ---
st.set_page_config(
    page_title="CareerCompass AI",
    layout="centered"
)

# ------ Title an Description ----
st.title("CareerCompass AI")
st.markdown("""
### Your Smart Resume Advisor
Upload your resume and let AI analyze your experience, match you with roles, 
and suggest how to make your portfolio stand out.
""")

# --- Input Section -----
uploaded_file = st.file_uploader(label= "📄 Upload your Resume (PDF or TXT)",
                                 type=['pdf', 'txt'])
target_role = st.text_input("🎯 Enter your Target Role (e.g., Data Scientist, Product Manager)")


analyse_btn = st.button("Get AI Feedback")

# ------ Process Resume -----------
if analyse_btn:
    if not uploaded_file and target_role:
        st.warning("⚠️ Please upload your resume and enter a target role before proceeding.")
        st.stop()
    
    with st.spinner("🧠 Analyzing your resume... This might take a minute ⏳"):
        resume_text = ""
        if uploaded_file.type == "application/pdf":
            # Open from bytes, not filename
            pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            for page in pdf:
                resume_text += page.get_text() + "\n\n"
            pdf.close()
        else:
            resume_text = uploaded_file.read().decode("utf-8")

        # ------ Run Langgraph workflow -----
        results = run_resume_screening(cv = resume_text, role = target_role)
        

    st.success("✅ Analysis Complete!")

    # --- Display results ------
    st.subheader("📊 Resume Summary")
    st.write(f"**Experience Level:** {results.get('experience_level', 'N/A')}")
    st.write(f"**Match Score:** {results.get('match_score', 'N/A')} / 100")

    if results["top_roles"]:   
        with st.expander("Top Matching Roles"):
            st.write(results["top_roles"])

    if results["recommended_projects"]:   
        with st.expander("Recommended Projects"):
            st.write(results["recommended_projects"])
            
    if results["skills_to_improve"]:
        with st.expander("Skills to Improve"):
            st.write(results["skills_to_improve"])

    st.subheader("💬 AI Feedback Summary")
    st.markdown(results.get("final_feedback", "_No feedback generated._"))


# ---- Footer -----
st.markdown("---")
st.caption("🚀 Built with LangGraph + Streamlit | by [Akhila Devarapalli](https://github.com/akhidevGIT)")











