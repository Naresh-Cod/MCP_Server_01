import streamlit as st
import asyncio
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# LangChain LLM (ChatGroq)
llm = ChatGroq(model="qwen-qwq-32b")
client = MCPClient.from_config_file("browse_mcp.json")
agent = MCPAgent(llm=llm, client=client, memory_enabled=True)

# Streamlit UI
st.set_page_config(page_title="🧠 MCP Chat", layout="wide")
st.title("🧠 AI Chat with MCP Agent")
st.markdown("Ask me anything!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar controls
with st.sidebar:
    st.subheader("🛠️ Controls")
    if st.button("Clear Conversation"):
        agent.clear_conversation_history()
        st.session_state.chat_history = []
        st.success("Conversation cleared.")

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    
    with st.spinner("Thinking..."):
        response = asyncio.run(agent.run(user_input))

    st.session_state.chat_history.append(("assistant", response))

# Display chat history
for role, message in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.write(message)
    else:
        with st.chat_message("assistant"):
            st.write(message)
