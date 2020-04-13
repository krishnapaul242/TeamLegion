"""
The flask application package.
"""
import os 
from flask import Flask
import pymongo
import dns
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://krishna:ZNy5sDQvtDDdBWrf@team-legion-bn5kh.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

import TeamLegion.views
