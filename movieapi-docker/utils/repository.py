import csv
import json
from json import JSONEncoder

from flask import Flask
from flask_restful import Resource, Api

from utils.utils import read


class Movie():
    def __init__(self, id: int, title: str, genres: str):
        self.id = id
        self.title = title
        self.genres = genres


class Links():
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbIb = imdbId
        self.tmdbId = tmdbId


class Ratings():
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tags():
    def __init__(self, userId, movieId, tag, timestamp):
        self.useId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


class Get_movies(Resource):
    def get(self):
        rows = []
        for row in read('movies'):
            json_row = list(row.values())
            rows.append(Movie(json_row[0], json_row[1], json_row[2]).__dict__)
        return rows


class Get_tags(Resource):
    def get(self):
        rows = []
        for row in read('tags'):
            json_row = list(row.values())
            rows.append(
                Tags(
                    json_row[0],
                    json_row[1],
                    json_row[2],
                    json_row[3]).__dict__)
        return rows


class Get_ratings(Resource):
    def get(self):
        rows = []
        for row in read('ratings'):
            json_row = list(row.values())
            rows.append(
                Ratings(
                    json_row[0],
                    json_row[1],
                    json_row[2],
                    json_row[3]).__dict__)
        return rows


class Get_links(Resource):
    def get(self):
        rows = []
        for row in read('links'):
            json_row = list(row.values())
            rows.append(Links(json_row[0], json_row[1], json_row[2]).__dict__)
        return rows
