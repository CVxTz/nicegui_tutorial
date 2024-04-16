from pathlib import Path

from nicegui import ui

STYLE_CSS = (Path(__file__).parent / "static" / "style.css").read_text()


def add_head_html() -> (
    None
):  # https://github.com/zauberzeug/nicegui/blob/main/website/header.py
    """Add the code from header.html and reference style.css."""
    ui.add_head_html(f"<style>{STYLE_CSS}</style>")
    with ui.header().classes("flex"):
        ui.label("Chuck Norris Random Facts").classes(
            "text-white text-lg"
        )

