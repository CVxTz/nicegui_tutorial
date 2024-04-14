import datetime

import requests
from nicegui import ui

from nicegui_app.header import add_head_html


class SentimentData:
    def __init__(self):
        self.data = None

    def update_data(self, date):
        if date:
            url = f"https://tradestie.com/api/v1/apps/reddit?date={date}"

            result = requests.get(url)

            if result.status_code == 200:
                result_json = result.json()
                if result_json:
                    self.data = result_json
                else:
                    ui.notify("No data found for this date, pick another date.")


@ui.refreshable
def render_data(data):
    with ui.grid(columns=10).classes("w-full"):
        for company in data:
            color = "green" if company["sentiment_score"] >= 0 else "red"
            with ui.card().classes(
                "text-white transition-transform transform hover:scale-105 shadow-lg"
            ).style(f"background-color: {color}"):
                ui.label(f"Ticker         : {company['ticker']}")
                ui.label(f"Sentiment      : {company['sentiment']}")
                ui.label(f"Sentiment Score: {company['sentiment_score']}")


def wsb():
    add_head_html()

    sentiment_data = SentimentData()
    default_value = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime(
        "%Y-%m-%d"
    )

    sentiment_data.update_data(default_value)

    with ui.grid(columns=12).classes("w-full"):
        col1 = ui.column().classes("col-span-2 p-6")
        col2 = ui.column().classes(
            "col-span-10 w-full rounded-lg p-6 flex justify-center"
        )
        with col2:
            render_data(sentiment_data.data)

        with col1:
            date = ui.date(
                value=default_value,
                on_change=lambda _: (
                    sentiment_data.update_data(date.value),
                    render_data.refresh(sentiment_data.data),
                ),
            )
