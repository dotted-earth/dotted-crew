import os
from langchain_groq import ChatGroq
from decouple import config


os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")


groqLLM = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"), model="llama3-8b-8192", temperature=0
)
