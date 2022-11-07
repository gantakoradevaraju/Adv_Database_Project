# database.py - functions for managing database

from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse
import json

with open("C:/Users/devar/Desktop/Kent/mongo_pass.json", "r") as f:
    private = json.load(f)

password = private["devaraju"]

username = urllib.parse.quote_plus('devaraju')
password = urllib.parse.quote_plus(f'{password}')
# client = MongoClient(
#     'mongodb+srv://%s:%s@mydatabase.kdw9m7f.mongodb.net/?retryWrites=true&w=majority' % (username, password))

client = MongoClient(f"mongodb+srv://devaraju:{password}@drcluster.lurt0md.mongodb.net/?retryWrites=true&w=majority")
db = client.test
shopping_db = client.shopping_db
list_collection = shopping_db.list_collection


def get_items(id=None):
    if id is None:
        items = list_collection.find({})
    else:
        items = list_collection.find({'_id': ObjectId(id)})
    items = [{'id': str(item['_id']), 'description': item['description']} for item in items]
    return items


def add_item(description):
    list_collection.insert_one({'description': description})


def delete_item(id):
    list_collection.delete_one({'_id': ObjectId(id)})


def update_item(id, description):
    list_collection.update_one({'_id': ObjectId(id)}, {'$set': {'description': description}})
