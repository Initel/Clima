import requests
import random

cities = ["New York", "London", "Paris", "Tokyo", "Sydney", "Beijing", "Moscow", "Cairo", "Rio de Janeiro", "Buenos Aires", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Mexico City", "São Paulo", "Lima", "Bogotá", "Istanbul", "Mumbai", "Delhi", "Shanghai", "Seoul", "Hong Kong", "Bangkok", "Kuala Lumpur", "Singapore", "Jakarta", "Manila", "Ho Chi Minh City", "Hanoi", "Cape Town", "Johannesburg", "Lagos", "Nairobi", "Kinshasa", "Dar es Salaam", "Addis Ababa", "Kigali", "Accra", "Abidjan", "Casablanca", "Tunis", "Rabat", "Amman", "Tel Aviv", "Dubai", "Abu Dhabi", "Kuwait City", "Doha", "Riyadh", "Jeddah", "Muscat", "Manama", "Bahrain", "Kuwait", "Doha", "Riyadh", "Jeddah", "Muscat", "Manama", "Bahrain"]
API_KEY = "27e13e506b1c0f013a05c651617bc80c"
city = random.choice(cities)
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"

req = requests.get(link)
request_dic = req.json()
desc = request_dic['weather'][0]['description']
temp = request_dic['main']['temp'] - 273.15
print(f"Em {city} agora está: {desc}, e está fazendo {temp}ºC")