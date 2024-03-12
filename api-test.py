import requests
import json

# BASE = "https://medical-es.vercel.app"
BASE = "http://127.0.0.1:5000"

user_data = {
    "fever": True,
    "cough": True,
    "runny_nose": True,
    "sore_throat": True,
    "fatigue": True,
    "body_aches": True,
    "rash": True,
    "itchiness": True,
    "swollen_glands": True,
    "vomiting": True,
    "diarrhea": True,
    "abdominal_pain": True,
    "wheezing": True,
    "difficulty_breathing": True,
    "ear_pain": True,
    "difficulty_sleeping": True,
    "sneezing": True,
    "itchy_eyes": True,
    "high_fever": True,
    "blisters": True,
    "excessive_thirst": True,
    "frequent_urination": True,
    "unexplained_weight_loss": True,
    "facial_pain": True,
    "headache": True,
    "nasal_congestion": True,
    "dehydration": True
}

response = requests.post(
    url=BASE + "/api",
    headers={
        # "api-key": "my-api-key",
        "Content-Type": "application/json"
    },
    data=json.dumps(user_data),
)

print( response.json() )

# curl -X POST http://127.0.0.1:5000/api -H 'Content-Type: application/json' -d '{"name": "hello", "age": 22}'
# curl -X POST https://medicales.vercel.app/api -H 'Content-Type: application/json' -d '{"name": "hello", "age": 22}'
# curl -X POST https://medical-es.vercel.app/api -H 'Content-Type: application/json' -d '{"name": "hello", "age": 22}'