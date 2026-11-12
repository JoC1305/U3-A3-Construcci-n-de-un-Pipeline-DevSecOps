import os

import requests

def fetch_data(url):
    # Vulnerabilidad SAST: Uso de credenciales hardcodeadas
    api_key = os.environ.get("API_KEY")
    response = requests.get(f"{url}?key={api_key}")
    return response.json()
#Cambio para probar el workflow de Actions