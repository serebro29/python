import requests
from colorama import init, Fore, Style

init(autoreset=True)

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

currency_symbols = {
    "UAH": "₴",
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "PLN": "zł",
    "RUB": "₽",
    "JPY": "¥",
    "CHF": "₣",
}

def get_symbol(code):
    return currency_symbols.get(code, code)

def get_rates():
    response = requests.get(URL)
    data = response.json()
    rates = {"UAH": 1.0}
    for item in data:
        rates[item["cc"]] = item["rate"]
    return rates

def main():
    rates = get_rates()

    print(Style.BRIGHT + Fore.CYAN + "Конвертер валют (НБУ)")
    print(Fore.YELLOW + "Доступні валюти:")
    print(Style.BRIGHT + ", ".join(sorted(rates.keys())))

    while True:
        from_currency = input("\nЗ якої валюти: ").upper()
        to_currency = input("В яку валюту: ").upper()
        if from_currency not in rates or to_currency not in rates:
            print(Fore.RED + "Невірна валюта")
            continue
        try:
            amount = float(input("Сума: "))
        except ValueError:
            print(Fore.RED + "Введіть число")
            continue

        amount_uah = amount * rates[from_currency]
        result = amount_uah / rates[to_currency]

        from_symbol = get_symbol(from_currency)
        to_symbol = get_symbol(to_currency)

        print(
            Style.BRIGHT +
            Fore.GREEN +
            f"{amount:.2f} {from_symbol} → {result:.2f} {to_symbol}"
        )

main()