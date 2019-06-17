# -*- coding: utf8 -*-

from django.shortcuts import render
from .forms import TestForm
import mysql.connector


def landing(request):

    form = TestForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        print("data=", data)
        # print(data["question"])

        add_quest(data)

        new_form = form.save()
    return render(request, 'homepage.html', locals())


def add_quest(data):

    bd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='iloveyou1239',
        database='testdb'
    )
    cur = bd.cursor()

    form = 'SELECT MAX(id) FROM questions'
    cur.execute(form)
    row = cur.fetchall()

    print(row)

    if row[0][0] is None:
        id_now = 1
    else:
        id_now = int(row[0][0]) + 1

    print("ID NOW=", id_now)

    add_id_quest(id_now, data["question"], cur)

    add_answer(id_now, data["fi_answer"], data['correct_answer'], 1, cur)
    add_answer(id_now, data["se_answer"], data['correct_answer'], 2, cur)
    add_answer(id_now, data["th_answer"], data['correct_answer'], 3, cur)
    add_answer(id_now, data["fo_answer"], data['correct_answer'], 4, cur)
    add_answer(id_now, data["fv_answer"], data['correct_answer'], 5, cur)

    bd.commit()


def add_id_quest(id_, text, cur):

    print("ID=", id_, "text=", text)

    form = f'INSERT INTO questions VALUES ("{id_}", "{text}")'
    print(form)
    cur.execute(form)


def add_answer(quest_id, text, is_true, num, cur):

    if str(num) == str(is_true):
        ff = "true"
    else:
        ff = "false"

    form = f'INSERT INTO answers VALUES ("{quest_id}", "{text}", {ff})'
    print(form)
    cur.execute(form)
