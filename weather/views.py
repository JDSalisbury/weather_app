from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8411709dfd1a3f1f2309d18434e9b26'
    city = 'Columbus'

    r = requests.get(url.format(city)).json()


    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    print(city_weather)
    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
