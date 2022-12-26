import requests
import sys
import json

try:
    if len(sys.argv) == 2:
        amount = float(sys.argv[1])

        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            rate = response.json()['bpi']['USD']['rate_float']
            total = float(rate) * amount
            print('$', end='')
            print(f'{total:,}')

        except requests.RequestException:
            print('ERROR')
            sys.exit()
    else:
        sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')