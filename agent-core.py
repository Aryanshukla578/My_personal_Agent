from database import init_db

def start_agent():
    print("🤖 AI Agent is starting...")
    init_db()
    print("📂 Database initialized successfully.")

def process_input(user_input):
    return f"You said: {user_input}"
