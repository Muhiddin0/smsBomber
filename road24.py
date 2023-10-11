
import time
import requests
import json


class Road24:

    def __init__(self) -> None:
        self.authorization = 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3NTYxMjczLCJpYXQiOjE2OTY5NTY0NzMsImp0aSI6IjlmOGQ1ODg2MjgyODQwYWY4NTNjMGIxOWJjNmFjMjdiIiwidXNlcl9pZCI6MjUxNzA5M30.u8J_X6ucPX6MY5N246mtIMCHmM4VcB7HcONejK6JVDc'
        self.header = {
            "accept": "application/json",
            "accept-encoding": "gzip",
            "accept-language": "uz",
            "api-version": "1.0",
            "app-os": "Android",
            "content-type": "application/json",
            "host": "api.road24.uz",
            "user-agent": "Dart/3.0 (dart:io)"
        }

    def send_sms(self):
        self.header['authorization'] = self.authorization
        r = requests.post(
            url="https://api.road24.uz/api/mobile/v2/users/auth/phone/",
            headers=self.header,
            data=json.dumps({
                "phone": "998905650213"
            })
        )

        print(r.content)
        print(r)

        return r

    def verifay_sms(self):
        r = requests.post(
            url="https://api.road24.uz/api/mobile/v1/users/auth/phone_verify/",
            headers=self.header,
            data=json.dumps({
                "phone": "998905650213",
                "sms_code": "526685"
            })
        )

        print(r.content)
        print(r)

        return r

    def register_car(self):
        self.header['authorization'] = self.authorization
        r = requests.post(
            url="https://api.road24.uz/api/mobile/v1/cars/",
            headers=self.header,
            data=json.dumps({
                "number": "40V604DA",
                "tech_pass_num": "3225001",
                "tech_pass_series": "AAF",
                "mark": "Chevrolet",
                "name": "Nexia 2",
                "car_brand": 12,
                "car_model": 128,
                "image": None
            })
        )

        print(r.content)
        print(r)

        return r

    # def fine(self):
        # r = requests.

while True:
    Road24().send_sms()