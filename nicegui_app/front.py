import os

from fastapi import FastAPI
from nicegui import ui

from nicegui_app.chuck import chuck
from nicegui_app.wsb import wsb


def init(fastapi_app: FastAPI) -> None:
    ui.page("/chuck", title="Chuck Norris Facts")(chuck)
    ui.page("/wsb", title="WallStreetBets Tracker")(wsb)

    ui.run_with(
        fastapi_app,
        mount_path="/",  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
        storage_secret=os.getenv("STORAGE", "__STORAGE__"),
    )
