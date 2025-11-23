# Context7 PDF Summarizer Agent - Setup Instructions

### step 1 Critical Technical Constraints
**You must adhere to the following strict configuration rules:**

1.  **Zero-Bloat Protocol (CRITICAL):**
    * **Do NOT write extra code.** Do not add bells, whistles, advanced error handling (unless specified), or unnecessary comments.
    * **Focus strictly on the integration:** Connect the `agent` to `streamlit`. Nothing else.
    * **No "Hallucinated" Features:** If it's not in the SDK docs, do not invent it.
2.  **API Configuration:**
    * Use the **OpenAI Agents SDK** Python Library configured for Gemini.
    * **Base URL:** `https://generativelanguage.googleapis.com/v1beta/openai/`
    * **API Key:** Load `GEMINI_API_KEY` from environment variables.
    * **Model:** Use `OpenaiChatCompletionModel` adapted for Gemini.
3.  **SDK Specificity:** You are using `openai-agents` SDK. This is **NOT** the standard `openai` library. You must use the specific syntax provided by the `openai-agents` SDK.
4.  **Error Recovery Protocol:**
    * If you encounter a `SyntaxError`, `ImportError`, or `AttributeError` related to `openai-agents` during development, **STOP**.
    * Do not guess the fix. **You MUST call the `get-library-docs` tool again** to re-read the documentation and verify the correct syntax before rewriting the code.
5.  **Dependency Management:** Use `uv` for package management.

### Step 2: Environment & Dependencies

  * Create a `.env` template.
  * List necessary packages in `pyproject.toml` (ensure `openai-agents` is included).
  * **Smart Install:** Check `pyproject.toml` and the current environment. **If the dependencies are already installed, DO NOT run the installation commands again.**

## 3. Install Required Dependencies
- Install necessary packages:  
  `pip install streamlit pypdf openai-agents`

## 4. Create Main Application Files
- Generate these files in your directory:  
  - `agent.py` (contains extraction, summary logic)
  - `ui.py` (contains Streamlit UI)
  - `requirements.txt` (generated automatically)
  - `README.md`

## 5. Write PDF Extraction Function (agent.py)
- Code for extracting all text from the uploaded PDF using PyPDF:
- User uploads a PDF.
- Text is extracted using PyPDF.
- Agent generates a clean, meaningful summary.
- Summary can appear in any UI style students choose (card, block,container, etc.).

## 6 Quiz Generator
- After summarization, the user can click Create Quiz.
- The agent reads the original PDF (not the summary).
- It generates:
- MCQs
- Or mixed-style quizzes

