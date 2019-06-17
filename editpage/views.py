# -*- coding: utf8 -*-

from django.shortcuts import render
from .forms import EditForm
import mysql.connector


def landing(request):

    form = EditForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        # print("data=", data)
        # print(data["question"])

        add_quest(data)

        new_form = form.save()
    return render(request, 'editpage.html', locals())


def add_quest(data):

    bd = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='iloveyou1239',
        database='testdb'
    )
    cur = bd.cursor()

    id_now = int(data["question_num"])

    print("ID NOW=", id_now)

    delete_all(id_now, cur)
    add_id_quest(id_now, data["question"], cur)

    add_answer(id_now, data["fi_answer"], data['correct_answer'], 1, cur)
    add_answer(id_now, data["se_answer"], data['correct_answer'], 2, cur)
    add_answer(id_now, data["th_answer"], data['correct_answer'], 3, cur)
    add_answer(id_now, data["fo_answer"], data['correct_answer'], 4, cur)
    add_answer(id_now, data["fv_answer"], data['correct_answer'], 5, cur)

    bd.commit()


def delete_all(id_, cur):

    form = f'DELETE FROM questions WHERE id = {id_}'
    print(form)
    cur.execute(form)

    form = f'DELETE FROM answers WHERE quest_id = {id_}'
    print(form)
    cur.execute(form)


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
