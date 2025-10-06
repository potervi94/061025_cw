# -*- coding: utf-8 -*-

# який спілкується з сервером

import requests

# виклик функції message на сервері
response = requests.post("http://localhost:8001/message")
print(response.status_code)

# виклик функції func на сервері
requests.post("http://localhost:8001/function")

# response2 = requests.post("http://localhost:8001/data")
# requests.post("http://localhost:8001/data")

response3 = requests.post("http://localhost:8001/mult2/5")
print(str(response3.content))