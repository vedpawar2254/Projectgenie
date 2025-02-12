######### cohere ##########

import streamlit as st
import cohere


api_key = st.secrets["api_keys"]["API_KEY"]

# # Initialize Cohere client
co = cohere.Client(api_key)


# Streamlit interface
st.title("Project Genie Chatbot")
st.write("Enter your interests to get project ideas.")

user_input = st.text_input("Enter your interests:")

if user_input:
    prompt = f"Suggest a unique project idea based on the following interests: {user_input}"
    
    response = co.generate(
        model="command-r-08-2024",
        prompt=prompt,
        max_tokens=500
    )
    
    st.write("Generated Project Idea:")
    st.write(response.generations[0].text)
    
    


# import streamlit as st
# from llama_cpp import Llama

# # Initialize Llama model
# llama_model = Llama(model_path="/Users/vedpawar/llama_models/mistral-7b-instruct")  # Replace with your model path

# # Define Streamlit app interface
# st.title("Llama 3.2 Chatbot")
# st.write("Enter a prompt, and Llama 3.2 will generate a response:")

# # Take user input
# user_input = st.text_input("Enter your prompt:")

# # Generate a response from Llama 3.2
# if user_input:
#     response = llama_model(user_input)  # Adjust based on the function used to query the model
#     st.write("Llama's Response:")
#     st.write(response)



# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# model_name = "gpt2"
# model = GPT2LMHeadModel.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# input_text = "Once upon a time"
# inputs = tokenizer.encode(input_text, return_tensors="pt")
# outputs = model.generate(inputs, max_length=100, num_return_sequences=1)

# print(tokenizer.decode(outputs[0], skip_special_tokens=True))