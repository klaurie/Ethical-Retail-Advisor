import json
SYSTEM_PROMPT = "You are an assistant that helps users find information about companies and their products."

class LLM_Client():
    def __init__(self, model, client, provider):
        self.client = client
        self.model = model
        self.provider = provider

    def get_company_name(self, query):
        """
        Get the company name from the query using the LLM.
        
        Args:
            query (str): The query to process.
        
        Returns:
            str: The identified company name.
        """
        extraction_tools = [
            {
                "type": "function",
                "name": "get_company_name",
                "description": "Get the company name from a query",
                "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "The name of the company mentioned. If none, return an empty string.",
                    },
                },
                "required": ["company_name"],
                }
            }
        ]
        
        # Run query with required call to get_company_name tool
        response = self.client.responses.create(
            model=self.model,
            tools=extraction_tools,
            input=query,
            tool_choice={"type": "function","name": "get_company_name"},
        )

        # Get the list of arguments for the tool call
        tool_call = response.output[0].arguments

        # Convert string to dictionary
        args = json.loads(tool_call)

        # Get extracted company name from the arguments
        company_name = args.get("company_name", "").strip()

        print(f"Tool call: {company_name}")
        return company_name