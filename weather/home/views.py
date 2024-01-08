from django.shortcuts import render
import requests 
# Create your views here.

# def home(request):
#     data = request.POST.get('cityName')
#     print(data,"aaaaaaaaaaaaaaaaaaaaaaaaa")
#     api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=d4a203db71ba734ce7fd007cef63b89a".format(data)
#     json= requests.get(api)
#     temperature = json['main']['temp']
#     description = json['weather'][0]['description']
#     city = json['name']
#     country = json['sys']['country']

#     print(temperature, description, city, country)
#     return render(request, 'home.html')

def home(request):
    if request.method == 'POST':
        data = request.POST.get('cityName')
        api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=d4a203db71ba734ce7fd007cef63b89a".format(data)
        response = requests.get(api)
        
        if response.status_code == 200:
            # Parse JSON content
            json_data = response.json()

            # Extract data from JSON
            temperature = json_data['main']['temp']
            temperature = int(temperature - 273.15 )
            description = json_data['weather'][0]['description']
            city = json_data['name']
            country = json_data['sys']['country']

            print(temperature, description, city, country)

            return render(request, 'home.html', {'temperature': temperature, 'description': description, 'city': city, 'country': country})
        else:
            # Handle API error
            print("Error: Unable to fetch weather data.")
    
    return render(request, 'home.html')