import requests
import json

# BASE = "https://medical-es.vercel.app"
# BASE = "http://127.0.0.1:5000"
BASE = "https://medical-es-api.vercel.app"

user_data = {
    "fever": True,
    "cough": True,
    "runny_nose": True,
    "sore_throat": False,
    "fatigue": True,
    "body_aches": True,
    "rash": True,
    "itchiness": True,
    "swollen_glands": False,
    "vomiting": False,
    "diarrhea": True,
    "abdominal_pain": True,
    "wheezing": True,
    "difficulty_breathing": True,
    "ear_pain": False,
    "difficulty_sleeping": True,
    "sneezing": True,
    "itchy_eyes": False,
    "high_fever": False,
    "blisters": True,
    "excessive_thirst": True,
    "frequent_urination": True,
    "unexplained_weight_loss": True,
    "facial_pain": False,
    "headache": True,
    "nasal_congestion": True,
    "dehydration": False
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
print( type(response.json()) )

# curl -X POST http://127.0.0.1:5000/api -H 'Content-Type: application/json' -d '{"name": "hello", "age": 22}'
# curl -X POST https://medicales.vercel.app/api -H 'Content-Type: application/json' -d '{"name": "hello", "age": 22}'
# curl -X POST https://medical-es-api.vercel.app/api -H 'Content-Type: application/json' -d '{ "fever": 1, "cough": 1, "runny_nose": 1, "sore_throat": 0, "fatigue": 1, "body_aches": 1, "rash": 1, "itchiness": 1, "swollen_glands": 0, "vomiting": 0, "diarrhea": 1, "abdominal_pain": 1, "wheezing": 1, "difficulty_breathing": 1, "ear_pain": 0, "difficulty_sleeping": 1, "sneezing": 1, "itchy_eyes": 0, "high_fever": 0, "blisters": 1, "excessive_thirst": 1, "frequent_urination": 1, "unexplained_weight_loss": 1, "facial_pain": 0, "headache": 1, "nasal_congestion": 1, "dehydration": 0 }'