import csv
import json
from json import JSONEncoder

from flask import Flask
from flask_restful import Resource, Api



csvfile = open('./data/movies.csv', 'r', encoding='utf-8')
fieldnames = ("id", "title", "genres")
reader = csv.DictReader(csvfile, fieldnames)
