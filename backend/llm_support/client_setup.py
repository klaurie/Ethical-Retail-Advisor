import os
from dotenv import load_dotenv

load_dotenv()

def setup_client():
    """
    Setup the client for the specified model provider and model.
    
    Args:
        model_provider (str): The model provider to use. Default is "deepseek".
        model (str): The model to use. Default is "deepseek-chat".
    
    Returns:
        Client: The configured client.
    """
    model_provider = os.getenv("MODEL_PROVIDER", "")

    if model_provider == "deepseek":
        return setup_deepseek_client()
    elif model_provider == "openai":
        return setup_openai_client()
    elif model_provider == "gemini":
        return setup_gemini_client()
    elif model_provider == "ollama":
        return setup_ollama_client()
    elif model_provider == "huggingface":
        return setup_huggingface_client()
    else:
        raise ValueError(f"Unsupported model provider: {model_provider}")

def setup_deepseek_client():
    """
    Setup the DeepSeek client for the specified model.
    
    Args:
        model (str): The model to use. Default is "deepseek-chat".
    
    Returns:
        DeepSeekClient: The configured DeepSeek client.
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError(
            "The 'openai' package is not installed. "
            "Please install it by running 'pip install openai'."
        )
    
    api_key = os.getenv("DEEPSEEK_API_KEY", None)
    
    if api_key is None:
        raise ValueError("DEEPSEEK_API_KEY environment variable not set")
    else:
        client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_API_BASE_URL", "https://api.deepseek.com"),
        )

    return client

def setup_openai_client(model="gpt-3.5-turbo"):
    """
    Setup the OpenAI client for the specified model.
    
    Args:
        model (str): The model to use. Default is "gpt-3.5-turbo".
    
    Returns:
        OpenAIClient: The configured OpenAI client.
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError(
            "The 'openai' package is not installed. "
            "Please install it by running 'pip install openai'."
        )
    
    api_key = os.getenv("OPENAI_API_KEY", None)
    
    if api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    else:
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com"),
        )

    return client

def setup_gemini_client(model="gemini"):
    """
    Setup the Gemini client for the specified model.
    
    Args:
        model (str): The model to use. Default is "gemini".
    
    Returns:
        GeminiClient: The configured Gemini client.
    """
    try:
        import google.generativeai as genai
    except ImportError:
        raise ImportError(
            "The 'google-generativeai' package is not installed. "
            "Please install it by running 'pip install google-generativeai'."
        )

    api_key = os.getenv("GENAI_API_KEY", None)
    if api_key is None:
        raise ValueError("GENAI_API_KEY environment variable not set")
    else:
        client = genai.Client(api_key="YOUR_API_KEY")

    return client

def setup_ollama_client(model="llama2"):
    """
    Setup the Ollama client for the specified model.
    
    Args:
        model (str): The model to use. Default is "llama2".
    
    Returns:
        Client: The configured Ollama client.
    """
    try:
        from ollama import Client
    except ImportError:
        raise ImportError(
            "The 'ollama' package is not installed. "
            "Please install it by running 'pip install ollama'."
        )
    
    client = Client(
        host='http://localhost:11434',
        headers={}
        )
    
    return client

def setup_huggingface_client():
    """
    Setup the HuggingFace client.
    
    Returns:
        Client: The configured HuggingFace client.
    """
    try:
        from huggingface_hub import InferenceClient 
    except ImportError:
        raise ImportError(
            "The 'huggingface_hub' package is not installed. "
            "Please install it by running 'pip install huggingface_hub'."
        )
    api_key = os.getenv("HUGGINGFACE_API_KEY", None)

    if api_key is None:
        raise ValueError("HUGGINGFACE_API_KEY environment variable not set")
    else:
        client = InferenceClient(repo_id=os.getenv("LLM_MODEL", "bert-base-uncased"), token=api_key)

    return client

if __name__ == "__main__":
    # Example usage    
    client = setup_client()
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are an assstant that helps users find information about companies and their products."},
        {"role": "user", "content": ""},
    ],
    stream=False
    )

    print(response.choices[0].message.content)