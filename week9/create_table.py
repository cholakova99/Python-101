import sqlite3

connection = sqlite3.connect('busines_card_catalog.db')
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE users
        (id primary key, full_name varchar UNIQUE, email varchar UNIQUE, \
         age integer, phone varchar, additional_info text )
    '''
)
connection.commit()
connection.close()
