# -*- coding:utf-8 -*-
# https://blog.streamlit.io/ai-talks-chatgpt-assistant-via-streamlit/
import streamlit as st
from conversation import show_chat_buttons, show_text_input, show_conversation

# --- GENERAL SETTINGS ---
PAGE_TITLE: str = "Eatwhat"
PAGE_ICON: str = "./src/1F260.png"

# Storing The Context
if "generated" not in st.session_state:
    st.session_state.generated = []
if "past" not in st.session_state:
    st.session_state.past = []
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_text" not in st.session_state:
    st.session_state.user_text = ""

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
)


def main() -> None:
    if st.session_state.user_text:
        show_conversation()
        st.session_state.user_text = ""
    show_text_input()
    show_chat_buttons()


if __name__ == "__main__":
    st.markdown(
        f"<h2 style='text-align: center;'>😋我是你的饮食助手</h1>",
        unsafe_allow_html=True,
    )
    main()
