import streamlit as st
import google.generativeai as genai
import os

# --- CONFIGURATION ---
# Replace with your actual API key or set it in your environment variables
# It is best practice to use os.getenv("GEMINI_API_KEY")
API_KEY = "YOUR_GEMINI_API_KEY_HERE" 

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Define the System Instruction (The Brains)
system_instruction = """
You are 'HealthBuddy', an AI Health Consultation Assistant. 
Your goal is to provide helpful, accurate general health information, wellness tips, and symptom explanations.

RULES:
1. Tone: Empathetic, professional, and calm.
2. Structure: Use bullet points for lists (e.g., symptoms, remedies).
3. SAFETY CRITICAL: You are NOT a doctor. You cannot prescribe medication or diagnose specific diseases. 
   ALWAYS end your response with a disclaimer advising the user to visit a certified medical professional.
4. If the user mentions an emergency (chest pain, trouble breathing, severe bleeding), tell them to call emergency services immediately.
"""

# Initialize the Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Flash is fast and good for chat
    system_instruction=system_instruction
)

# --- STREAMLIT UI ---
st.set_page_config(page_title="AI Health Consultant", page_icon="🩺")

st.title("🩺 AI Health Consultation Assistant")
st.markdown("ask me about symptoms, wellness, or nutrition. \n\n*Note: I am an AI support tool, not a doctor.*")

# Initialize Chat History in Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    # Start the chat session with the model
    st.session_state.chat_session = model.start_chat(history=[])

# Display Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Area
user_prompt = st.chat_input("Describe your symptoms or ask a health question...")

if user_prompt:
    # 1. Display User Message
    st.chat_message("user").markdown(user_prompt)
    
    # 2. Add to history
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # 3. Get Response from Gemini
    try:
        response = st.session_state.chat_session.send_message(user_prompt)
        ai_response = response.text
        
        # 4. Display AI Message
        with st.chat_message("assistant"):
            st.markdown(ai_response)
            
        # 5. Add AI response to history
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
