import requests
import json
from config import keys

class APIExcepton(Exception):
    pass


class CriptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExcepton(f"Невозможно перевести одинаковые вылюты {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExcepton(f"Не удалось обработать валюту {quote}.")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExcepton(f"Не удалось обработать валюту {base}.")

        try:
            amount = float(amount)
        except ValueError:
            raise APIExcepton(f"Неудалось обработать количество {amount}.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]

        return total_base
