import streamlit as st
from retriever import retrieve
from llm import generate_response

st.title("🧠 SHL Assessment Recommendation Engine")

query = st.text_input("Enter your assessment needs:")

if query:
    with st.spinner("Finding the best assessments..."):
        context = retrieve(query)
        answer = generate_response(query, context)

    st.markdown("### 🔍 Recommended Assessments:")
    st.write(answer)