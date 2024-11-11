import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
#from langchain.output_parsers import PydanticOutputParser


import os
from dotenv import load_dotenv


load_dotenv()

##Langsmith tracking

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="QandA Chatbot with OPENAI"


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}") 
    ]
)
def generate_response(question,api_key,engine,temperature,max_tokens):
    
    openai.api_key=api_key

    llm=ChatOpenAI(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer

##title of the app

st.title("Utkarsh's QandA Chatbot with OpenAI")


##SIDEBAR FOR SETTINGS
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Open AI API Key:" , type="password")

## Drop down to select various OpenAI models

llm=st.sidebar.selectbox("Select an OpenAI Model",["gpt-4o", "gpt-4-turbo", "gpt-4"])

##Adjust response parameter
temperature=st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens=st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


##Main interface for user Input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")
if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query!!")
