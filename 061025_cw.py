# -*- coding: utf-8 -*-


# https://www.google.com/search?q=java

from fastapi import FastAPI
from fastapi.responses import JSONResponse

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


@app.post("/message")
def message_endpoint():
    message()
    return JSONResponse({"status": "ok", "action": "message"})


@app.post("/function")
def function_endpoint():
    func()
    return JSONResponse({"status": "ok", "action": "function"})


@app.post("/data")
def get_data():
    return JSONResponse({"status": "ok", "action": "data"})


@app.post("/mult2/{num}")
def mult2(num: int):
    return JSONResponse({"status": "ok", "action": "mult2","param":num,  "result":2*num})