# services/services.py

import requests

class SafetyService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_safety_information(self, country_code=None):
        if country_code:
            url = f'{self.base_url}?countrycode={country_code}/'
        else:
            url = f'{self.base_url}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None


