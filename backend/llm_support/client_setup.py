import os
from dotenv import load_dotenv

load_dotenv()

def setup_client(model_provider="deepseek", model="deepseek-chat"):
    """
    Setup the client for the specified model provider and model.
    
    Args:
        model_provider (str): The model provider to use. Default is "deepseek".
        model (str): The model to use. Default is "deepseek-chat".
    
    Returns:
        Client: The configured client.
    """
    #TODO: Add support for other model providers
    if model_provider == "deepseek":
        return setup_deepseek_client()
    else:
        raise ValueError(f"Unsupported model provider: {model_provider}")

def setup_deepseek_client(model="deepseek-chat"):
    """
    Setup the DeepSeek client for the specified model.
    
    Args:
        model (str): The model to use. Default is "deepseek-chat".
    
    Returns:
        DeepSeekClient: The configured DeepSeek client.
    """
    from openai import OpenAI
    api_key = os.getenv("DEEPSEEK_API_KEY", None)
    
    if api_key is None:
        raise ValueError("DEEPSEEK_API_KEY environment variable not set")
    else:
        client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_API_BASE_URL", "https://api.deepseek.com"),
        )

    return client

if __name__ == "__main__":
    # Example usage    
    client = setup_client()
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
    )

    print(response.choices[0].message.content)