# services/services.py

import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://v6.exchangerate-api.com/v6/f6e9d49461055b64ddbf1f7d/'

    def get_exchange_rate(self, from_currency, to_currency):
        url = f'{self.base_url}latest/{from_currency}'
        params = {'api_key': self.api_key, 'base': from_currency}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data['conversion_rates'].get(to_currency)
        else:
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        exchange_rate = self.get_exchange_rate(from_currency, to_currency)
        if exchange_rate is not None:
            converted_amount = float(amount) * float(exchange_rate)
            return converted_amount
        return None

