import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=20)


@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/d5418905a087fe4b6f85408c/latest/{base_currency}"
    response = requests.get(url)
    result =response.json()['conversion_rates'][target_currency]

    return float(result)

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


if __name__ == "__main__":
    base_currency = input("Enter the base currency:").upper()
    target_currency = input("Enter the target currency:").upper()
    amount = int(input("How much will you convert?"))
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    result = convert_currency(amount, exchange_rate)
    print(f"The exchanged value is : {result:.2f}")
