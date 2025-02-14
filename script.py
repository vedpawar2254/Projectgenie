# ######## cohere ##########



import streamlit as st
import cohere
import fitz  # PyMuPDF
import pdfplumber
import re



# try:
#     import fitz  
#     pymupdf_available = True
# except ImportError:
#     pymupdf_available = False
    
# try:
#     import pdfplumber
#     pdfplumber_available = True
# except ImportError:
#     pdfplumber_available = False


full_stack = """
100 Project Ideas for Full Stack Developers
Welcome to this list of project ideas for full-stack developers. Whether you're a beginner looking for practice or an experienced developer seeking new challenges, these ideas cover various domains and technologies.

Web Development Projects
Personal Portfolio Website
Blogging Platform
E-commerce Website
Social Media Platform
Content Management System (CMS)
Online Quiz Application
Forum or Community Platform
Real-time Chat Application
Weather Forecast App
News Aggregator
Recipe Sharing Website
Task Management App
URL Shortener
Online Code Editor
Event Management System
Crowdfunding Platform
Booking and Reservation System
Music Streaming Service
Polling and Survey App
E-learning Platform
Mobile App Projects
To-Do List App
Expense Tracker
Fitness and Workout App
Recipe and Meal Planning App
Language Learning App
Music Player
Note-Taking App
News Reader
Location-Based Reminder App
Social Networking App
Weather App
QR Code Scanner
Budgeting and Finance App
Meditation and Mindfulness App
Event Countdown App
Habit Tracker
Flashcard App
Ride-Sharing App
Document Scanner
Navigation App
Data Science and Analytics Projects
Data Visualization Dashboard
Stock Market Analysis Tool
Sentiment Analysis of Social Media Data
Predictive Analytics Tool
Customer Churn Prediction
Recommendation System
Fraud Detection System
Natural Language Processing (NLP) Tool
Sales Forecasting App
Data Annotation and Labeling Tool
IoT and Hardware Projects
Smart Home Automation System
Weather Station with Sensors
Home Security System
Remote-controlled Robot
Smart Mirror
IoT-based Plant Watering System
Fitness Tracker with IoT
GPS Tracking Device
Automated Pet Feeder
Smart Light Control System
Game Development Projects
2D Platformer Game
Puzzle Game
Chess or Checkers Game
Card Game (e.g., Solitaire)
Multiplayer Online Game
Racing Game
Tower Defense Game
Augmented Reality (AR) Game
Educational Game for Kids
Quiz or Trivia Game
Machine Learning and AI Projects
Image Recognition App
Chatbot
Predictive Text Generator
Speech Recognition System
Facial Recognition System
Sentiment Analysis Chatbot
Recommendation Engine
Object Detection System
Anomaly Detection Tool
AI-powered Virtual Assistant
Open Source and Community Projects
Open-source Full-Stack Project Template
Content Sharing Platform for Developers
Volunteer Management System for Nonprofits
Event Scheduling App for Local Communities
Collaboration and Project Management Tool
Code Review and Collaboration Platform
Platform for Collecting and Sharing Educational Resources
Charity and Donation Management System
Library Management System for Local Libraries
Open-source Healthcare Information System
Finance and Fintech Projects
Expense Tracking and Budgeting App
Cryptocurrency Portfolio Tracker
Stock Portfolio Management System
Peer-to-Peer Payment App
Loan and Mortgage Calculator
Invoice and Billing System
Investment Portfolio Analyzer
Personal Finance Dashboard
Automated Savings Planner
Cryptocurrency Exchange Platform
"""

frontend = """01.Gradient loader animation
02.Fliping cradit-card animation
03.Custom dropdown list
04.Login form in html and css
05.QR code generator
06.To-do list
07.happy birthday animation
08.realistic candle animation
09.Quiz app
10.Weather app
11.Form validation in Javascript
12.Tic-Tac-Toe Game
13.Portfolio website
14.Own code editor
15.Text To Speech converter"""


backend = """"Projects
1.Company-Portfolio
2.Blog-Website
3.E-book Website
4.E-commerce Website
5.Resturant Website
6.Hotel Website
7.Photography Portfolio Website
8.Fitness Website
9.Password Generator
10.QR code Generator
11.Weather App
12.Tic-Tac-Toe Game
13.Link Shorten Website
14.Drawing App
15.Alarm Clock
16.Meme Generator
17.Chatting App
18.Online From
19.Text-Translator
20.Playable Piano
21.Image Resizer
22.Dynamic Calender
23.File Downloader
24.Chess Game
25.Car-Racing
26.Connect-Game
27.snake-Lander Game
28.Word-Guessing Game
29.Analog Watch
30.Photo Editor
31.Music Player
32.Calculator
33.Rock-Paper-Scissors Game
34.Note App
35.Text-File Saver
36.Dictionay App
37.Snake Game
38.Stock Trading App
39.Stop watch
40.Text to Word Convertor
41.Todo List App
42.Twitter Clone
43.Typing Speed Test App
44.Admin Panel Dashboard
45.Whatsapp Clone
46.Video 2 Audio converter
47.Random Qoute Generator
48.Online Quiz Website
49.Dragon Game
50.Drag&Drop Image"""


st.set_page_config(layout="wide")  
st.title("🚀 Project Genie & Resume Analyzer")

