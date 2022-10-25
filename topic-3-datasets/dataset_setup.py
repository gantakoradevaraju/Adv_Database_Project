import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Guava' },
        { "description": 'Apples' },
        { "description": 'Grapes' },
        { "description": 'Banana' },
        { "description": 'Onions' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()