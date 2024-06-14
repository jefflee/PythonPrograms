# pip install langchain_community
# Run Ollma locally first.
from langchain_community.llms import Ollama


llm = Ollama(model='llama3:8b')
print(llm.invoke('Hi, how are you today?'))
# I'm just a language model, I don't have emotions or feelings like humans do. 
# However, I'm functioning properly and ready to assist with any questions or tasks you may have! 
# How can I help you today?