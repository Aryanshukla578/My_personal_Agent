# AI Agent with Streamlit GUI

This project is an **AI-powered agent** with a **Streamlit-based web interface**.  
It uses separate Python modules for **AI logic** (`myagent.py`) and **helper functions** (`main_gui.py`) to keep the code clean and modular.

---

## 📂 Project Structure
AI_AGENT/
│
├── app.py # Streamlit web app for user interaction
├── myagent.py # AI logic and processing functions
├── main_gui.py # Helper functions / GUI backend code
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Installation

1. **Clone the repository** (or download the project folder):
   ```bash
   git clone https://github.com/your-username/AI_AGENT.git
   cd AI_AGENT
2.**Create and activate a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```
3.Install Dependencies:
pip install -r requirements.txt
🖥️ Usage
Run the Streamlit app:
streamlit run app.py
This will open the web UI in your browser where you can:

Enter your query

Get responses from the AI agent

View results interactively

🧠 How It Works
myagent.py
Contains the core process_user_input() function that processes the user query and returns the AI response.

main_gui.py
Contains helper functions that can be reused in the app.

app.py
Runs a Streamlit interface that:

Takes input from the user

Passes it to process_user_input() from myagent.py

Displays the AI's response

📦 requirements.txt Example
If you don’t have it yet, create a requirements.txt with:
streamlit
If you use other libraries in your AI logic, add them too:
streamlit
openai
requests

🛠️ Troubleshooting
ImportError:
Make sure your Python files (app.py, myagent.py, main_gui.py) are in the same folder and functions are defined before importing.

Streamlit not found:
Run:
pip install streamlit

📜 License
This project is open-source. Feel free to modify and improve it.