def initialize_cohere():
    api_keys = [st.secrets["api_keys"].get("API_KEY_1"), st.secrets["api_keys"].get("API_KEY_2"), st.secrets["api_keys"].get("API_KEY_3")]
    for key in api_keys:
        if key:
            try:
                co = cohere.Client(key)
                return co
            except Exception:
                continue
    st.error("🚨 All API keys failed. APIs not working.")
    return None

co = initialize_cohere()


col1, col2 = st.columns([1, 1])

with col1:
  
    st.header("📄 Resume Analyzer")
    uploaded_file = st.file_uploader("Upload your PDF Resume", type="pdf")
    
    def extract_text_pymupdf(uploaded_file):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = "\n".join(page.get_text() for page in doc)
        return text
    
    def extract_text_pdfplumber(uploaded_file):
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        return text
    
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        method = st.radio("Choose Extraction Method", ["PyMuPDF", "pdfplumber"])
        
     
        # resume_text = extract_text_pymupdf(uploaded_file) if method == "PyMuPDF" else extract_text_pdfplumber(uploaded_file)
        
        resume_text = extract_text_pymupdf(uploaded_file) if method == "PyMuPDF" else extract_text_pdfplumber(uploaded_file)
        
        st.subheader("Extracted Resume Text")
        st.text_area("", resume_text, height=300)
        
        st.subheader("Anything you want to learn while building these projects?")
        user_learning_input = st.text_input("")
        
        if st.button("Generate Project Ideas"):
            st.session_state.resume_text = resume_text 
            st.session_state.user_learning_input = user_learning_input 
            st.session_state.button_clicked = True 

with col2:
    if "resume_text" in st.session_state and co is not None:
        st.header("🛠 Generated Project Ideas")
        st.write("🔍 **Processing for project recommendations...**")
        
        prompt = f"""You are an AI project advisor helping students build relevant and achievable technology solutions/projects. for exapmle frontend app if the student knows frontend,etc. and other software projects that help students get internships and placements
        Use {frontend},{backend},{full_stack} as per need if the user's resume has the required skills for those projects
            ### **Student Profile:**
            Give more importance to students current technical skills
            {resume_text}
            ### **Project Guidelines:**
            1. Use only the technologies mentioned in skills.
            2. Suggest 3 projects—one beginner, one intermediate, and one advanced.
            3. Projects should be achievable within 2-6 weeks.
            4. Align projects with career trends.
            5. Format output as follows:
            #### **Project {1,2,3}: [Project Title]**
            - **Level**: Beginner/Intermediate/Advanced  
            - **Description**: [Brief overview]  
            - **TechStack used**: [tech stack used and why]
            - **Scope and Features**: [give features and the scope of project]
            - **Step-by-step Roadmap**:  
            - Step 1
            - Step 2
            .
            .
            .
            - Step n
            - **Required Resources**: [Courses, GitHub repos, docs, or tutorials]  
            - **Expected Outcome**: [What the user will learn]  
            Only return structured project ideas. No extra explanations.
            """
                    
        try:
            response = co.generate(
                model="command-r-08-2024",
                prompt=prompt,
                max_tokens=700
            )
            st.subheader("Recommended Project Ideas:")
            st.write(response.generations[0].text)
        except Exception as e:
            st.error(f"🚨 Error generating project ideas: {str(e)}")
        
       
    st.markdown("---")
    st.subheader("💡 Tips for Effective Learning")
    st.write("- Break projects into smaller tasks and set milestones.")
    st.write("- Follow the recommended resources step by step.")
    st.write("- Document your learning journey through blogs or GitHub.")



# import streamlit as st
# import cohere


# api_key = st.secrets["api_keys"]["API_KEY"]

# # # Initialize Cohere client
# co = cohere.Client(api_key)


# # Streamlit interface
# st.title("Project Genie Chatbot")
# st.write("Enter your interests to get project ideas.")

# user_input = st.text_input("Enter your interests:")

# if user_input:
#     prompt = f"Suggest a unique project idea based on the following interests: {user_input}"
    
#     response = co.generate(
#         model="command-r-08-2024",
#         prompt=prompt,
#         max_tokens=5
#     )
    
#     st.write("Generated Project Idea:")
#     st.write(response.generations[0].text)
    
    
    
# import streamlit as st
# import fitz  # PyMuPDF
# import pdfplumber

# # Function to extract text using PyMuPDF
# def extract_text_pymupdf(uploaded_file):
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = "\n".join(page.get_text() for page in doc)
#     return text

# # Function to extract text using pdfplumber (alternative)
# def extract_text_pdfplumber(uploaded_file):
#     with pdfplumber.open(uploaded_file) as pdf:
#         text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
#     return text

# # Streamlit UI
# st.title("📄 Resume Analyzer")

# uploaded_file = st.file_uploader("Upload your PDF Resume", type="pdf")

# if uploaded_file is not None:
#     st.success("File uploaded successfully!")
    
#     # Choose extraction method
#     method = st.radio("Choose Extraction Method", ["PyMuPDF", "pdfplumber"])

#     # Extract text
#     if method == "PyMuPDF":
#         resume_text = extract_text_pymupdf(uploaded_file)
#     else:
#         resume_text = extract_text_pdfplumber(uploaded_file)

#     # Display extracted text
#     st.subheader("Extracted Resume Text")
#     st.text_area("", resume_text, height=300)

#     # Option to process further
#     if st.button("Analyze Resume"):
#         st.write("🔍 **Processing for project recommendations...**")
#         # You can now pass `resume_text` to your LLM for project suggestions!









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

