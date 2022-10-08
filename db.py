"""Для работы с базой данных"""
import sqlite3

con = sqlite3.connect("db.db")
cur = con.cursor()


def add_member(id, user):
    query = f"INSERT INTO members (id_member, username) values (?, ?)"
    params = (id, user)
    cur.execute(query, params)
    con.commit()

def select_users():
    query = "select id_member from members"
    cur.execute(query)
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    return result

def add_task(messs, id):
    query = "INSERT INTO tasks (message, author) values (?, ?)"
    params = (messs, id)
    cur.execute(query, params)
    con.commit()

def get_id(id):
    query = f"select id from members where id_member = {id}"
    cur.execute(query)
    real_id = cur.fetchone()[0]
    return real_id

def list_of_tasks(id):
    query = f"select message from tasks where author = {id}"
    cur.execute(query)
    list_of_dirty = cur.fetchall()
    list_of_pure = []
    for x in list_of_dirty:
        list_of_pure.append(x[0])
    return list_of_pure

def get_id_text(message):
    query = f"select id from tasks where message = '{message}'"
    cur.execute(query)
    message_id = cur.fetchone()[0]
    return message_id

def delete_task(messag):
    query = f"delete from tasks where message = '{messag}'"
    cur.execute(query)
    con.commit()

def list_of_all_messages():
    query = f"select message from tasks"
    cur.execute(query)
    list_of_dirty = cur.fetchall()
    list_of_pure = []
    for x in list_of_dirty:
        list_of_pure.append(x[0])
    return list_of_pure