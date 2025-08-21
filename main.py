import streamlit as st
import fitz
import subprocess
import json

def extract(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def call_ollama(prompt, model="llama3"):
    reesult = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        capture_output=True,
    )
    return reesult.stdout.decode("utf-8")

st.set_page_config(page_title="Quizzie", page_icon="📋", layout="centered")
st.title("Quizzie 📋")

uploaded_file = st.file_uploader("Upload your pdf here", type=["pdf"])

if uploaded_file:
    st.success("PDF sucessfully uploaded!")

    if st.button("Pass to AI"):
        with st.spinner("Extracting text...."):
            pdf_text = extract(uploaded_file)

        with st.spinner("Summarizing..."):
            sum_prompt = f"Summarize the following text into clear well defined points to be helped in understanding and memorizing: \n\n {pdf_text[:4000]}"
            summary = call_ollama(sum_prompt)

        st.subheader("Summary!")
        st.write(summary)

        with st.spinner("Generating Quiz...."):
            quiz_prompt = f"Create a 10-question quiz with answers (MCQs preffered) from this text: \n\n {pdf_text[:4000]}"
            quiz = call_ollama(quiz_prompt)

        st.subheader("10-Question Quiz")
        st.write(quiz)