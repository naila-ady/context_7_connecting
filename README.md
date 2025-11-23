# PDF Summarizer Agent

This project implements a PDF summarizer agent using Streamlit and OpenAI Agents SDK.

## Setup

1.  **Initialize project**
     ```
      uv init
     ```
  
2.  **Create a virtual environment (optional but recommended):**
    ```
     uv venv
    .venv/Scripts/activate.
    uv add openai-agents python dotenv
    ```
6.  **Set up your API Key:**
    Create a `.env` file in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY=your_gemini_api_key_here
    
    ```
7. **Copy your gemini api key:**
   ```
    go to .gemini folder and inside settings.json write the following with your own api key
    "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {
        "CONTEXT7_API_KEY":""<YOUR_CONTEXT7_API_KEY_HERE>""
      }
       ```

## Running the Application

To run the Streamlit application:

```bash
streamlit run ui.py
```










