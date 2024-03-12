from flask import Flask
from flask_restful import Api, Resource, reqparse

# import packages
# from expert_system import ExpertSystem
# from controller import Controller

# newCont = Controller()
# newCont.preprocess()
# engine = ExpertSystem(newCont.symptom_map, newCont.if_not_matched, newCont.get_treatments, newCont.get_details)
# engine.reset()
# engine.run()

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def get():
    Flask.render_template('index.html')

class Model(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("headache", type=bool, help="headache value is required", required=True, default=False)
        self.parser.add_argument("back_pain", type=bool, help="back_pain value is required", required=True, default=False)
        self.parser.add_argument("chest_pain", type=bool, help="chest_pain value is required", required=True, default=False)
        self.parser.add_argument("cough", type=bool, help="cough value is required", required=True, default=False)
        self.parser.add_argument("fainting", type=bool, help="fainting value is required", required=True, default=False)
        self.parser.add_argument("sore_throat", type=bool, help="sore_throat value is required", required=True, default=False)
        self.parser.add_argument("fatigue", type=bool, help="fatigue value is required", required=True, default=False)
        self.parser.add_argument("restlessness", type=bool, help="restlessness value is required", required=True, default=False)
        self.parser.add_argument("low_body_temp", type=bool, help="low_body_temp value is required", required=True, default=False)
        self.parser.add_argument("fever", type=bool, help="fever value is required", required=True, default=False)
        self.parser.add_argument("sunken_eyes", type=bool, help="sunken_eyes value is required", required=True, default=False)
        self.parser.add_argument("nausea", type=bool, help="nausea value is required", required=True, default=False)
        self.parser.add_argument("blurred_vision", type=bool, help="blurred_vision value is required", required=True, default=False)

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
        data = self.parser.parse_args()

        if self.matched(data):
            return {'response_status': 'Matched'}, 200
        else:
            return {'response_status': 'Not Matched'}, 201


api.add_resource(Model, '/api')

if __name__ == '__main__':
    app.run(debug=False)