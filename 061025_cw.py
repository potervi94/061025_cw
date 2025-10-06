# -*- coding: utf-8 -*-


# https://www.google.com/search?q=java

from fastapi import FastAPI

# застосунок для сервера
# допомагає позначити як отримати доступ до окремих функцій на сервері

# коли робитиметься виклик до сервера
# http:our_ip\шлях до функції
app = FastAPI()

# створення функцій
def message():  # new*
    print("виклик функції message")

def func():  # new*
    print("виклик функції func")