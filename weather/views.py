from django.shortcuts import render
import requests
from .models import City


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8411709dfd1a3f1f2309d18434e9b26'
    city = 'Columbus'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)



    print(weather_data)
    context = {'weather_data': weather_data}
    return render(request, 'weather/weather.html', context)
