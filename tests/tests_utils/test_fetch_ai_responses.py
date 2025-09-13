import unittest
import pytest
from unittest.mock import AsyncMock, MagicMock
from utils import fetch_chatgpt, fetch_gemini, fetch_deepseek, fetch_claude


class TestFetchAIResponses(unittest.TestCase):
    """Test cases for fetch_ai_responses"""

    @pytest.mark.asyncio
    async def test_fetch_chatgpt(self):
        mock_client = AsyncMock()
        mock_client.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="test response"))]
        )
        model_name, response = await fetch_chatgpt(mock_client, "gpt-4", "chatgpt test prompt")
        assert model_name == "CHATGPT"
        assert response == "test response"
        mock_client.chat.completions.create.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_fetch_gemini(self):
        mock_client = AsyncMock()
        mock_client.aio.models.generate_content.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="test response"))]
        )
        model_name, response = await fetch_gemini(mock_client, "gemini", "gemini test prompt")
        assert model_name == "GEMINI"
        assert response == "test response"
        mock_client.aio.models.generate_content.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_fetch_deepseek(self):
        mock_client = AsyncMock()
        mock_client.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="test response"))]
        )
        model_name, response = await fetch_deepseek(mock_client, "deepseek", "deepseek test prompt")
        assert model_name == "DEEPSEEK"
        assert response == "test response"
        mock_client.chat.completions.create.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_fetch_claude(self):
        mock_client = AsyncMock()
        mock_client.messages.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="claude test response"))]
        )
        model_name, response = await fetch_deepseek(mock_client, "claude", "deepseek test prompt")
        assert model_name == "CLAUDE"
        assert response == "test response"
        mock_client.messages.create.assert_awaited_once()


if __name__ == '__main__':
    unittest.main()
