# Request example using Requests module to communicate with an external
# service; in this case will be a complete request to Exchangeratesapi's
# APIs.

import requests


def main():
    '''
    The user must provide the base and second currency (e.g. EUR, USD, ...)
    and the application will return the exchange rate and the date of those
    values.
    '''
    base_currency = input("\nInsert the base currency: ").upper()
    symbol_currency = input("Insert the second currency: ").upper()

    # Payload creation and requests to the external API
    payload = {'base': base_currency, 'symbols': symbol_currency}
    response = requests.get("https://api.exchangeratesapi.io/latest",
                            params=payload)

    # Response check and retrieving the request data, if the status
    # code of the response is 200 (STATUS_OK)
    if response.status_code != 200:
        raise Exception("Error request! Base or second "
                        "currency doesen't exist! Try again!")
    data = response.json()
    quotation = data['rates'][symbol_currency]

    # Print of the results
    print("\nDate: ", data['date'])
    print(f'1 {base_currency} => {quotation} {symbol_currency}')


if __name__ == "__main__":
    main()
