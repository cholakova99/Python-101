import sqlite3


def add(user_name, email, age, phone, add_info):
    connection = sqlite3.connect('busines_card_catalog.db')
    cursor = connection.cursor()
    if not isinstance(user_name, str) or not isinstance(email, str) or not isinstance(phone, str):
        raise ValueError("Invalid input for user name or email")
    if not isinstance(age, int):
        raise ValueError("Invalid input for age")
    if not isinstance(add_info, str) and add_info is not None:
        raise ValueError("Invalid input for age")
    cursor.execute(" select count(full_name) from users;")
    data_helper = cursor.fetchall()
    next_id = data_helper[0][0]
    next_id += 1
    ins = f'''
        INSERT INTO users (id, full_name, email, age, phone, additional_info)
        VALUES({next_id},"{user_name}", "{email}", {age}, "{phone}", "{add_info}")
    '''
    cursor.execute(ins)
    connection.commit()
    connection.close()


def list_info():
    connection = sqlite3.connect('busines_card_catalog.db')
    cursor = connection.cursor()
    sel = f'''
        SELECT *
        FROM users
    '''
    cursor.execute(sel)
    data_info = cursor.fetchall()
    connection.commit()
    connection.close()
    return data_info


def delete(id_number):
    connection = sqlite3.connect('busines_card_catalog.db')
    cursor = connection.cursor()
    cursor.execute(" select count(full_name) from users;")
    data_helper = cursor.fetchall()
    last_id = data_helper[0][0]
    if id_number > last_id:
        raise ValueError("Wrong index!")
    del_info = f'''
        DELETE FROM users
        WHERE id = {id_number};
    '''
    cursor.execute(del_info)
    connection.commit()
    connection.close()


def get(id_number):
    connection = sqlite3.connect('busines_card_catalog.db')
    cursor = connection.cursor()
    sel = f'''
    SELECT id, email, full_name FROM users WHERE id = {id_number}
    '''
    cursor.execute(sel)
    data_helper = cursor.fetchall()
    connection.commit()
    connection.close()
    return data_helper
