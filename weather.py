import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError:
        print("Error: Unable to parse JSON response")
        print("Response content:", response.text)
    return None

def display_weather(data):
    if data is None:
        print("Error: No data received.")
        return
    if data.get('cod') != 200:
        print("Error fetching weather data:", data.get('message', 'Unknown error'))
        return

    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['description']

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
   

def main():
    api_key = "Your_own_api" 
    location = input("Enter a city name or ZIP code: ")

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
