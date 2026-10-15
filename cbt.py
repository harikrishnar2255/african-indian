import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Get API key from variable "x"
api_key = os.getenv("x")

if not api_key:
    raise ValueError("API key not found in .env file")

# Create Groq client
client = Groq(api_key=api_key)

# GPT-OSS 120B model
MODEL = "openai/gpt-oss-120b"

# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("🤖 Groq GPT-OSS 120B Chatbot")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=2048
        )

        assistant_response = response.choices[0].message.content

        print("\nBot:", assistant_response, "\n")

        messages.append({
            "role": "assistant",
            "content": assistant_response
        })

    except Exception as e:
        print("Error:", e)