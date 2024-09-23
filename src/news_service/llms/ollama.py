import ollama
from news_service.llms.prompt import PromptGenerator
import asyncio

class OllamaChat:
    def __init__(self, model_name: str = 'gemma2:2b') -> None:
        self.model = model_name

    async def summarize(self, news_content: str, news_title: str):
        prompt = PromptGenerator.generate_summarization_prompt(news_content=news_content, title=news_title)
        response = ollama.chat(model=self.model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
        ])
        return response['message']['content']
    
    async def batch_summarize(self, new_contents: list[str], news_titles: list[str]):
        summarized_tasks = [self.summarize(content, news_titles[index]) for index, content in enumerate(new_contents)]
        results = await asyncio.gather(*summarized_tasks)
        return results