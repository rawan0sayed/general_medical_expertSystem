import requests

BASE = "http://127.0.0.1:5000"

data = {
    "headache": True,
    "back_pain": True,
    "chest_pain": False,
    "cough": True,
    "fainting": True,
    "sore_throat": False,
    "fatigue": False,
    "restlessness": True,
    "low_body_temp": False,
    "fever": True,
    "sunken_eyes": False,
    "nausea": False,
    "blurred_vision": True
}

data = {
    "name": "Ismail",
    "age": 22
}

response = requests.get(BASE + "/api", data=data)

print( response.json() )