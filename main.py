import csv

from flask import Flask
from flask_restful import Resource, Api

from utils.repository import Get_links, Get_movies, Get_ratings, Get_tags


app = Flask(__name__)
api = Api(app)


class Main(Resource):
    def get(self):
        return f'python/movies, /tags, /links, /ratings'


api.add_resource(Main, '/')
api.add_resource(Get_movies, '/movies')
api.add_resource(Get_tags, '/tags')
api.add_resource(Get_links, '/links')
api.add_resource(Get_ratings, '/ratings')


if __name__ == '__main__':
    app.run(debug=True)
