from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8411709dfd1a3f1f2309d18434e9b26'
    city = 'Columbus'

    r = request.get(url.format(city))
    print(r.text)

    return render(request, 'weather/weather.html')
