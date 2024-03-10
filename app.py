from flask import Flask
from flask_restful import Api, Resource, reqparse
import main

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
    def post(self):
        preprocess()
        engine = ExpertSystem(symptom_map, if_not_matched, get_treatments, get_details)
        # loop to keep running the code until user says no when asked for another diagnosis
        
        while 1:
            engine.reset()
            engine.run()
            print("Would you like to diagnose some other symptoms?\n Reply yes or no")
            if input() == "no":
                exit()

        args = model_args.parse_args()
        return {'name': args['name']}
    
api.add_resource(Model, '/model')

"""
request: symptoms = { {} }
response: {
    "name": "disease",
    "description": "asdfasdfA",
    "treatment": "asdfasdfasdFASDF"
}
"""

if __name__ == '__main__':
    app.run(debug=True)