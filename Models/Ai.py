"""A single AI model"""
import openai
import anthropic


class Ai:
    name: str
    version: str
    url: str | None
    key: str
    client_name: str
    client: openai.OpenAI | anthropic.Anthropic

    def __init__(self, name: str, version: str, url: str | None, key: str, client_name: str):
        self.name = name
        self.version = version
        self.url = url
        self.key = key
        self.client_name = client_name
        self.client = self.establish_connection()

    def __str__(self):
        return self.name + " " + self.version

    def establish_connection(self) -> openai.OpenAI | anthropic.Anthropic:
        # check if api key is set
        if not self.key:
            raise ValueError(f"missing api key for {self.name}")

        # establish connection
        if self.client_name == "ANTHROPIC":
            return anthropic.Anthropic(api_key=self.key)
        elif self.name == "CHATGPT":
            return openai.OpenAI(api_key=self.key)
        else:
            return openai.OpenAI(api_key=self.key, base_url=self.url)

