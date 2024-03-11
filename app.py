import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
# import packages
# from expert_system import ExpertSystem
# from controller import Controller

app = Flask(__name__)
api = Api(app)

# model_args.add_argument("headache", type=bool, help="headache value is required", required=True)
# model_args.add_argument("back_pain", type=bool, help="back_pain value is required", required=True)
# model_args.add_argument("chest_pain", type=bool, help="chest_pain value is required", required=True)
# model_args.add_argument("cough", type=bool, help="cough value is required", required=True)
# model_args.add_argument("fainting", type=bool, help="fainting value is required", required=True)
# model_args.add_argument("sore_throat", type=bool, help="sore_throat value is required", required=True)
# model_args.add_argument("fatigue", type=bool, help="fatigue value is required", required=True)
# model_args.add_argument("restlessness", type=bool, help="restlessness value is required", required=True)
# model_args.add_argument("low_body_temp", type=bool, help="low_body_temp value is required", required=True)
# model_args.add_argument("fever", type=bool, help="fever value is required", required=True)
# model_args.add_argument("sunken_eyes", type=bool, help="sunken_eyes value is required", required=True)
# model_args.add_argument("nausea", type=bool, help="nausea value is required", required=True)
# model_args.add_argument("blurred_vision", type=bool, help="blurred_vision value is required", required=True)

# def get(self):
    # return 'Hello World', 200
    # newCont = Controller()
    # newCont.preprocess()
    # engine = ExpertSystem(newCont.symptom_map, newCont.if_not_matched, newCont.get_treatments, newCont.get_details)
    # engine.reset()
    # engine.run()
    # if self.matched(raw_data):
    #     return {'response_status': 'Matched'}
    #     return json.dumps({'response_status': 'Matched'})
    # else:
    #     return {'response_status': 'Not Matched'}
    #     return json.dumps({'response_status': 'Not Matched'})
# def matched(self, raw_data):
#     for key in raw_data:
#         if raw_data[key] != self.base_data[key]:
#             return False
#     return True

base_data = {
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


class Model(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, help="name value is required", required=True)
        parser.add_argument("age", type=int, help="age value is required", required=True)
        data = parser.parse_args()
        return data, 201


api.add_resource(Model, '/api')

if __name__ == '__main__':
    app.run(debug=True)