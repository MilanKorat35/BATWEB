from django.shortcuts import render
import requests

def get_weather(city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        weather_data = get_weather(city)
        if weather_data['cod'] == '404':
            error_message = 'City not found. Please enter a valid city name.'
            return render(request, 'weather_app/home.html', {'error_message': error_message})
        else:
            weather_info = {
                'city': weather_data['name'],
                'country': weather_data['sys']['country'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
            }
            return render(request, 'weather_app/home.html', {'weather_info': weather_info})
    return render(request, 'weather_app/home.html')
