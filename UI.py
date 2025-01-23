import streamlit as st
from openai import OpenAI
import os

# Initialize the OpenAI client with DeepSeek configuration
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY", "your-api-key-here"),
    base_url="https://api.deepseek.com"
)

# Set page configuration
st.set_page_config(page_title="DeepSeek Chat", page_icon="💭")
st.title("DeepSeek Chat Interface")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]

# Display chat messages
for message in st.session_state.messages[1:]:  # Skip the system message
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to ask?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response
        response = client.chat.completions.create(
            model='deepseek-reasoner',
            messages=st.session_state.messages,
            stream=True
        )
        
        reasoning_content = ""
        for chunk in response:
            if chunk.choices[0].delta.reasoning_content:
                reasoning_content += chunk.choices[0].delta.reasoning_content
            elif chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.write(full_response + "▌")
        
        # Display final response and reasoning if available
        message_placeholder.write(full_response)
        if reasoning_content:
            with st.expander("Show reasoning"):
                st.write(reasoning_content)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
