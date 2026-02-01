import requests

class CurrencyConverter:
    def __init__(self, usd_rate):
        self.usd_rate = usd_rate  # гривень за 1 USD

    def uah_to_usd(self, uah):
        return uah / self.usd_rate

def get_usd_rate_from_nbu():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    response = requests.get(url)
    data = response.json()
    return data[0]["rate"]

def main():
    usd_rate = get_usd_rate_from_nbu()
    print(f"Курс НБУ: 1 USD = {usd_rate} UAH")

    converter = CurrencyConverter(usd_rate)

    while True:
        try:
            uah = float(input("Введіть суму в гривнях: "))
            usd = converter.uah_to_usd(uah)
            print(f"{uah:.2f} UAH = {usd:.2f} USD\n")
        except ValueError:
            print("Потрібно ввести число!\n")

if __name__ == "__main__":
    main()