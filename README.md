
# Chimtu Chatbot 🤖

Chimtu Chatbot is a conversational AI application built using [Langchain](https://python.langchain.com/en/latest/), [Streamlit](https://streamlit.io/), and the [Ollama LLM](https://ollama.com/). The chatbot provides concise answers based on user questions while maintaining a chat history. It uses a pre-defined large language model to answer questions and avoids fabricating responses when sufficient information is unavailable.

## Features

- Uses **Ollama Llama 3.1** as the language model.
- Integrates with **Streamlit** for a clean and interactive UI.
- Maintains a chat history between user and assistant.
- Provides concise and accurate responses without making up information.

## Installation

### Prerequisites
- **Python 3.8+** must be installed.
- Required Python packages: 
  - `langchain`
  - `streamlit`
  - `ollama`
  
To install dependencies, run:
```bash
pip install langchain streamlit ollama
```

### Running the Chatbot

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/chimtu-chatbot.git
   cd chimtu-chatbot
   ```

2. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

3. **Use in the Console**:
   You can also run the chatbot directly in the console by executing:
   ```bash
   python chatbot.py
   ```

## Project Structure

```
chimtu-chatbot/
│
├── utils.py            # Contains helper functions for loading the language model.
├── chatbot.py          # Core chatbot logic handling user input and responses.
├── app.py              # Streamlit web application.
├── README.md           # Project documentation.
└── requirements.txt    # List of required Python dependencies.
```

## How It Works

1. The language model **Ollama Llama 3.1** is loaded via `utils.py`.
2. **chatbot.py** defines how user inputs and context are processed, generating responses using the loaded LLM.
3. The **Streamlit app** (`app.py`) provides a user-friendly web interface to interact with the chatbot.
4. The chat history is stored and displayed, allowing users to maintain a conversational context.

## Example

```text
User: What is Langchain?
Assistant: Langchain is a framework designed to simplify the creation of applications powered by large language models (LLMs).
```

```

Save this as `README.md` in your project folder, and it will be ready to go when you push the project to GitHub.
