import streamlit as st
import time

st.set_page_config(page_title = "ChatBot Demo")
st.title("ChatBot UI Demo")
with st.chat_message("user"):
    st.write("Hello from user side!")
with st.chat_message("assistant"):
    st.write("Hello , I'm your assistant. How can I help you today?")


user_message = st.chat_input("Enter your message")
if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            time.sleep(1.5)
        st.write(f"Hey, you wrote: {user_message}. I'm still in development. Please be patient with me. Thank you.")
