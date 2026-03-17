import streamlit as st
import ollama

st.title("🐞 AI Bug Analyzer Pro")

with st.form("bug_form"):
    bug_input = st.text_area("Paste your error / bug here:")
    submit = st.form_submit_button("Analyze Bug")

if submit:
    if bug_input.strip() == "":
        st.warning("Please enter a bug")
    else:
        with st.spinner("Analyzing... 🤖"):
            try:
                prompt = f"""
You are a senior software engineer and QA expert.

Analyze the following bug and respond in STRICT format:

Bug Type: (Frontend / Backend / API / Database / DevOps / User Issue)
Priority: (High / Medium / Low)
Root Cause:
Fix:
Prevention:

Bug:
{bug_input}
"""

                response = ollama.chat(
                    model="llama3",
                    messages=[{"role": "user", "content": prompt}]
                )

                result = response['message']['content']

                st.success("Analysis Complete ✅")

                # Display nicely
                st.markdown("### 📊 Analysis Result")
                st.write(result)
                

            except Exception as e:
                st.error(f"Error: {e}")