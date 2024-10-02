import streamlit as st
from chatbot import handle_chat

# Set the title of the web app
st.title("Chimtu Chatbot :dog2:")

# Initialize chat history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input from chat box
if prompt := st.chat_input("Hi! Enter your question or type 'BYE' to exit"):
    if prompt.lower() == 'bye':
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown("Goodbye!")
        # Clear the session state chat history
        st.session_state.messages = []
    else:
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display the assistant's response
        with st.chat_message("assistant"):
            response = handle_chat(prompt)
            st.markdown(response)
        
        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
