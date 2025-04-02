from dotenv import load_dotenv
import streamlit as st
import requests
from typing import List, Dict, Literal
import json

load_dotenv()

# Define message type
MessageType = Literal["user", "agent"]

class Message:
    def __init__(self, content: str, type: MessageType):
        self.content = content
        self.type = type

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages: List[Message] = []

# UI Configuration
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    system_prompt = st.text_area(
        "System Prompt",
        height=100,
        placeholder="Define your AI Agent's behavior..."
    )
    
    provider = st.radio(
        "Select Provider:",
        ("Groq", "OpenAI"),
        horizontal=True
    )
    
    model_options = {
        "Groq": ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "qwen-2.5-32b"],
        "OpenAI": ["gpt-4o-mini"]
    }
    selected_model = st.selectbox(
        f"Select {provider} Model",
        model_options[provider]
    )
    
    allow_web_search = st.checkbox("Enable Web Search")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# Chat input
if user_query := st.chat_input("Ask Anything!"):
    # Add user message to history
    st.session_state.messages.append(
        Message(content=user_query, type="user")
    )
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)

    # Prepare API request
    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt or "You are a helpful AI assistant",
        "messages": [msg.content for msg in st.session_state.messages],
        "allow_search": allow_web_search
    }

    # Show loading spinner while waiting for response
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://127.0.0.1:5090/chat",
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            response_data = response.json()
            
            if isinstance(response_data, dict) and "error" in response_data:
                st.error(response_data["error"])
            # else isinstance(response_data, str):
            #     st.error(response_data) #display the string directly as an error
            else:
                # Add agent response to history
                st.session_state.messages.append(
                    Message(content=response_data, type="agent")
                )
                
                # Display agent response
                with st.chat_message("agent"):
                    st.markdown(response_data)
                    
        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {str(e)}")