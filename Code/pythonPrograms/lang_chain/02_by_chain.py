# pip install langchain_community
# Run Ollma locally first.

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model='llama3:8b')

prompt = ChatPromptTemplate.from_messages([
    ("user", "{input}"),
])

chain = prompt | llm

print(chain.invoke({"input": "Hi, how are you today?"}))
# AI: I'm doing well, thank you for asking! I'm a large language model,
# so I don't have emotions or feelings like humans do,
# but I'm always happy to chat and assist with any questions or topics you'd like to discuss.
# How about you? What's on your mind today?
