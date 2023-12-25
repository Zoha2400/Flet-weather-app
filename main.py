# import flet as ft
# from flet import Text, TextField, FloatingActionButton, Image, Container, Row
# import requests as req
#
# def main(page: ft.Page):
#     #window main params
#     page.title = "Weather App"
#     page.window_width = 600
#     page.window_height = 600
#     page.window_resizable = False
#
#     def getGeo(name):
#         apikey = '658960280a870348580836nqxea7e6f'
#         geo_code_url = f"https://geocode.maps.co/search?q={name}&api_key={apikey}"
#         res = req.get(url=geo_code_url)
#         data_geocode = res.json()
#
#         lat = data_geocode[0]["lat"]
#         lon = data_geocode[0]["lon"]
#         return [lat, lon]
#
#     def getWeather(name):
#         apikey = 'a143100e-2bd8-473e-ac37-a6df3f33794a'
#         lat, lon = getGeo(name)
#
#         res = req.get(f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true&lang=ru_RU", headers={'X-Yandex-API-Key': apikey})
#         data_weather = res.json()
#         country_name = data_weather["geo_object"]["country"]["name"]
#         temp = data_weather["fact"]["temp"]
#         feels_like = data_weather["fact"]["feels_like"]
#         condition = data_weather["fact"]["condition"]
#         wind_speed = data_weather["fact"]["wind_speed"]
#         pressure = data_weather["fact"]["pressure_pa"]
#         humidity = data_weather["fact"]["humidity"]
#         daytime = data_weather["fact"]["daytime"]
#         prec_type = data_weather["fact"]["prec_type"]
#         icon = f"https://yastatic.net/weather/i/icons/funky/dark/{data_weather['fact']['icon']}.svg"
#
#         page.add(
#             [
#             Image(src=icon, width=100, height=100),
#             Text(value=f"{country_name}/{name}"),
#             Text(value=f"день"),
#             Text(value=f"Температура: {temp}°C"),
#             Text(value=f"Чувствуется как: {feels_like}°C"),
#             Text(value=f"{condition}"),
#             Text(value=f"Скорость ветра: {wind_speed}м/c"),
#             Text(value=f"Давление(pa): {pressure}"),
#             Text(value=f"Влажность: {humidity}%"),
#             ]
#         )
#         page.update()
#
#         #return [country_name, temp, feels_like, condition, wind_speed, pressure, humidity, daytime, prec_type, icon]
#
#     def find_city(e):
#         if search_input.value != '':
#             getWeather(search_input.value)
#             print(search_input.value)
#             search_input.value = ''
#
#     search_input = TextField(value='', hint_text='Find your city', border_radius=15, border_color='white', color='white')
#     find_button = FloatingActionButton(icon=ft.icons.ADD, on_click=find_city)
#
#     page.add(
#         Row(
#             [search_input, find_button],
#             alignment=ft.MainAxisAlignment.CENTER
#         ),
#     )
#
# ft.app(target=main)


import flet as ft
from flet import Text, TextField, FloatingActionButton, Image, Row
import requests as req


def main(page: ft.Page) :
    # window main params
    page.title = "Weather App"
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False

    def getGeo(name) :
        try :
            apikey = '658960280a870348580836nqxea7e6f'
            geo_code_url = f"https://geocode.maps.co/search?q={name}&api_key={apikey}"
            res = req.get(url=geo_code_url)
            res.raise_for_status()  # Проверка наличия ошибок при запросе
            data_geocode = res.json()

            lat = data_geocode[0]["lat"]
            lon = data_geocode[0]["lon"]
            return lat, lon
        except Exception as e :
            print(f"Error in getGeo: {e}")
            return None

    def getWeather(name) :
        try:
            apikey = 'a143100e-2bd8-473e-ac37-a6df3f33794a'
            lat, lon = getGeo(name)

            if lat is None or lon is None :
                print("Unable to get geo data.")
                return

            res = req.get(f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true&lang=ru_RU",
                          headers={'X-Yandex-API-Key' : apikey})
            res.raise_for_status()  # Проверка наличия ошибок при запросе
            data_weather = res.json()
            global country_name, temp, feels_like, condition, wind_speed, pressure, humidity, icon, inpname
            country_name = data_weather["geo_object"]["country"]["name"]
            temp = data_weather["fact"]["temp"]
            feels_like = data_weather["fact"]["feels_like"]
            condition = data_weather["fact"]["condition"]
            wind_speed = data_weather["fact"]["wind_speed"]
            pressure = data_weather["fact"]["pressure_pa"]
            humidity = data_weather["fact"]["humidity"]
            icon = f"https://yastatic.net/weather/i/icons/funky/dark/{data_weather['fact']['icon']}.svg"
            inpname = name

            page.update()

        except Exception as e :
            print(f"Error in getWeather: {e}")

    def find_city(e) :
        try :
            if search_input.value != '' :
                getWeather(search_input.value)
                print(search_input.value)
                search_input.value = ''
        except Exception as e:
            print(f"Error in find_city: {e}")

    def change_theme(e) :
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    search_input = TextField(value='', label='Find your city', border_radius=15, border='UNDERLINE',
                             border_color='grey')
    find_button = FloatingActionButton(icon=ft.icons.ADD, on_click=find_city)

    getWeather('Берлин')

    page.add(
        Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme)
            ]
        ),
        Row(
            [search_input, find_button],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        Row([Image(src=icon, width=200, height=200)], alignment=ft.MainAxisAlignment.CENTER),
        Row([Text(value=f"{country_name}/{inpname}")], alignment=ft.MainAxisAlignment.CENTER),
        Row([Text(value=f"день")], alignment=ft.MainAxisAlignment.CENTER),
        Row([Text(value=f"Температура: {temp}°C")], alignment=ft.MainAxisAlignment.CENTER),
        Row([Text(value=f"Скорость ветра: {wind_speed}м/c")], alignment=ft.MainAxisAlignment.CENTER),
        Row([Text(value=f"Давление(pa): {pressure}")], alignment=ft.MainAxisAlignment.CENTER),
        Row([Text(value=f"Влажность: {humidity}%")], alignment=ft.MainAxisAlignment.CENTER),
    )
    page.update()

ft.app(target=main)
