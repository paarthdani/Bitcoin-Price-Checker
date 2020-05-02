import requests
import json

CURRENCIES = ["USD", "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "DKK", "EUR", "GBP", "HKD", "INR", "ISK", "JPY", "KRW", "NZD", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD"]


# this function will fetch the Bitcoin price for all currency code.
def get_price():
    req = requests.get("https://blockchain.info/ticker")
    x = json.loads(req.text)
    req.close()
    return x


# this function will convert amount of particular currency to Bitcoin.
def get_currency_value(currency, value):
    url = "https://blockchain.info/tobtc?currency=" + currency + "&value=" + str(value)
    req = requests.get(url)
    return req.text


if __name__ == '__main__':
    print("\n               Bitcoin Price Checker\n")
    print("Enter 1 - to fetch the Bitcoin price for particular currency code.")
    print("Enter 2 - to convert amount of particular currency to Bitcoin.")
    option = int(input("Select 1 or 2: "))
    bitcoin_conversion = ""
    if option == 1:
        while True:
            currency_code = input("Enter Currency Code for equivalent bitcoin price: ")
            if currency_code.upper() not in CURRENCIES:
                print("Please select the currency code from below codes: \n", [x for x in CURRENCIES])
            else:
                break
        bitcoin_conversion = "1 Bitcoin is " + str(get_price()[currency_code.upper()]["symbol"]) + " " + str(get_price()[currency_code.upper()]["last"])
    elif option == 2:
        while True:
            currency_code = input("Enter the currency code: ")
            if currency_code.upper() not in CURRENCIES:
                print("Please select the currency code from below codes: \n", [x for x in CURRENCIES])
            else:
                break
        amount = int(input("Enter Amount: "))
        bitcoin_conversion = str(get_price()[currency_code.upper()]["symbol"]) + " " + str(amount) + " is " + get_currency_value(currency_code.upper(), amount) + " Bitcoin"
    else:
        print("Please try again.")

    print(bitcoin_conversion)
