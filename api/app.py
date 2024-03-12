from args import arguments
from engine import ExpertSystem

import flask
from flask_restful import Api, Resource, reqparse

app = flask.Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def home():
    return flask.render_template('index.html')

class Model(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        for arg in arguments:
            self.parser.add_argument(arg, type=bool, help=f"{arg} value is required", required=False, default=False)
            
    def post(self):
        patient_data = self.parser.parse_args()

        engine = ExpertSystem(patient_data)
        result = engine.run()
        return result


api.add_resource(Model, '/api')


if __name__ == '__main__':
    app.run(debug=True)