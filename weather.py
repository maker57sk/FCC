# for sending request to website

import requests

#pretty print for Json to tree
from pprint import pprint

API_Key = '13b3da2c3ccb0cdcf138c9aca4714087'

city = input("Enter a city:  ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)