# import os
# from dotenv import load_dotenv
# from pypdf import PdfReader
# from agents import Agent, OpenAIChatCompletionsModel, Runner
# from openai import AsyncOpenAI
# import streamlit as st

# # --- Custom CSS for Dark Background + Cyan Text ---
# st.markdown("""
#     <style>
#         html, body, .main { background-color: #151a21; }
#         h1, h2, h3, h4 { color: #33FFE0; font-family: 'Segoe UI', sans-serif; }
#         .stApp { background-color: #151a21; }
#         .stButton>button {
#             background-color: #1356d3;
#             color: #FAF7F2;
#             border-radius: 8px;
#         }
#         .stFileUploader label { color: #33FFE0; font-weight: bold; font-size: 1.1em;}
#         .stInfo, .stAlert, .stMarkdown {
#             background-color: #212733 !important;
#             color: #33FFE0 !important;
#             border-radius: 8px;
#             font-size: 1.08em;
#         }
#         .stSuccess {
#             background-color: #22DFFF !important;
#             color: #151a21 !important;
#         }
#         .stSubheader { color: #33FFE0; }
#     </style>
# """, unsafe_allow_html=True)

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# def extract_text_from_pdf(pdf_file):
#     try:
#         reader = PdfReader(pdf_file)
#         text = ""
#         for page in reader.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text
#         return text
#     except Exception as e:
#         return f"Error reading PDF: {e}"

# def summarize_text(text_to_summarize):
#     if not api_key:
#         return "GEMINI_API_KEY not found. Please set it in your .env file."
#     client = AsyncOpenAI(
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#         api_key=api_key
#     )
#     model = OpenAIChatCompletionsModel(
#         model="gemini-2.5-flash",  # Try "gemini-2.0-flash" if this fails
#         openai_client=client
#     )
#     agent = Agent(
#         name="PDFSummarizer",
#         instructions="You are a helpful assistant that summarizes text.",
#         model=model
#     )
#     prompt = f"Please summarize the following text:\n\n{text_to_summarize}"
#     result = Runner.run_sync(agent, prompt)
#     return getattr(result, "final_output", str(result))

# def generate_quiz(text_for_quiz):
#     if not api_key:
#         return "GEMINI_API_KEY not found. Please set it in your .env file."
#     client = AsyncOpenAI(
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#         api_key=api_key
#     )
#     model = OpenAIChatCompletionsModel(
#         model="gemini-2.5-flash",
#         openai_client=client
#     )
#     agent = Agent(
#         name="QuizGenerator",
#         instructions="You are an expert quiz creator. Create a multiple-choice quiz from the provided text. Ensure questions are clear and answers are concise.",
#         model=model
#     )
#     prompt = f"Generate a 5-question multiple-choice quiz from the following text:\n\n{text_for_quiz}"
#     result = Runner.run_sync(agent, prompt)
#     return getattr(result, "final_output", str(result))
# def main():
#     st.title("📄 PDF Text Processor")
#     st.markdown(
#         "<h4 style='color: #33FFE0'>Summarize and generate quizzes from your PDFs with Gemini AI</h4>",
#         unsafe_allow_html=True,
#     )
#     st.write(" ")

#     # Initialize all necessary state variables
#     for key in ['extracted_text', 'summary', 'quiz']:
#         if key not in st.session_state:
#             st.session_state[key] = None

#     uploaded_file = st.file_uploader("Upload PDF Document", type="pdf")
#     if uploaded_file:
#         if st.button("Extract PDF Text"):
#             with st.spinner("Extracting text..."):
#                 st.session_state.extracted_text = extract_text_from_pdf(uploaded_file)
#                 st.success("Text extracted!")
#                 # Clear previous outputs
#                 st.session_state.summary = None
#                 st.session_state.quiz = None

#     # Show buttons (regardless of summary state!), as soon as we have extracted text
#     if st.session_state.extracted_text:
#         st.markdown("<p style='color:#33FFE0;'>PDF Text Loaded</p>", unsafe_allow_html=True)

