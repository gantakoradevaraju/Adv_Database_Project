# from pymongo import MongoClient
# import urllib

from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('devaraju')
password = urllib.parse.quote_plus('Raju@0424')
client = MongoClient('mongodb+srv://%s:%s@mydatabase.kdw9m7f.mongodb.net/?retryWrites=true&w=majority' % (username, password))
# import json
# with open("/home/devarajug/mongo_pass.json","r") as f:
#     private = json.load(f)

# password = private["devaraju"]

# client = MongoClient("mongodb+srv://devaraju:<Raju@0424>@drcluster.lurt0md.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# mongo_uri = "mongodb://devaraju:" + urllib.parse.quote("Raju@0424") + "@drcluster.lurt0md.mongodb.net/"
# client = MongoClient(mongo_uri)
# db = client.test

from bson.objectid import ObjectId

shopping_db = client.shopping_db
list_collection = shopping_db.list_collection

list_collection.delete_many({})

list_collection.insert_many([
        { "description": 'apples' },
        { "description": 'guava' },
        { "description": 'bananas' },
        { "description": 'grapes' },
        { "description": 'onioins' },
        { "description": 'Tomato' }
    ])

items = list_collection.find()
print(items)
# from peewee import SqliteDatabase, Model, CharField

# db = SqliteDatabase('peewee_shopping_list.db')

# class Item(Model):
#     description = CharField()

#     class Meta:
#         database = db

# def add_items_to_db():
#     global db
#     items = [
#         { "description": 'apples' },
#         { "description": 'guava' },
#         { "description": 'bananas' },
#         { "description": 'grapes' },
#         { "description": 'onioins' },
#         { "description": 'Tomato' }
#         ]
#     for item in items:
#         Item.create(description=item['description'])

# if __name__ == "__main__":
#     db.connect()
#     db.create_tables([Item])
#     add_items_to_db()
