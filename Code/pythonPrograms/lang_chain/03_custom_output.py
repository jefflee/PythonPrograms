from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


class MyOutputParser(StrOutputParser):
    def parse(self, text):
        return text.replace('Assistant: ', '')


output_parser = MyOutputParser()

llm = Ollama(model='llama3:8b')
prompt = ChatPromptTemplate.from_messages([
    ("user", "{input}"),
])

chain = prompt | llm | output_parser
print(chain.invoke({"input": "Hi, how are you today?"}))
