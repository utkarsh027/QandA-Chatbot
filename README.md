# QandA-Chatbot
This project is an end-to-end Question and Answer (Q&A) chatbot application that leverages OpenAI's API to respond to user queries. Built with Python, the chatbot uses Streamlit to provide an interactive web interface where users can ask questions and receive answers powered by OpenAI's language models.

# Features
Interactive chat interface using Streamlit
Easy-to-use virtual environment setup
Seamless integration with OpenAI for generating responses

# Prerequisites
Python 3.10 or higher
OpenAI API Key (Sign up at OpenAI to get your API key)

#Option B: Open-Source Model (Using app.py with Ollama Mistral)

#Install Ollama:
Install Ollama on your local machine by following the instructions at Ollama's website.

#Download the Mistral Model:
Run the following command in your terminal to download the model:
ollama run mistral
#Run the Chatbot: 
Start the chatbot using Streamlit:
streamlit run app.py
#Troubleshooting
If you encounter issues, make sure:

->Your virtual environment is activated.
->Dependencies are correctly installed.
->OpenAI API key is correctly set in the .env file (if using main.py).
->The Mistral model is correctly downloaded (if using app.py).






