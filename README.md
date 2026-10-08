# CLI Chatbot

A command-line chatbot built with Python and the Google Gemini API. It keeps conversation memory and uses a system prompt to control its behavior.

## What I learned
- Calling an LLM API from Python
- Keeping secrets out of code with `.env` files
- System prompts and temperature
- Conversation memory (chat history)

## How to run
```bash
python -m venv venv
# Windows: venv\Scripts\activate   |   Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
# copy .env.example to .env and add your Gemini API key
python chatbot.py
```

Commands: `quit` to exit, `reset` to start a new conversation.
