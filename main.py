import csv
import json
from json import JSONEncoder

from flask import Flask
from flask_restful import Resource, Api

#from utils.utils import MovieEncoder, Movie

app = Flask(__name__)
api = Api(app)


class Movie():
    def __init__(self,id: int, title: str, genres: str)-> str:
        self.id=id
        self.title=title
        self.genres=genres
    
class MovieEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class Get(Resource):
    
    def get(self):
        csvfile = open('data\movies.csv', 'r', encoding='utf-8')
        fieldnames = ("id","title","genres")
        reader = csv.DictReader( csvfile, fieldnames)
        rows=[]
        for row in reader:
            #json_row=list(row.values())
            #MovieEncoder().encode(Movie(json_row[0],json_row[1],json_row[2])
            #rows.append(MovieEncoder().encode(Movie(json_row[0],json_row[1],json_row[2])))
            # Tak naprawde daje taki output jak ma być ale nie używa __dict__ ani klasy Movie
            rows.append(row)
        return rows
        
api.add_resource(Get, '/')

if __name__ == '__main__':
    app.run(debug=True)