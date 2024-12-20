import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
    API_KEY = '07de5fcaa73be7e367d96ed54981b42a'  # Sign up at OpenWeatherMap for an API key
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    
    for city in cities:
        response = requests.get(url.format(city.name, API_KEY)).json()
        
        if response.get('main'):
            city_weather = {
                'city': city.name,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
    
    context = {
        'weather_data': weather_data,
        'form': form,
    }
    return render(request, 'weather/index.html', context)