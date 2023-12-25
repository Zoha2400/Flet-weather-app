import flet as ft
from flet import Text, TextField, FloatingActionButton, Image, Container, Row
import requests as req

def main(page: ft.Page):

    #window main params
    page.title = "Weather App"
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False


    geocode = 'Ташкент'

    def getGeo():
        apikey = '658960280a870348580836nqxea7e6f'
        geo_code_url = f"https://geocode.maps.co/search?q={geocode}&api_key={apikey}"
        res = req.get(url=geo_code_url)
        data_geocode = res.json()
        print(data_geocode)

        lat = data_geocode[0]["lat"]
        lon = data_geocode[0]["lon"]
        return [lat, lon]

    def getWeather():
        apikey = 'a143100e-2bd8-473e-ac37-a6df3f33794a'
        lat, lon = getGeo()

        res =req.get(f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true", headers={'X-Yandex-API-Key': apikey})
        data_weather = res.json
        print(data_weather)

    getWeather()

    hello = Text(value='Weather App.')

    page.add(hello)

ft.app(target=main)
