from langchain_core.prompts import ChatPromptTemplate
from utils import load_llm_model

# Load the Ollama Llama model
llm_model = load_llm_model("ollama-llama3.1")

# Template for constructing the chatbot prompt
template_text = """
You are an Assistant, answer the user question below. Be concise and don't make up answers if you don't have sufficient information.
Here is the chat history: {context}

User question: {user_q}
"""
# Create a prompt template from the string template
prompt_template = ChatPromptTemplate.from_template(template_text)

# Initialize an empty list for conversation history
conversation_history = []

# Function to handle chat responses, combining the prompt with the model
def generate_response(user_input, chat_history):
    chain = prompt_template | llm_model
    assistant_response = chain.invoke({"user_q": user_input, "context": chat_history})
    return assistant_response

# Function to manage the chat, append user and bot messages to history
def handle_chat(user_input) -> str:
    # Convert chat history to string format
    history_str = "\n".join(entry for entry in conversation_history)
    # Generate assistant's response based on user input and chat history
    assistant_response = generate_response(user_input, history_str)
    # Update the chat history with the latest user and bot messages
    conversation_history.append(f"User: {user_input}")
    conversation_history.append(f"Assistant: {assistant_response}")
    return assistant_response

# Main function to handle interactive command-line chat
if __name__ == "__main__":
    print("Welcome to Echo chatbot, press 'Q' to exit!")
    while True:
        # Take user input from the console
        user_input = input("Enter your question: ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        # Generate and print the bot response
        assistant_response = handle_chat(user_input)
        print(assistant_response)
