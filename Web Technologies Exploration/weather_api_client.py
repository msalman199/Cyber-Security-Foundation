#!/usr/bin/env python3
import requests
import json
from datetime import datetime

class WeatherAPIClient:
    def __init__(self):
        # Using a free API that doesn't require authentication
        self.base_url = "https://api.open-meteo.com/v1"
    
    def get_weather_data(self, latitude, longitude):
        """Get current weather data for given coordinates"""
        endpoint = f"{self.base_url}/forecast"
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current_weather': 'true',
            'hourly': 'temperature_2m,relative_humidity_2m',
            'timezone': 'auto'
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def display_weather_info(self, weather_data):
        """Display formatted weather information"""
        if not weather_data:
            print("No weather data available")
            return
        
        current = weather_data.get('current_weather', {})
        
        print("=== Current Weather Information ===")
        print(f"Temperature: {current.get('temperature', 'N/A')}°C")
        print(f"Wind Speed: {current.get('windspeed', 'N/A')} km/h")
        print(f"Wind Direction: {current.get('winddirection', 'N/A')}°")
        print(f"Weather Code: {current.get('weathercode', 'N/A')}")
        print(f"Time: {current.get('time', 'N/A')}")
        
        # Display timezone info
        timezone = weather_data.get('timezone', 'Unknown')
        print(f"Timezone: {timezone}")

def main():
    client = WeatherAPIClient()
    
    # Test with coordinates for New York City
    print("Fetching weather data for New York City...")
    latitude = 40.7128
    longitude = -74.0060
    
    weather_data = client.get_weather_data(latitude, longitude)
    client.display_weather_info(weather_data)
    
    print("\n" + "="*50)
    
    # Test with coordinates for London
    print("Fetching weather data for London...")
    latitude = 51.5074
    longitude = -0.1278
    
    weather_data = client.get_weather_data(latitude, longitude)
    client.display_weather_info(weather_data)

if __name__ == "__main__":
    main()
