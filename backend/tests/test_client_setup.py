import pytest
from unittest.mock import patch, MagicMock
from backend.llm_support.client_setup import setup_client, setup_deepseek_client

# Absolute import for the functions to be tested

# The OpenAI class is imported inside setup_deepseek_client,
# so we need to patch it where it's looked up.
OPENAI_CLIENT_PATH = 'backend.llm_support.client_setup.OpenAI'

@pytest.fixture
def mock_openai_client():
    """Fixture to mock the OpenAI client."""
    with patch(OPENAI_CLIENT_PATH) as mock_client_constructor:
        mock_instance = MagicMock()
        mock_client_constructor.return_value = mock_instance
        yield mock_client_constructor, mock_instance

class TestSetupDeepSeekClient:
    def test_setup_deepseek_client_no_api_key(self, monkeypatch):
        """
        Tests setup_deepseek_client when DEEPSEEK_API_KEY is not set.
        It should raise a ValueError.
        """
        # Ensure DEEPSEEK_API_KEY is not set
        monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)

        with pytest.raises(ValueError) as excinfo:
            setup_deepseek_client()
        assert "DEEPSEEK_API_KEY environment variable not set" in str(excinfo.value)

class TestSetupClient:

    @patch('backend.llm_support.client_setup.setup_deepseek_client')
    def test_setup_client_default_provider(self, mock_setup_deepseek):
        """
        Tests setup_client with the default provider ("deepseek").
        It should call setup_deepseek_client.
        """
        mock_deepseek_instance = MagicMock()
        mock_setup_deepseek.return_value = mock_deepseek_instance

        client = setup_client() # Default provider is "deepseek"

        mock_setup_deepseek.assert_called_once_with() # Called with no args
        assert client == mock_deepseek_instance

    @patch('backend.llm_support.client_setup.setup_deepseek_client')
    def test_setup_client_explicit_deepseek_provider(self, mock_setup_deepseek):
        """
        Tests setup_client explicitly specifying "deepseek" as the provider.
        The 'model' parameter of setup_client is not passed to setup_deepseek_client.
        """
        mock_deepseek_instance = MagicMock()
        mock_setup_deepseek.return_value = mock_deepseek_instance

        client = setup_client(model_provider="deepseek", model="a-specific-model")

        # setup_deepseek_client is called without arguments, so it uses its own defaults
        mock_setup_deepseek.assert_called_once_with()
        assert client == mock_deepseek_instance

    def test_setup_client_unsupported_provider(self):
        """
        Tests setup_client with an unsupported model provider.
        It should raise a ValueError.
        """
        unsupported_provider = "some_other_provider"
        with pytest.raises(ValueError) as excinfo:
            setup_client(model_provider=unsupported_provider)
        assert f"Unsupported model provider: {unsupported_provider}" in str(excinfo.value)


