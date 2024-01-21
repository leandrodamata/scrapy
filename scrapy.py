## vlgi pivi kkus kpdo
## vlgipivikkuskpdo

import requests
import smtplib
import email.message
import ssl

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}
def get_product_data(url, number):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return next((c for c in data.get("colorOptions", []) if c["code"] == number), None)
    except requests.RequestException as e:
        print(f"Error fetching product data for {number}: {e}")
        return None

def send_email(product_name, product_price, receiver_email):
    subject = "Price Drop Alert!"
    body_msg = f'''The price of {product_name} has dropped to {product_price}.'''
    message = f"Subject: {subject}\n\n{body_msg}"

    sender = 'pythonscrapydamata@gmail.com'
    password = 'vlgipivikkuskpdo'
    receiver = 'vini.damatta17@gmail.com'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)

        server.sendmail(sender, receiver, message.encode('utf-8'))

number1 = "1003500430051U"
number2 = "1002001070011U"

url1 = f"https://www.vans.com.br/arezzocoocc/v2/vans/products/{number1}/dynamic-product-fields?fields=DYNAMIC_FIELDS_PDP"
url2 = f"https://www.vans.com.br/arezzocoocc/v2/vans/products/{number2}/dynamic-product-fields?fields=DYNAMIC_FIELDS_PDP"

product1 = get_product_data(url1, number1)
product2 = get_product_data(url2, number2)

if product1 and "price" in product1:
    productprice1 = product1["price"]["value"]
    print(product1["name"], productprice1)

if product2 and "price" in product2:
    print(product2["name"], product2["price"]["value"])

try:
    data1 = requests.get(url1, headers=headers).json()
    data2 = requests.get(url2, headers=headers).json()
except requests.RequestException as e:
    print(f"Error fetching product data: {e}")

for c in data1["colorOptions"]:
    if c["code"] == number1:
        productprice1 = data1["price"]["value"]
        print(c["name"], productprice1)
        break

for c in data2["colorOptions"]:
    if c["code"] == number2:
        print(c["name"], data2["price"]["value"])
        break

if productprice1 and productprice1 < 600:
    send_email(product1["name"], productprice1, 'vini.damatta17@gmail.com')