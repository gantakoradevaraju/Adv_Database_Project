import dataset

db = dataset.connect("sqlite:///shopping_list.db")

def get_items(id=None):
    table = db['list']
    if id:
        pass
        # items = cursor.execute(f"select id, description from list where id={id}")
    else:
        items = table.find()
    items = [dict(i) for i in items]
    print(items)
    return items

def add_item(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into list (description) values ('{description}')")
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()

def update_item(id, description):
    cursor = connection.cursor()
    cursor.execute(f"update list set description='{description}' where id={id}")
    connection.commit()

if __name__ == "__main__":
    get_items()