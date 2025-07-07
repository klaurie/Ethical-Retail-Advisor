import os
from backend.llm_support.client_setup import setup_client

def parse_response(response):
    """
    Parse the response from the LLM and return the relevant information.

    Args:
        response (str): The response from the LLM.

    Returns:
        str: The parsed response.
    """
    # TODO: Implement more logic for choosing the best response
    return response.choices[0].message.content

def query_llm(query: str, client):
    """
    Query the LLM with a given prompt and return the response.

    Args:
        query (str): The prompt to send to the LLM.
        model (str): The model to use for querying the LLM.
        temperature (float): The temperature setting for the LLM.

    Returns:
        str: The response from the LLM.
    """
    # TODO: Integrate with model providers other than DeepSeek
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": os.getenv("LLM_SYSTEM_PROMPT", "You are an assitant that helps users find information about companies and their products.")},
        {"role": "user", "content": query},
    ],
    stream=False
    )
    # Placeholder for actual LLM querying logic
    # This should be replaced with actual API calls to the LLM service
    return f"{parse_response(response)}"

if __name__ == "__main__":
    client = setup_client()
    print(query_llm("Tell me about the latest iPhone model.", client))