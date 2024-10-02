from langchain_ollama import OllamaLLM

# Function to retrieve the LLM model based on the model name provided
def load_llm_model(model_name):
    if model_name == "ollama-llama3.1":
        return OllamaLLM(model="llama3.1")
