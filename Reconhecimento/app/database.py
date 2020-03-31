from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.fatec
