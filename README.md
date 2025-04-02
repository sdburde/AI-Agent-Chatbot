
```markdown
# AI Agent Chatbot

A sophisticated chatbot framework with Groq/OpenAI integration, featuring:
- Streamlit frontend with conversation history
- FastAPI backend for AI processing
- Support for multiple LLM providers
- Web search capabilities via Tavily

```


![Chatbot Demo](https://github.com/sdburde/AI-Agent-Chatbot/blob/main/demo/AI_Agent_Chatbot_GIF_1.gif)


```
## 🚀 Features

- **Multi-Provider Support**: Switch between Groq and OpenAI models
- **Conversation Memory**: Full chat history with user/agent differentiation
- **Web Search Integration**: Optional real-time web search for responses
- **Modern Stack**:
  - Streamlit for interactive frontend
  - FastAPI for robust backend
  - LangChain/LangGraph for AI orchestration


## 📦 Project Structure

AI-Agent-Chatbot/
├── ai_agent_chatbot/       # Conda environment
├── __pycache__/
├── .env                    # Environment variables
├── .gitignore
├── ai_agent.py             # Core AI agent logic
├── fast_api_backend.py     # FastAPI server
├── requirements.txt        # Python dependencies
└── streamlit_frontend.py   # Chat interface
```

## 🛠️ Setup

### Prerequisites
- Python 3.10+
- Conda (recommended)
- API keys for:
  - Groq (required)
  - OpenAI (optional)
  - Tavily (optional for web search)

### Installation
1. Create Conda environment:
   ```bash
   conda create -p ./ai_agent_chatbot python=3.12 -y
   conda activate ./ai_agent_chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```ini
   GROQ_API_KEY=your_key_here
   TAVILY_API_KEY=your_key_here
   OPENAI_API_KEY=your_key_here  # Optional
   ```

## 🖥️ Usage

### Start Backend (FastAPI)
uvicorn fast_api_backend:app --reload --port 9999
```bash
python fast_api_backend.py
```

### Start Frontend (Streamlit)
```bash
streamlit run streamlit_frontend.py
```

Access the chat interface at `http://localhost:8501`

## 🌟 Features in Action

1. **Model Selection**:
   - Choose between Groq (Llama3-70B, Mixtral) or OpenAI (GPT-4) models
   - Set custom system prompts

2. **Web Search**:
   - Toggle web search for real-time information

3. **Conversation Flow**:
   - Full chat history preservation
   - Clear message differentiation (user vs agent)

## 🤖 Technical Stack

| Component       | Technology |
|----------------|------------|
| Frontend       | Streamlit  |
| Backend        | FastAPI    |
| AI Orchestration | LangChain, LangGraph |
| LLM Providers  | Groq, OpenAI |
| Search         | Tavily API |

