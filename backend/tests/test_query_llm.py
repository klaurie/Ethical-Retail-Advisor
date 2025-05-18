import unittest
from unittest.mock import MagicMock
from backend.llm_support.query_llm import parse_response, query_llm

# Absolute import for the functions to be tested

# Helper classes to mock the LLM API response structure
class MockMessage:
    def __init__(self, content):
        self.content = content

class MockChoice:
    def __init__(self, content):
        self.message = MockMessage(content)

class MockLLMAPIResponse:
    def __init__(self, content):
        self.choices = [MockChoice(content)]

class TestLLMQuery(unittest.TestCase):

    def test_parse_response(self):
        """
        Tests if parse_response correctly extracts content from a mock LLM response.
        """
        # ARRANGE
        expected_content = "This is the LLM's answer."
        mock_llm_response = MockLLMAPIResponse(content=expected_content)

        # ACT
        result = parse_response(mock_llm_response)

        # ASSERT
        self.assertEqual(result, expected_content)

    def test_query_llm(self):
        """
        Tests if query_llm calls the client with correct parameters
        and returns the parsed response.
        """
        # ARRANGE
        test_query = "Tell me about the latest AI advancements."
        expected_response_content = "AI is advancing rapidly, especially in generative models."

        # Create a mock client
        mock_client = MagicMock()

        # Configure the mock client's chat.completions.create method
        # to return a mock response object that parse_response can process.
        mock_api_response = MockLLMAPIResponse(content=expected_response_content)
        mock_client.chat.completions.create.return_value = mock_api_response

        # ACT
        actual_response = query_llm(test_query, mock_client)

        # ASSERT
        # Verify that the client's create method was called once with the expected arguments
        mock_client.chat.completions.create.assert_called_once_with(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an assstant that helps users find information about companies and their products."},
                {"role": "user", "content": test_query},
            ],
            stream=False
        )

        # Verify that the response from query_llm is the content parsed from the mock API response
        self.assertEqual(actual_response, expected_response_content)
        def test_query_llm_api_call_raises_exception(self):
            """
            Tests if query_llm correctly propagates an exception from the API call.
            """
            # ARRANGE
            test_query = "Test query for API failure."
            mock_client = MagicMock()
            
            # Configure the client's method to raise an exception
            api_error_message = "Simulated API Error"
            # For older unittest.mock versions, side_effect might need to be an instance
            mock_client.chat.completions.create.side_effect = RuntimeError(api_error_message)
            
            # ACT & ASSERT
            with self.assertRaises(RuntimeError) as context:
                query_llm(test_query, mock_client)
            
            self.assertEqual(str(context.exception), api_error_message)
            # Verify that the client's create method was called once with the expected arguments
            mock_client.chat.completions.create.assert_called_once_with(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are an assstant that helps users find information about companies and their products."},
                    {"role": "user", "content": test_query},
                ],
                stream=False
            )

        @unittest.mock.patch('backend.llm_support.query_llm.parse_response')
        def test_query_llm_parse_response_raises_exception(self, mock_parse_response):
            """
            Tests if query_llm correctly propagates an exception from parse_response.
            """
            # ARRANGE
            test_query = "Test query for parse failure."
            mock_client = MagicMock()
            
            # Mock the API call to return a dummy response.
            # This response object doesn't need to be complex as parse_response is mocked
            # and won't actually process its structure.
            dummy_api_response_object = MagicMock() 
            mock_client.chat.completions.create.return_value = dummy_api_response_object
            
            # Configure the mocked parse_response to raise an exception
            parse_error_message = "Simulated Parsing Error"
            mock_parse_response.side_effect = AttributeError(parse_error_message)
            
            # ACT & ASSERT
            with self.assertRaises(AttributeError) as context:
                query_llm(test_query, mock_client)
                
            self.assertEqual(str(context.exception), parse_error_message)
            
            # Verify the API call was made
            mock_client.chat.completions.create.assert_called_once_with(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are an assstant that helps users find information about companies and their products."},
                    {"role": "user", "content": test_query},
                ],
                stream=False
            )
            # Verify parse_response was called with the object returned by the API call
            mock_parse_response.assert_called_once_with(dummy_api_response_object)

if __name__ == '__main__':
    unittest.main()