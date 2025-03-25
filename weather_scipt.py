import requests

# Configuración
API_KEY = "93139bb9170001d69380abeb7995df03"  # Reemplaza con tu API Key de OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5"

class WeatherService:
    @staticmethod
    def get_weather_by_city(city):
        url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def get_weather_by_coordinates(lat, lon):
        url = f"{BASE_URL}/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Ejemplo de uso
if __name__ == "__main__":
    city = input("Ingresa el nombre de la ciudad: ")
    try:
        weather_data = WeatherService.get_weather_by_city(city)
        print("Datos meteorológicos:")
        print(weather_data)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")