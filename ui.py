# import streamlit as st
# import os
# from agent import extract_text_from_pdf, summarize_text

# # --- Streamlit UI ---
# st.set_page_config(page_title="PDF Summarizer", page_icon="📄", layout="centered")

# st.title("📄 PDF Summarizer Agent")
# st.write("Upload a PDF file and get a summary of its content.")

# # Check for API key and display a warning if it's not set
# if not os.getenv("GEMINI_API_KEY") and 'your_gemini_api_key_here' in open('.env').read():
#     st.warning("⚠️ Please set your `GEMINI_API_KEY` in the `.env` file to use the summarizer.", icon="❗")


# uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# if uploaded_file is not None:
#     # Save the uploaded file temporarily
#     temp_dir = "temp"
#     if not os.path.exists(temp_dir):
#         os.makedirs(temp_dir)
#     temp_path = os.path.join(temp_dir, uploaded_file.name)
#     with open(temp_path, "wb") as f:
#         f.write(uploaded_file.getvalue())

#     st.write("---")
#     st.write(f"**File:** `{uploaded_file.name}`")
    
#     with st.spinner("Extracting text from PDF..."):
#         extracted_text = extract_text_from_pdf(temp_path)

#     if "Error reading PDF" in extracted_text:
#         st.error(extracted_text)
#     elif not extracted_text.strip():
#         st.warning("Could not extract any text from the PDF. The file might be empty or contain only images.")
#     else:
#         st.success("Text extracted successfully!")
        
#         if st.button("Summarize Text", use_container_width=True):
#             with st.spinner("Generating summary... This may take a moment."):
#                 summary = summarize_text(extracted_text)
#                 st.subheader("Summary")
#                 st.markdown(summary)

#     # Clean up the temporary file
#     os.remove(temp_path)

import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from agent import extract_text_from_pdf, summarize_text, generate_quiz

# Environment config
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="PDF Summarizer", page_icon="📄", layout="centered")
st.title("📄 PDF Summarizer Agent")
st.write("Upload a PDF file and get a summary (and quiz) of its content.")

if not api_key:
    st.warning("⚠️ Please set your `GEMINI_API_KEY` in the `.env` file to use the summarizer.", icon="❗")

# SESSION STATE INIT
if "extracted_text" not in st.session_state: st.session_state.extracted_text = ""
if "summary" not in st.session_state: st.session_state.summary = ""
if "quiz" not in st.session_state: st.session_state.quiz = ""

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.write("---")
    st.write(f"**File:** `{uploaded_file.name}`")

    if st.session_state.extracted_text == "":
        with st.spinner("Extracting text from PDF..."):
            st.session_state.extracted_text = extract_text_from_pdf(temp_path)
        os.remove(temp_path)

    if "Error reading PDF" in st.session_state.extracted_text:
        st.error(st.session_state.extracted_text)
    elif not st.session_state.extracted_text.strip():
        st.warning("Could not extract any text from the PDF. The file might be empty or contain only images.")
    else:
        st.success("Text extracted successfully!")
        # Summary Button + Output
        if st.button("Summarize Text"):
            with st.spinner("Generating summary... This may take a moment."):
                st.session_state.summary = summarize_text(st.session_state.extracted_text)

        if st.session_state.summary:
            st.subheader("Summary")
            st.markdown(st.session_state.summary)
        
        # Quiz Button + Output
        if st.button("Create Quiz from PDF"):
            with st.spinner("Generating quiz..."):
                st.session_state.quiz = generate_quiz(st.session_state.extracted_text)
        if st.session_state.quiz:
            st.subheader("Quiz")
            st.markdown(st.session_state.quiz)

else:
    st.info("Please upload a PDF to get started.")
