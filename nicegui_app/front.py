import os

from fastapi import FastAPI
from nicegui import ui

from nicegui_app.chuck import chuck
from nicegui_app.wsb import wsb
from nicegui_app.header import add_head_html


def init(fastapi_app: FastAPI) -> None:
    @ui.page("/", title="Demo NiceGUI App")
    def main_page():
        add_head_html()
        with ui.column().classes("w-full flex justify-center mx-auto max-w-screen-md "):
            ui.label("Such empty! Pick one of the elements in the menu above.").classes("text-2xl")
            ui.image("https://i.imgur.com/C4iPxwN.png").classes("justify-center w-1/2")

    ui.page("/chuck", title="Chuck Norris Facts")(chuck)
    ui.page("/wsb", title="WallStreetBets Tracker")(wsb)

    ui.run_with(
        fastapi_app,
        mount_path="/ui",  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
        storage_secret=os.getenv("STORAGE", "__STORAGE__"),
    )
