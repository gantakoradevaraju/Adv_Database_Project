
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, get, post, template, request, redirect

'''import sqlite3
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
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return template("shopping_list.tpl", name="DevaRaju", shopping_list=rows)

@get('/add')
def get_add():
    return template("add_item.tpl")

@post('/add')
def post_add():
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"insert into list (description) values ('{description}')")
    connection.commit()
    redirect('/list')

@route("/delete/<id>")
def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()
    redirect('/list')

@get("/edit/<id>")
def get_edit(id):
    cursor = connection.cursor()
    items = cursor.execute(f"select description from list where id={id}")
    items = list(items)
    if len(items) != 1:
        redirect('/list')
    description = items[0][0]
    return template("edit_item.tpl", id=id, description=description)

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"update list set description='{description}' where id={id}")
    connection.commit()
    redirect('/list')'''

import database

@route('/')
def get_index():
    redirect('/list')

@route('/list')
def get_list():
    items = database.get_items()
    return template("shopping_list.tpl", name="DevaRaju", shopping_list=items)

@post('/add')
def post_add():
    description = request.forms.get("description")
    database.add_item(description)
    redirect('/list')

@route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect('/list')

@get("/edit/<id>")
def get_edit(id):
    items = database.get_items(id)
    if len(items) != 1:
        redirect('/list')
    item_id, description = items[0]['id'], items[0]['desc']
    assert item_id == int(id)
    return template("edit_item.tpl", id=id, description=description)

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    database.update_item(id, description)
    redirect('/list')

application = default_app()

