import sqlite3
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-oss-20b")

if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY is missing! Please set it in your .env file.")

def init_db():
    """Initialize SQLite database for storing chat history."""
    conn = sqlite3.connect("agent.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_ai_response(user_input):
    """Call OpenRouter API and return AI-generated text."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions", 
            headers=headers, json=payload, timeout=30
        )
        response.raise_for_status()
        data = response.json()

        if "choices" not in data or not data["choices"]:
            return "[Error: Unexpected API response format]"

        return data["choices"][0]["message"]["content"].strip()

    except requests.exceptions.RequestException as e:
        return f"[Error: Failed to reach OpenRouter API - {e}]"
    except Exception as e:
        return f"[Error: {e}]"

def process_input(user_input):
    """Process user input, get AI response, and store in DB."""
    response = get_ai_response(user_input)

    try:
        conn = sqlite3.connect("agent.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO interactions (user_input, bot_response) VALUES (?, ?)",
            (user_input, response)
        )
        conn.commit()
    except sqlite3.Error as e:
        return f"[Database Error: {e}]"
    finally:
        conn.close()

    return response

# ✅ Add this wrapper for Streamlit
def process_user_input(text):
    """Wrapper function for Streamlit to keep naming consistent."""
    return process_input(text)
