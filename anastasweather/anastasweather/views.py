import requests
   from django.shortcuts import render

   def get_weather(city):
       api_key = 'YOUR_API_KEY'
       url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
       response = requests.get(url)
       return response.json()

   def weather_view(request):
       city = request.GET.get('city', 'Moscow')  # По умолчанию - Москва
       weather_data = get_weather(city)
       return render(request, 'weather/weather.html', {'weather': weather_data})