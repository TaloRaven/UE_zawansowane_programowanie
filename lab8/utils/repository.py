import csv
import json
from json import JSONEncoder

from flask import Flask
from flask_restful import Resource, Api

from utils.utils import reader

class Movie():
    def __init__(self, id: int, title: str, genres: str):
        self.id = id
        self.title = title
        self.genres = genres


class Get(Resource):
    def get(self):
        rows = []
        csvfile = open('./data/movies.csv', 'r', encoding='utf-8')
        fieldnames = ("id", "title", "genres")
        reader = csv.DictReader(csvfile, fieldnames)

        for row in reader:
            json_row = list(row.values())
            rows.append(Movie(json_row[0], json_row[1], json_row[2]).__dict__)
        return rows