#         # Summarize button
#         if st.button("Summarize Text"):
#             with st.spinner("Generating summary..."):
#                 st.session_state.summary = summarize_text(st.session_state.extracted_text)
#         if st.session_state.summary:
#             st.subheader("Summary")
#             st.info(st.session_state.summary)
#             st.write("---")
        
#         # Quiz button
#         if st.button("Create Quiz from PDF"):
#             with st.spinner("Generating quiz..."):
#                 st.session_state.quiz = generate_quiz(st.session_state.extracted_text)
#         if st.session_state.quiz:
#             st.subheader("Quiz")
#             st.markdown(f"<div style='color:#33FFE0'>{st.session_state.quiz}</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(
#             "<p style='color: #33FFE0'>Please upload and extract a PDF to get started.</p>",
#             unsafe_allow_html=True,
#         )


# # def main():
# #     st.title("📄 PDF Text Processor")
# #     st.markdown(
# #         "<h4 style='color: #33FFE0'>Summarize and generate quizzes from your PDFs with Gemini AI</h4>",
# #         unsafe_allow_html=True,
# #     )
# #     st.write(" ")

# #     if 'extracted_text' not in st.session_state:
# #         st.session_state.extracted_text = None
# #     if 'summary' not in st.session_state:
# #         st.session_state.summary = None
# #     if 'quiz' not in st.session_state:
# #         st.session_state.quiz = None

# #     uploaded_file = st.file_uploader("Upload PDF Document", type="pdf")
# #     if uploaded_file:
# #         with st.spinner("Extracting text..."):
# #             st.session_state.extracted_text = extract_text_from_pdf(uploaded_file)
# #             st.success("Text extracted!")

# #     if st.session_state.extracted_text:
# #         # Show 'Summarize' button always after extraction
# #         if st.button("Summarize Text"):
# #             with st.spinner("Generating summary..."):
# #                 st.session_state.summary = summarize_text(st.session_state.extracted_text)

# #         # Show summary (if exists)
# #         if st.session_state.summary:
# #             st.subheader("Summary")
# #             st.info(st.session_state.summary)
# #             st.write("---")
        
# #         # Quiz button is now always visible after extraction
# #         if st.button("Create Quiz from PDF"):
# #             with st.spinner("Generating quiz..."):
# #                 st.session_state.quiz = generate_quiz(st.session_state.extracted_text)
        
# #         # Show quiz (if exists)
# #         if st.session_state.quiz:
# #             st.subheader("Quiz")
# #             st.markdown(f"<div style='color:#33FFE0'>{st.session_state.quiz}</div>", unsafe_allow_html=True)
# #     else:
# #         st.markdown(
# #             "<p style='color: #33FFE0'>Please upload a PDF to get started.</p>",
# #             unsafe_allow_html=True,
# #         )

# if __name__ == "__main__":
#     main()
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI

# Only load env once per process
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a PDF file given its path."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def summarize_text(text_to_summarize):
    """Summarizes the given text using the Gemini model via Agents SDK."""
    
    client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=API_KEY
    )
    model = OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",  # If fails, use "gemini-2.0-flash"
        openai_client=client
    )
    agent = Agent(
        name="PDFSummarizer",
        instructions="You are a helpful assistant that summarizes text.",
        model=model
    )
    prompt = f"Please summarize the following text:\n\n{text_to_summarize}"
    result = Runner.run_sync(agent, prompt)
    return getattr(result, "final_output", str(result))

def generate_quiz(text_for_quiz):
    """Generates a multiple-choice quiz from the given text using Gemini."""
    client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=API_KEY
    )
    model = OpenAIChatCompletionsModel(
        model="gemini-2.5-flash",  # If fails, use "gemini-2.0-flash"
        openai_client=client
    )
    agent = Agent(
        name="QuizGenerator",
        instructions="You are an expert quiz creator. Create a 5-question multiple-choice quiz from the text. Each question should have four options and indicate the correct answer.",
        model=model
    )
    prompt = f"Generate a 5-question multiple-choice quiz from the following text:\n\n{text_for_quiz}"
    result = Runner.run_sync(agent, prompt)
    return getattr(result, "final_output", str(result))
