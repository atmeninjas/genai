# -*- coding: utf-8 -*-
!pip install langchain langchain-cohere langchain-community
!pip install gdown




import getpass
import os
if not os.environ.get("COHERE_API_KEY"):
  os.environ["COHERE_API_KEY"] = getpass.getpass("Enter API key for Cohere: ")
from langchain_cohere import ChatCohere
model = ChatCohere(model="command-r7b-12-2024")





from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("Tell me a quote on the {topic}")
chain = prompt | model
chain.invoke({"topic": "AI"}).content






import gdown
file_id = "18opmXTc4DKEPvtBKoAhNp5YUDwyJ8nA1"
file_path = "ai_agents_info.txt"
gdown.download(f"https://drive.google.com/uc?export=download&id={file_id}", file_path, quiet=False)
with open(file_path, "r", encoding="utf-8") as file:
  document_text = file.read()
print(document_text)






from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("Extract and list the types of AI agents as bullet points from the following text:{document_text}")
chain = prompt | model





print(chain.invoke({"document_text": document_text}).content)
