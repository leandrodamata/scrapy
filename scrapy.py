import requests
import smtplib
import email.message

number1 = "1003500430051U"
number2 = "1002001070011U"

url1 = f"https://www.vans.com.br/arezzocoocc/v2/vans/products/{number1}/dynamic-product-fields?fields=DYNAMIC_FIELDS_PDP"
url2 = f"https://www.vans.com.br/arezzocoocc/v2/vans/products/{number2}/dynamic-product-fields?fields=DYNAMIC_FIELDS_PDP"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

data1 = requests.get(url1, headers=headers).json()
data2 = requests.get(url2, headers=headers).json()

for c in data1["colorOptions"]:
    if c["code"] == number1:
        productprice1 = data1["price"]["value"]
        print(c["name"], productprice1)
        break

for c in data2["colorOptions"]:
    if c["code"] == number2:
        print(c["name"], data2["price"]["value"])
        break


def send_email():
    email_content = """"https://www.vans.com.br/arezzocoocc/v2/vans/products/{number1}/dynamic-product-fields?fields=DYNAMIC_FIELDS_PDP"""
    msg = ()
    msg['Subject'] = 'Preco do Ultra Range Baixou!!'

    msg['From'] = 'matinhabey1@gmail.com'
    msg['To'] = 'matinhabey1@gmail.com'
    password = 'Scrapteste1!'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

    print("Success")



if (productprice1 < 600):
    send_email()