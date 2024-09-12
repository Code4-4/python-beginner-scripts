# weather_api.py
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    get_weather(key, city)
