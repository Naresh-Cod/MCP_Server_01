from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq


class MCPClient:
    """Dummy client for session management (placeholder for real backend client)."""
    def __init__(self):
        self.sessions = True

    @staticmethod
    def from_config_file(config_file):
        print(f"[DEBUG] Loaded config from: {config_file}")
        return MCPClient()

    async def close_all_sessions(self):
        print("[DEBUG] Closing all sessions")
        self.sessions = False


class MCPAgent:
    """MCP Agent with memory support using LangChain."""
    def __init__(self, llm, client, max_steps=15, memory_enabled=True):
        self.llm = llm
        self.client = client
        self.max_steps = max_steps
        self.memory_enabled = memory_enabled

        self.memory = ConversationBufferMemory()
        self.chain = ConversationChain(llm=self.llm, memory=self.memory)

    async def run(self, user_input):
        print(f"[DEBUG] Asking LLM: {user_input}")
        return self.chain.run(user_input)

    def clear_conversation_history(self):
        print("[DEBUG] Clearing memory buffer")
        self.memory.clear()
