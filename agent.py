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
