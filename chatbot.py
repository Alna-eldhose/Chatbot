"""
Project 1: Command-line chatbot
--------------------------------
A simple chatbot that runs in your terminal, talks to Google's Gemini LLM,
and remembers the conversation.

Run it with:  python chatbot.py
Type 'quit' to exit, 'reset' to start a new conversation.
"""

import os

from dotenv import load_dotenv   # reads secrets from the .env file
from google import genai          # Google's official Gemini SDK
from google.genai import types

# 1. Load settings from .env (so your API key is never written in the code)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise SystemExit("No API key found. Create a .env file with GEMINI_API_KEY=your_key")

# 2. The "system prompt" tells the LLM how to behave in every answer.
#    Try changing this and see how the bot's personality changes!
SYSTEM_PROMPT = (
    "You are a friendly, patient tutor helping a beginner learn Python and AI. "
    "Keep answers short and clear, and use simple examples."
)

# 3. Create the client (the connection to the API)
client = genai.Client(api_key=API_KEY)


def new_chat():
    """Start a fresh conversation. The chat object keeps the history for us,
    which is how the bot 'remembers' what you said earlier."""
    return client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.7,  # 0 = predictable, higher = more creative
        ),
    )


def main():
    chat = new_chat()
    print(f"Chatbot ready (model: {MODEL}). Type 'quit' to exit, 'reset' to start over.\n")

    # 4. The main loop: read input -> send to LLM -> print answer -> repeat
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("Bye!")
            break
        if user_input.lower() == "reset":
            chat = new_chat()
            print("--- New conversation started ---\n")
            continue

        try:
            response = chat.send_message(user_input)
            print(f"Bot: {response.text}\n")
        except Exception as error:
            # Network problems, wrong key, rate limits etc. end up here
            print(f"Something went wrong: {error}\n")


# This line means: only run main() when the file is run directly
if __name__ == "__main__":
    main()
