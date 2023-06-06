# working with sqlite3

import sqlite3

conn = sqlite3.connect('py.db')
print('success')

conn.execute(
    '''CREATE TABLE items (
         ID INT PRIMARY KEY,
         ITEM_NAME TEXT,
         PRICE INT,  STATUS TEXT)'''
)

print('Table created successfully')