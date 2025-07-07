import re
from typing import Optional

def clean_query(query: str) -> str:
    """
    Clean the query to extract the company name by removing unnecessary phrases and punctuation.

    input:
        query (str): The input query string that may contain company names and additional context.

    output:
        str: A cleaned version of the query that focuses on the company name.
    """
    if not query or not query.strip():
        return ""
    
    # Clean the query: remove extra whitespace and convert to lowercase for processing
    cleaned_query = query.strip().lower()
    
    # Remove punctuation
    cleaned_query = re.sub(r'[?!.]', '', cleaned_query)

    # Removing common phrases that do not contribute to the company name and apostrophes
    removal_patterns = [
        r'\b(what do you know about|tell me about|give me info on|give me information about|do you know anything about|how ethical is|is|what about|can you find info on|show me|what are)\b',
        r"'[^ ]*",
    ]
    
    # Apply removal patterns
    for pattern in removal_patterns:
        cleaned_query = re.sub(pattern, '', cleaned_query, flags=re.IGNORECASE)
    
    # Remove extra whitespace
    cleaned_query = re.sub(r'\s+', ' ', cleaned_query).strip()

    # If we still have content, return it; otherwise return the original query
    if cleaned_query:
        return cleaned_query.title()  # Return in title case
    else:
        # Fallback: return the original query if cleaning removed everything just in case!
        return query.strip()


def identify_company(query: str) -> str:
    """
    Identify the company name from the query.

    Use a basic LLM to extract the company name from the query.
    
    input:
        query (str): The input query string that may contain company names and additional context.

    output:
        str: The identified company name, or an empty string if no valid company name is found.
    """
    # Prompt to use with the LLM for company identification

    # merge prompt with the cleaned query

    # query LLM to identify the company name

    # parse response to extract the company name
    
    # return identified company name
def fuzzy_search(query: str) -> str:
    """
    Perform a fuzzy search to find the best matching company.
    """
    pass

def collect_company_info(query: str) -> str:
    """
    Perform a web search to find ethical information about the company.

    """
    pass

def evaluate_company_ethics(company_info: str) -> int:
    """
    Evaluate the ethical score of the company based on the collected information.
    """
    pass


def web_search(query: str) -> str:
    """
    Perform a web search to find information about the company.

    This function is a placeholder for actual web search logic.
    It should return a string containing the search results.
    """
    pass

def process_search_result(search_result: str) -> None:
    """
    Process the search result to extract relevant company information.

    This function is a placeholder for actual processing logic.
    It should extract and return relevant information from the search result.
    """
    pass


def get_company_info(query: str) -> str:
    """
    Get the company information based on the query.

    This function orchestrates the process of identifying the company,
    processing the query, performing a fuzzy search, collecting information,
    evaluating ethics, and populating the database.
    """
    # Clean query before identifying company name
    clean_query = clean_query(query)
    # Extract company name from the query
    company = identify_company(query)
    
    # Log the extracted company name for debugging
    print(f"Extracted company name: '{company}' from query: '{query}'")

    # Search through database for company (fuzzy should account for  any spelling errors)
    company_info = fuzzy_search(company)

    # If no fuzzy result is found, perform a web search to populate the database
    if not company_info:
        company_search_result = web_search(company)

        # TODO: Handle case where no company is found
        if not company_search_result:
            raise ValueError(f"No company found for the given query: '{query}' (extracted: '{company}')")
        
        # Process the search result to extract relevant information
        company_info = process_search_result(company_search_result)

    # Collect ethical information about the company
    ethics_score = evaluate_company_ethics(company_info)

    return f"Company: {company}, Ethics Score: {ethics_score}"
