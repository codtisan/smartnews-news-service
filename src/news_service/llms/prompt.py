class PromptGenerator:

    @staticmethod
    def generate_summarization_prompt(news_content: str, title: str, num_of_points: int = 4) -> str:
        return f'你的任務是要去根據新聞標題去歸納一篇新聞成{num_of_points}要點，你的答案只包括要點並以根據這格式例子：1.XXXXX。2.YYYYY。3.ZZZZZ。你要歸納的新聞標題是：{title}，該新聞是：{news_content}'