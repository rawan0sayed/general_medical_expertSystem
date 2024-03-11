import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
# import packages
# from expert_system import ExpertSystem
# from controller import Controller

app = Flask(__name__)
api = Api(app)

model_args = reqparse.RequestParser()
model_args.add_argument("headache", type=str, help="headache value is required", required=True)
model_args.add_argument("back_pain", type=str, help="back_pain value is required", required=True)
model_args.add_argument("chest_pain", type=str, help="chest_pain value is required", required=True)
model_args.add_argument("cough", type=str, help="cough value is required", required=True)
model_args.add_argument("fainting", type=str, help="fainting value is required", required=True)
model_args.add_argument("sore_throat", type=str, help="sore_throat value is required", required=True)
model_args.add_argument("fatigue", type=str, help="fatigue value is required", required=True)
model_args.add_argument("restlessness", type=str, help="restlessness value is required", required=True)
model_args.add_argument("low_body_temp", type=str, help="low_body_temp value is required", required=True)
model_args.add_argument("fever", type=str, help="fever value is required", required=True)
model_args.add_argument("sunken_eyes", type=str, help="sunken_eyes value is required", required=True)
model_args.add_argument("nausea", type=str, help="nausea value is required", required=True)
model_args.add_argument("blurred_vision", type=str, help="blurred_vision value is required", required=True)

class Model(Resource):
    def __init__(self):
        self.base_data = {
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

    def matched(self, raw_data):
        for key in raw_data:
            if raw_data[key] != self.base_data[key]:
                return False
        return True

    def post(self):
        # newCont = Controller()
        # newCont.preprocess()
        # engine = ExpertSystem(newCont.symptom_map, newCont.if_not_matched, newCont.get_treatments, newCont.get_details)
        # engine.reset()
        # engine.run()

        raw_data = model_args.parse_args()
        
        if self.matched(raw_data):
            return json.dumps({'response_status': 'Matched'})
        else:
            return json.dumps({'response_status': 'Not Matched'})
    
api.add_resource(Model, '/api')

if __name__ == '__main__':
    app.run(debug=True)