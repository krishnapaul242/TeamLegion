"""
The flask application package.
"""
import os 
from flask import Flask
import pymongo
import dns
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client.test

import TeamLegion.views
