import flet as ft
from flet import Text, TextField, FloatingActionButton, Image

def main(page: ft.Page):
    page.title = "Weather App"

    page.window_width = 450
    page.window_height = 550

    page.window_resizable = False

    hello = Text(value="Hello World")

    page.add(hello)

ft.app(target=main)
