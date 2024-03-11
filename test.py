import requests

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

BASE = "http://127.0.0.1:5000/"

def test():
    return requests.POST(BASE + '/api', data)

if __name__ == "__main__":
    print("Getting response from server...\n", test())
    print("Everything passed")
