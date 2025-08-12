# AI Agent with Streamlit GUI

This is a simple AI Agent project with a **Streamlit** GUI, integrating a custom AI logic from `myagent.py`.

## 📂 Project Structure

```
AI_AGENT/
│
├── app.py              # Streamlit application
├── myagent.py          # AI logic and process_user_input function
├── main_gui.py         # Optional GUI logic functions
└── README.md           # Project documentation
```

## 🚀 Features
- Streamlit-based GUI
- Modular AI logic in `myagent.py`
- Easy to customize and extend

## ⚙️ Installation

1. **Clone the repository** (or copy the files)
   ```bash
   git clone <your-repo-url>
   cd AI_AGENT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   *Example `requirements.txt`*:
   ```
   streamlit
   ```

## ▶️ Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

## 🛠 Troubleshooting

- Make sure the `process_user_input` function exists in **myagent.py**.
- If you remove `main_gui.py`, also remove its import from **app.py**.
- Keep file names consistent with imports.

## 📜 License
This project is for learning purposes only.
