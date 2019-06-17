import mysql.connector
from telebot import types

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='iloveyou1239',
    database='testdb'
)
cur = bd.cursor()


def get_count_quest():

    form = 'SELECT MAX(id) FROM questions'

    cur.execute(form)
    row = cur.fetchall()

    print(row[0][0])
    return row[0][0]


def get_text(id_):

    form = f'SELECT text FROM questions WHERE id = {id_}'

    cur.execute(form)
    row = cur.fetchall()
    return row[0][0]


def get_count_answers(id_):
    form = f'SELECT count(is_true) FROM answers WHERE quest_id = {id_}'

    cur.execute(form)
    row = cur.fetchall()

    return row[0][0]


def get_resp(id_):
    form = f'SELECT text, is_true FROM answers WHERE quest_id = {id_}'

    cur.execute(form)
    row = cur.fetchall()

    return row


def get_test_by_id(message):

    id_quest = message[3:len(message) - 1]
    mess = get_text(id_quest)

    # finish_test

    key = types.InlineKeyboardMarkup()

    resp = get_resp(id_quest)

    for data_ in resp:
        quest_text = data_[0]
        ff = data_[1]

        if int(id_quest) == int(get_count_quest()):
            callback = 'finish_test'
        else:
            callback = 'C#_' + str(int(id_quest) + 1) + str(ff)

        but = types.InlineKeyboardButton(text=quest_text, callback_data= callback)
        key.add(but)
        print("+ ", quest_text)

    last_but = types.InlineKeyboardButton(text='<<<', callback_data='3')

    key.add(last_but)

    return mess, key


def has_id(id_):

    print("CHECK", id_)

    form = f'SELECT * FROM admin WHERE id = {id_}'
    print(form)

    cur.execute(form)
    row = cur.fetchall()

    print(row)
    print(len(row))

    if len(row) == 0:
        return False
    return True


def add_id(id_):

    form = f'INSERT INTO admin VALUES ("{id_}")'

    cur.execute(form)
    bd.commit()

# get_test_by_id("c#_10")
