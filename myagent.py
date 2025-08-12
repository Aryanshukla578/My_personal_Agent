import sqlite3
import os
import requests
from dotenv import load_dotenv
import streamlit as st

# Load .env file locally (ignored on Streamlit Cloud)
load_dotenv()

def get_secret(key, default=None):
    """
    Try to get secret from env variables or Streamlit secrets.
    Returns default if not found.
    """
    try:
        return os.getenv(key) or st.secrets[key]
    except KeyError:
        return default

# Load config variables safely
OPENROUTER_API_KEY = get_secret("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = get_secret("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
MODEL_NAME = get_secret("MODEL_NAME", "gpt-oss-20b")

if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY is missing! Please set it in your .env file or Streamlit Secrets.")

print(f"DEBUG: Using API Key starts with: {OPENROUTER_API_KEY[:5]}...")  # For debugging; remove in production

def init_db():
    """Initialize SQLite DB and create table if not exists."""
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
    """Send user input to OpenRouter API and return the AI response."""
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
        print(f"DEBUG: Sending request to {OPENROUTER_BASE_URL}/chat/completions")
        print(f"DEBUG: Headers: {headers}")
        print(f"DEBUG: Payload: {payload}")

        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )

        print(f"DEBUG: Response Status: {response.status_code}")
        print(f"DEBUG: Response Body: {response.text}")

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
    """Get AI response and store the interaction in DB."""
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

def process_user_input(text):
    """Wrapper function for Streamlit or other UIs."""
    return process_input(text)
