import streamlit as st
import myagent

myagent.init_db()

st.set_page_config(page_title="AI Agent", page_icon="🤖", layout="centered")

st.title("AI Agent 🤖")

user_input = st.text_input("Type your message here:")

if st.button("Send") and user_input.strip():
    response = myagent.process_input(user_input)
    st.write(f"**You:** {user_input}")
    st.write(f"**Agent:** {response}")
