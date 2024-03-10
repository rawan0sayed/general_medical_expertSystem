from flask import Flask
from flask_restful import Api, Resource, reqparse
import packages
from expert_system import ExpertSystem
from controller import Controller

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
        newCont = Controller()
        newCont.preprocess()
        engine = ExpertSystem(newCont.symptom_map, newCont.if_not_matched, newCont.get_treatments, newCont.get_details)
        
        engine.reset()
        engine.run()

        args = model_args.parse_args()
        return {'name': args['name']}
    
api.add_resource(Model, '/model')

if __name__ == '__main__':
    app.run(debug=True)