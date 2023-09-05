import reflex as rx
from Web_Python import style
from Web_Python.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
               style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
               style=style.answer_style,
        ),
        margin_Y="1em",       
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a Question",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_blur=State.answer,
            style=style.button_style,
        ),
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )

app = rx.App()
app.add_page(index)
app.compile()