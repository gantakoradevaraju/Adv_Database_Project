
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template

import sqlite3

connection = sqlite3.connect("shopping_list.db")

@route('/')
def hello_world():
    return 'Hello from Devaraju! Welcome'

@route('/hi')
def hi_world():
    return 'Hi from Deva Raju!'

@route('/bye')
def bye_world():
    return 'Bye from Deva Raju!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id':row[0] ,'description':row[1]} for row in rows ]
    return template("shopping_list.tpl", name="DevaRaju", shopping_list=rows)


application = default_app()

