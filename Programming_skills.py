import requests


city_name = input()
appid ='2b46cc6c857f94e34ab172997c5363fc'


def get_weather_celsius(appid: str, city: str):
    """
    Get celsius temperature.
    :param appid: key for authenticated
    :param city: name of city
    :return: float
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}"
    response = requests.get(url).json()
    temp = response['main']['temp']
    return temp

print(get_weather_celsius(appid, city_name))