import csv

from flask import Flask
from flask_restful import Resource, Api

from utils.repository import Get
from utils.utils import reader



app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def main(self):
        return Get.get()

        
api.add_resource(Get, '/')

if __name__ == '__main__':
    app.run(debug=True)