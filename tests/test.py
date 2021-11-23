import csv
import json
from json import JSONEncoder

from flask import Flask
from flask_restful import Resource, Api



def read(csv_name: str):
    csvfile = open('./data/{}.csv'.format(csv_name), 'r', encoding='utf-8')
    for i in csvfile:
        filename=i.strip()
        break
    filenames=filename.split(',')
    reader = csv.DictReader(csvfile, filenames)
    return reader



