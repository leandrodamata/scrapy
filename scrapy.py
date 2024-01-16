import requests

number = "1003500430051U"

url = f"https://www.vans.com.br/arezzocoocc/v2/vans/products/{number}/dynamic-product-fields?fields=DYNAMIC_FIELDS_PDP"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

data = requests.get(url, headers=headers).json()

for c in data["colorOptions"]:
    if c["code"] == number:
        print(c["name"], data["price"]["value"])
        break