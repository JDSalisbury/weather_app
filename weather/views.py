from django.shortcuts import render

# Create your views here.
def index(request):
    retun render(request, 'weather/weather.html')
