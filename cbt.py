import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Groq GPT-OSS 120B - African Culture & AI",
    page_icon="🌍",
    layout="wide"
)

# Sidebar with African Culture Gallery & Heritage Showcase
with st.sidebar:
    st.header("🌍 African Culture & Heritage")
    st.write("Exploring the vibrant colors, art, wildlife, and traditions of Africa.")
    
    # Curated public image URLs showcasing African culture, landscapes, and patterns
    african_images = [
        {
            "url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800&auto=format&fit=crop&q=60",
            "caption": "Majestic Savannah Landscapes & Wildlife"
        },
        {
            "url": "https://images.unsplash.com/photo-1516026666904-81262d4742a8?w=800&auto=format&fit=crop&q=60",
            "caption": "Vibrant Traditional Patterns & Textiles"
        },
        {
            "url": "https://images.unsplash.com/photo-1489493887464-892ce6e14454?w=800&auto=format&fit=crop&q=60",
            "caption": "Rich Architectural & Cultural Landmarks"
        }
    ]
    
    for img in african_images:
        st.image(img["url"], caption=img["caption"], use_container_width=True)

# Main Chat Interface
st.title("🤖 Groq GPT-OSS 120B Chatbot")
st.markdown("### Powered by Groq & Streamlit • Celebrating African Culture & Innovation")

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    api_key = os.getenv("x")
    if not api_key:
        st.error("API key not found in .env file under variable 'x'. Please check your environment configuration.")
        st.stop()
    return Groq(api_key=api_key)

client = get_groq_client()
MODEL = "openai/gpt-oss-120b"

# Initialize conversation history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant with a deep appreciation for diverse global cultures, heritage, and traditions across Africa."
        }
    ]

# Display prior chat messages (excluding the system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Handle user input via Streamlit's chat input widget
if user_input := st.chat_input("Type your message here..."):
    # Append user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=st.session_state.messages,
                    temperature=0.7,
                    max_tokens=2048
                )
                assistant_response = response.choices[0].message.content
                st.markdown(assistant_response)
                
                # Append assistant response to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_response
                })
                
            except Exception as e:
                st.error(f"Error: {e}")
