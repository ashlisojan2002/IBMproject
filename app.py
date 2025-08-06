
import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Page styling
st.set_page_config(page_title="CivicAssist AI", layout="centered")
st.markdown("""
    <style>
        body { background-color: #ffffff; color: #0b1c2c; }
        .stApp { background-color: #ffffff; font-family: 'Segoe UI', sans-serif; }
        h1, h2, h3 { color: #2d7792; }
        .stButton>button {
            background-color: #2d7792; color: white; border-radius: 8px;
            padding: 0.5em 1em; border: none;
        }
        .stButton>button:hover {
            background-color: #0b1c2c; color: white;
        }
        .stTextInput>div>input, .stTextArea>div>textarea, .stSelectbox>div>div {
            background-color: #f5f9fa; color: #0b1c2c;
            border: 1px solid #2d7792; border-radius: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# State list
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Frontend
st.title("🌐 CivicAssist AI")
st.subheader("A Smart Assistant for Reporting Civic Issues in India")

state = st.selectbox("📍 Select Your State", indian_states)
location = st.text_input("📌 Your Location (Area/City)")
issue = st.text_area("🗣️ Describe Your Civic Issue")

# Submit
if st.button("Submit"):
    if not location or not issue:
        st.warning("⚠️ Please enter both location and issue.")
    else:
        with st.spinner("🤖 Thinking..."):
            prompt = f"""
You are a civic assistant AI for India. The user is from {state}, near "{location}".

Understand their civic complaint and respond in this format:

Issue Type:
Responsible Department:
Contact Information (realistic for {state}):
Nearest Office (if known):
Google Maps Link:
Suggestion:

Complaint: {issue}
"""
            response = model.generate_content(prompt)
            st.success("✅ AI Response:")
            st.markdown(response.text)
