import requests
   from django.shortcuts import render

   def weather_view(request):
       city = request.GET.get('city', 'London')  # По умолчанию Лондон
       api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Замените на ваш API-ключ
       url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

       response = requests.get(url)
       data = response.json()

       if response.status_code == 200:
           context = {
               'city': city,
               'temperature': data['main']['temp'],
               'description': data['weather'][0]['description'],
           }
       else:
           context = {
               'error': data['message'],
           }

       return render(request, 'weather/weather.html', context)

