# -*- coding:utf-8 -*-
import streamlit as st
from typing import List
from openai import OpenAI, OpenAIError
from streamlit_chat import message


def clear_chat() -> None:
    st.session_state.generated = []
    st.session_state.past = []
    st.session_state.messages = []
    st.session_state.user_text = ""


def show_text_input() -> None:
    st.text_area(
        label="告诉我你的想法💡:",
        value=st.session_state.user_text,
        key="user_text",
    )


def show_chat_buttons() -> None:
    b0, b1 = st.columns(2)
    with b0, b1:
        b0.button(label="Ask")
        b1.button(label="Clear", on_click=clear_chat)


def create_gpt_completion(
    messages: List[dict] = [
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
) -> dict:
    api_key = "sk-MHsqURJak3XEGYiYv3PSWC5v1UqqwyJASf7dMWqyxGig2u1K"
    base_url = "https://api.chatanywhere.tech"

    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
        base_url=base_url,
    )

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    return chat_completion


def show_chat(ai_content: str, user_text: str) -> None:
    if ai_content not in st.session_state.generated:
        # store the ai content
        st.session_state.past.append(user_text)
        st.session_state.generated.append(ai_content)
    if st.session_state.generated:
        for i in range(len(st.session_state.generated)):
            message(
                st.session_state.past[i],
                is_user=True,
                key=str(i) + "_user",
                # avatar_style="micah",
            )
            if False:
                message("", key=str(i))
                st.markdown(st.session_state.generated[i])
            else:
                message(
                    st.session_state.generated[i],
                    is_user=True,
                    key=str(i),
                )


def show_gpt_conversation() -> None:
    try:
        completion = create_gpt_completion(st.session_state.messages)
        ai_content = completion.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": ai_content})
        if ai_content:
            show_chat(ai_content, st.session_state.user_text)
            st.divider()
        # show_audio_player(ai_content)
    except (OpenAIError, UnboundLocalError) as err:
        st.error(err)


def show_conversation() -> None:
    if st.session_state.messages:
        st.session_state.messages.append(
            {"role": "user", "content": st.session_state.user_text}
        )
    else:
        ai_role_prefix = "你是一个专业美食家，"
        ai_role_postfix = "请根据我的问题谨慎回答问题，回答问题的过程中，请介绍相关的营养知识，如果我问你吃什么，请给我推荐相关的菜肴"
        ai_role = f"{ai_role_prefix}{ai_role_postfix}"
        st.session_state.messages = [
            {"role": "system", "content": ai_role},
            {"role": "user", "content": st.session_state.user_text},
        ]
    show_gpt_conversation()
