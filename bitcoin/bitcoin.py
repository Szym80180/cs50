from sys import argv, exit
import requests

try:
    n = float(argv[1])
except ValueError:
    print("Not a number")
    exit(1pytest)
try:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("request failed")
    exit()
request = request.json()
r=request["bpi"]["USD"]["rate_float"]
fullprice=r*n
print(f"${fullprice:,.4f}")
