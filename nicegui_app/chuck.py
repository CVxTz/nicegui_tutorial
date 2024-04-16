import requests
from nicegui import ui

from nicegui_app.header import add_head_html

CATEGORIES = [
    "animal",
    "career",
    "celebrity",
    "dev",
    "fashion",
    "food",
    "money",
    "movie",
    "music",
    "science",
    "sport",
    "travel",
]


class Fact:
    def __init__(self):
        self.fact = None

    def update_fact(self, category):
        url = f"https://api.chucknorris.io/jokes/random?category={category}"

        for i in range(10):
            result = requests.get(url)

            if result.status_code == 200:
                result_json = result.json()
                if self.fact != result_json["value"]:
                    self.fact = result_json["value"]
                    break


def chuck():
    add_head_html()
    default_value = CATEGORIES[0]

    fact = Fact()
    fact.update_fact(default_value)

    with ui.grid(columns=12).classes("w-full"):
        with ui.column().classes("col-span-4 sm:col-span-2 space-x-0"):
            ui.label("Pick a fact category:")
            category = ui.radio(
                CATEGORIES,
                value=default_value,
                on_change=lambda _: fact.update_fact(category.value),
            ).classes("w-full")
            ui.button(
                "⟳ Re-Generate", on_click=lambda _: fact.update_fact(category.value)
            )

        with ui.column().classes(
            "flex col-span-8 sm:col-span-10 w-full justify-center mx-auto max-w-screen-md"
        ):
            ui.label().bind_text_from(fact, "fact").classes(
                "text-lg sm:text-3xl text-gray-800 bg-gray-100 rounded-lg shadow-lg p-6"
            )
