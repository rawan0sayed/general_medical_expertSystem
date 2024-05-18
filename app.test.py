import requests
import json

# BASE = "http://127.0.0.1:5000"
BASE = "https://general-eosin.vercel.app"

user_data = {
    "fever": 1,
    "cough": 0,
    "runny_nose": 0,
    "sore_throat": 1,
    "fatigue": 1,
    "body_aches": 0,
    "rash": 1,
    "itchiness": 1,
    "swollen_glands": 0,
    "vomiting": 0,
    "diarrhea": 1,
    "abdominal_pain": 0,
    "ear_pain": 0,
    "sneezing": 1,
    "itchy_eyes": 1,
    "frequent_urination": 1,
    "unexplained_weight_loss": 1,
    "dehydration": 1,
    "difficulty_breathing": 0,
    "difficulty_sleeping": 0,
    "blisters": 0,
    "excessive_thirst": 1,
    "nasal_congestion": 1,
    "headache": 0,
}

response = requests.post(
    url=BASE + "/api",
    headers={"Content-Type": "application/json"},
    data=json.dumps(user_data),
)

print( response.json() )
