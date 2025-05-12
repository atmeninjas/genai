from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel
class InstitutionDetails(BaseModel):
  """
  Pydantic model to structure the output data for institution
  details.
  """
  founder: str
  founded: str
  branches: int
  employees: int
  summary: str





prompt_template = """
Given the name of an institution, extract the following details from
Wikipedia:
1. Founder of the institution
2. When it was founded
3. Current branches of the institution
4. How many employees work in it
5. A 4-line brief summary of the institution
Institution: {institution_name}
"""
import getpass

!pip install langchain-cohere
import os
if not os.environ.get("COHERE_API_KEY"):
  os.environ["COHERE_API_KEY"] = getpass.getpass("Enter API key forCohere: ")
from langchain_cohere import ChatCohere
model = ChatCohere(model="command-r7b-12-2024")





prompt = PromptTemplate(input_variables=["institution_name"],template=prompt_template)
chain = LLMChain(llm=model, prompt=prompt)
def fetch_institution_details(institution_name: str):
  """
  Fetches institution details using the Langchain chain and GPT-3
  model.
  Args:
  institution_name (str): The name of the institution to fetch

  details for.
  Returns:
  str: The result from the LLMChain run, containing institution

  details.
  """
  result = chain.run(institution_name=institution_name)
  return result

institution_name = input("Enter the institution name: ")
institution_details = fetch_institution_details(institution_name)
print(institution_details)
