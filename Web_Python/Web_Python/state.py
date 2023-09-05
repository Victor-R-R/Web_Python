import reflex as rx
import openai
from Web_Python import openai_env

openai.api_key = openai_env.API_KEY

class State(rx.State):
    question: str

    chat_history: list[tuple[str,str]]

    def answer(self):
        session = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role":"user", "content":self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        answer = ""
        self.chat_history.append((self.question, answer))
        for item in session:
            if hasattr(item.choices[0].delta,"content"):
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.question, answer)
                yield
