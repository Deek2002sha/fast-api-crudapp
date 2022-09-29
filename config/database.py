#import statement
from pymongo import MongoClient

#create bd connection
connection = MongoClient("mongodb://localhost:27017/test")
