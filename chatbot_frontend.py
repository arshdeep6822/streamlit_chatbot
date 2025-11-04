import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot_backend import chatbot

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:

    with st.chat_message('user'):
        st.write(user_input)
    st.session_state['message_history'].append({'role':'user', 'content': user_input})

    with st.chat_message('assistant'):
        response = chatbot.invoke({'messages':[HumanMessage(user_input)]},  config={"configurable": {"thread_id": "chat_1"}})
        st.write(response['messages'][-1].content)
    st.session_state['message_history'].append({'role':'assistant', 'content':response['messages'][-1].content })