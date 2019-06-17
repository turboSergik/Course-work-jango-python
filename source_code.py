# -*- coding: utf8 -*-

import requests
import json
import telebot
from telebot import types
import pprint as pp
import sql_get_test

token = '866464818:AAEUdHTdgJCmkql3GdRu9o0yERucK9Dlq4U'
bot = telebot.TeleBot(token)

my_id = 493304937
my_try_id = my_id

id_for_access = 0

flag = 0
local_id = 228322
cur_user = ""
access_cur_user = ""


def log(message):
    print(
        f'Новое сообщение от {message.from_user.first_name} {message.from_user.last_name} \n С текстом: {message.text} ')


def get_id():
    return local_id


def in_afk():
    in_1()


def in_1():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='>>>', callback_data='2')

    key.add(but_1)

    mess = "Сейчас я тебя обучу работать с классами на шарпах. Всё что нужно - в этом уроке. Этакий краткий"
    mess += " экскурс по 2 сему шарпов. Интерфейс интуитивно-понятный. К каждому объяснению/коду будет добавлен файлик"
    mess += " с кодом + источник. Так что самостоятельно всё узнать будет не составлять труда. Ну так что, приступим!"

    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_2():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='>>>', callback_data='3')
    but_2 = types.InlineKeyboardButton(text='<<<', callback_data='1')

    mess = "О, ты не закрыл мой проэкт с первой страницы! Клёво. Наверное... Первое, что тебе предстоит - это выбрать"
    mess += " направление для изучения. Тут предоставлен краткий список всего того, что тебе может понадобится."
    mess += " Каждый пунктик познавателен и очень полезен. Окей, обучение начинается!!"

    key.add(but_2, but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_3():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='2')

    but_3 = types.InlineKeyboardButton(text='Классы как таковые + конструкторы', callback_data='class')
    but_4 = types.InlineKeyboardButton(text='Свойства', callback_data='const')
    but_5 = types.InlineKeyboardButton(text='Индексаторы', callback_data='ind')

    but_6 = types.InlineKeyboardButton(text='Интерфейсы, что б их!', callback_data='inter')
    but_7 = types.InlineKeyboardButton(text='Ннннаследование', callback_data='nasik')
    but_8 = types.InlineKeyboardButton(text='Что-то про делегаты', callback_data='deleg')
    but_9 = types.InlineKeyboardButton(text='Helllo, I\'m event', callback_data='events')
    but_10 = types.InlineKeyboardButton(text='Pass the C # test', callback_data='start_test')

    mess = "Выбери пункт, который хочешь изучить!"

    key.add(but_3)
    key.add(but_4)
    key.add(but_5)
    key.add(but_6)
    key.add(but_8)
    key.add(but_9)
    key.add(but_7)
    key.add(but_10)

    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_class():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')
    but_2 = types.InlineKeyboardButton(text='Ссылочка на метанит', url='https://metanit.com/sharp/tutorial/3.1.php')
    but_3 = types.InlineKeyboardButton(text='source_code by author(me)', url='https://ideone.com/ZsEFGf')

    mess = "О, классы. Классы в шарпах как и в любом другом языке чертовки важны. Работа с классами это одно из первых,"
    mess += " чему должен научиться уважающий себя кодер. Если вкратце, классы это отдельный тип данных, который "
    mess += "создаёт сам пользователь. Этот тип данных имеет свои методы, и другие разные клёвые штуки. Как и обещал,"
    mess += "тут есть ссылка на metanit - клёвый сайтик где очень много всего полезного про классы и вообще про шарпы "
    mess += "а так же классоый код, написанный мной."

    key.add(but_2)
    key.add(but_3)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_inter():
    print("IN INTER")

    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')
    but_2 = types.InlineKeyboardButton(text='Metanit com', url='https://metanit.com/sharp/tutorial/3.9.php')
    but_3 = types.InlineKeyboardButton(text='Source код лежит на метаните', callback_data='None')

    mess = "Интерфейсы очень странный предмет. Сам объект есть, а реализации нет... Интерфейс это объект, содержащий"
    mess += "набор методов и свойств. Вся фича интерфейсов в том, что реализуют функционал интерфейа классы и "
    mess += "структуры, которые используют этот интерфейс. Чем-то напоминает абстрактные функции.... почти, но нет."
    mess += " В шарпах запрещено множественное наследование... А вот интерфейсы это ограничение обходят. Здорово"
    mess += ", правда?"

    key.add(but_2)
    key.add(but_3)
    key.add(but_1)

    print("BEFORE SEND")

    print(mess, id, get_id(), sep='\n')

    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)

    print("AFTER SEND")


def in_del():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')
    but_2 = types.InlineKeyboardButton(text='Метанит', url='https://metanit.com/sharp/tutorial/3.13.php')
    # but_3 = types.InlineKeyboardButton(text='Code', url='vk.com/shun_kuzo')

    mess = "Делегаты. Очень топовые штуки, от части бесполезные, но иногда можно найти полезное применение. Что это?"
    mess += "Хз. Шутка. Делегаты это указатели на методы. Непонятно, верно? Для меня делегаты это копирование и "
    mess += "изменение названия функции. Есть функция abs, а мы её просто копируем, переназываем как \"kek\" и"
    mess += " используем как kek() по факту обращаясь к функции abs. И всё это в коде, не трогая 1 функцию."
    mess += " Вот что такое делегаты. Так же к делегату можно привязать сразу несколько фукнций, и делегат будет "
    mess += "просто вызывать их всех по порядку."

    key.add(but_2)
    # key.add(but_3)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_event():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')
    but_2 = types.InlineKeyboardButton(text='Ссылка на инфу', url='https://metanit.com/sharp/tutorial/3.14.php')
    but_3 = types.InlineKeyboardButton(text='Source code лежит на метаните', callback_data='none')

    mess = "Ивенты. Если вкратце - сигнализируют о том, что что-то произошло. Этакие триггеры на некоторые события. "
    mess += "Привязаны к делегатам. Про них сложно "
    mess += "много сказать. Как говорится, лучше 1 раз увидеть, чем 3 раза услышть. Или не 3....."
    mess += ""
    mess += ""
    mess += ""

    key.add(but_2)
    key.add(but_3)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_const():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')
    but_2 = types.InlineKeyboardButton(text='Как всегда, ссылочка на метанит',
                                       url='https://metanit.com/sharp/tutorial/3.4.php')
    but_3 = types.InlineKeyboardButton(text='source_code by author(me)', url='https://ideone.com/FQqObi')

    mess = "Хмммм, а теперь про свойства. Существуют пециальные методы доступа, которые называют свойства."
    mess += " Они обеспечивают такие приятные штуки как простой доступ к полям класса, узнать их значение или выполнить"
    mess += " их установку. Свойства очень полезны, они позволяют не нарушая принципа инкапсуляции изменять поля"
    mess += " класса и получить к ним доступ без особых труднойстей"

    key.add(but_2)
    key.add(but_3)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_ind():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')
    but_3 = types.InlineKeyboardButton(text='sOURce code', url='https://ideone.com/7qWiyi')
    but_2 = types.InlineKeyboardButton(text='MeTaNiT.CoM :) ',
                                       url='https://metanit.com/sharp/tutorial/4.10.php')

    mess = "Хоп, а вот и индексаторы подъехали. Индексаторы это такие штуки, которые позволяют получить доступ к"
    mess += "любому полю класса по индексу. ЭТО ВООБЩЕ ЗАКОННО?!?!?!? Если говорить вкратце, это простое"
    mess += " переопределение оператора []. Используется гораздо реже, чем свойства, но не менее удобно. И традиционные"
    mess += "Ссылочки на всё, что нужно"

    key.add(but_2)
    key.add(but_3)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_nasik():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')
    but_3 = types.InlineKeyboardButton(text='Наследование', callback_data='nasik_1')
    but_2 = types.InlineKeyboardButton(text='как всегда, Метанит ',
                                       url='https://metanit.com/sharp/tutorial/4.10.php')
    but_4 = types.InlineKeyboardButton(text='Сам код ',
                                       url='https://ideone.com/ppbB1K')

    mess = "Наследование является одним из ключевых моментов ООП. Благодаря наследованию"
    mess += " один класс может унаследовать функциональность другого класса. Наследник в процессе наследует все "
    mess += "те же свойства, методы, поля, которые есть в классе, КРОМЕ конструктора."
    mess += "Сейчас я Вам на живом примере покажу, что такое наследование. Lets start!"

    key.add(but_3)
    key.add(but_2)
    key.add(but_4)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_nasik_1():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik')
    but_2 = types.InlineKeyboardButton(text='Устройство.', callback_data='None')
    but_3 = types.InlineKeyboardButton(text='Телефон', callback_data='nasik_3')
    but_4 = types.InlineKeyboardButton(text='Компьютер', callback_data='nasik_4')

    mess = "Покажу Вам примеры наследования на чем-то нереально простом. Возьмём базовый класс - устройство. "
    mess += "Устройство подразумивает собой множество объектов, без какой-то конкретики. На данный момент наш объект"
    mess += " имеет один атрибут - стоимость.  \n\n Атрибуты: \n  Стоимость."

    key.add(but_2)
    key.add(but_3, but_4)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_nasik_3():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_1')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Телефон.        ', callback_data='None', )
    but_3 = types.InlineKeyboardButton(text='IPhone', callback_data='ip')
    but_4 = types.InlineKeyboardButton(text='Meizu', callback_data='me')
    but_5 = types.InlineKeyboardButton(text='Xiaomi', callback_data='xi')

    mess = "Класс телефон наследуется от класса -Устройство. Соответственно берёт все его свойства + добавляет свои."
    mess += " Уникальные для этого класса. И так происходит с каждым последующим наследованием."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Марка телефона. \n  Размер экрана."
    mess += ""

    key.add(but_2)
    key.add(but_3, but_4, but_5)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_xi():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_3')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Телефон. Xiaomi   ', callback_data='None', )

    mess = "Класс Xiaomi наследуется от класса -phone. Появился новый метод."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Марка телефона. \n  Размер экрана. \n  Уникальный серийный номер Xiaomi"
    mess += ""

    key.add(but_2)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_me():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_3')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Телефон. Meizu   ', callback_data='None', )

    mess = "Класс Meizu наследуется от класса -phone. Появился новый метод."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Марка телефона. \n  Размер экрана. \n  Уникальный серийный номер Meizu"
    mess += ""

    key.add(but_2)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_ip():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_3')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Телефон. Iphone   ', callback_data='None', )

    mess = "Класс iphone наследуется от класса -phone. Появился новый метод."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Марка телефона. \n  Размер экрана. \n  Уникальный ID айфона"
    mess += ""

    key.add(but_2)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_nasik_4():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_1')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Компьютер.  ', callback_data='None', )
    but_3 = types.InlineKeyboardButton(text='ultrabook', callback_data='ul')
    but_4 = types.InlineKeyboardButton(text='Laptop', callback_data='la')
    but_5 = types.InlineKeyboardButton(text='Neetbook', callback_data='ne')

    mess = "Класс компьютер наследуется от класса -Устройство. Соответственно берёт все его свойства + добавляет свои."
    mess += " Уникальные для этого класса. И так происходит с каждым последующим наследованием."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Вес. \n  Мощность процессора. \n  Объем оперативной памяти."
    mess += ""

    key.add(but_2)
    key.add(but_3, but_4, but_5)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_ul():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_4')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Компьютер. ultrabook   ', callback_data='None', )

    mess = "Класс ultrabook наследуется от класса -computer. Появился новый метод."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Вес. \n  Мощность процессора. \n  Объем оперативной памяти. \n "
    mess += " Уникальный ID ноутбука"

    key.add(but_2)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_la():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_4')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Компьютер. laptop   ', callback_data='None', )

    mess = "Класс laptop наследуется от класса -computer. Появился новый метод."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Вес. \n  Мощность процессора. \n  Объем оперативной памяти. \n "
    mess += " Уникальный ID ноутбука"

    key.add(but_2)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_ne():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='nasik_4')
    but_2 = types.InlineKeyboardButton(text='     Устройства. Компьютер. Neetbook   ', callback_data='None', )

    mess = "Класс Neetbook наследуется от класса -computer. Появился новый метод."
    mess += "\n\nАтрибуты: \n  Стоимость. \n  Вес. \n  Мощность процессора. \n  Объем оперативной памяти. \n "
    mess += " Уникальный ID ноутбука"

    key.add(but_2)
    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_c_test(message):

    # key = types.InlineKeyboardMarkup()

    mess, key = sql_get_test.get_test_by_id(message)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_start_test():

    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')

    but_2 = types.InlineKeyboardButton(text='Угу.', callback_data='C#_10')
    but_3 = types.InlineKeyboardButton(text='Редактировать тест (нужна админка).', callback_data='check_access')

    mess = "Сейчас тебя ждёт небольшой тестик по шарпам. Вопросы не сложные. Готов?"

    key.add(but_2)
    key.add(but_3)

    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_finish_test():
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='3')

    res = 'X/X'
    mess = f'Вы завершили тест. Ваш результат: {res}'

    key.add(but_1)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_check_access():

    flag_ = sql_get_test.has_id(my_id)

    if flag_ is True:
        edit_test()
    else:
        access_denied()


def access_denied():

    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='start_test')

    but_2 = types.InlineKeyboardButton(text='Отправить запрос за разрешение', callback_data='try_get_access')

    mess = "Простите, но у Вас недостаточно прав на редактирование теста. Но вы можете отправить запрос " \
           "разработчику для возможности редактирования теста."

    key.add(but_2)

    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def in_try_get_access():

    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='<<<', callback_data='start_test')

    get_access_from_admin()

    mess = "Запрос отправлен и будет рассмотрен в ближайшее время. Спасибо!"

    key.add(but_1)
    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def get_access_from_admin():

    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Accept', callback_data='accept_req')
    but_2 = types.InlineKeyboardButton(text='Reject', callback_data='reject_req')

    mess = f"Привет! У Вас вот этот чел @{cur_user}  попросил админку. Подтвердить разрешеие?"

    global id_for_access
    global access_cur_user

    id_for_access = my_id
    access_cur_user = cur_user

    key.add(but_1, but_2)

    bot.send_message(my_try_id, mess, reply_markup=key)
    # bot.edit_message_text(mess, my_try_id, get_id(), reply_markup=key)


def in_accept_req():
    sql_get_test.add_id(id_for_access)
    in_reject_req(1)


def in_reject_req(ff):

    key = types.InlineKeyboardMarkup()

    if ff == 1:
        mess = f"Запрос подтверждён для @{access_cur_user}"
    else:
        mess = f"Запрос Отклонен для @{access_cur_user}"

    # bot.send_message(my_id, mess, reply_markup=key)
    bot.edit_message_text(mess, my_id, get_id(), reply_markup=key)


def edit_test():
    print("this func for editinng test")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    # pp.pprint(message)

    if message.text == '/start':
        answer = 'Привет! Сейчас тебя научат шарпам. Будет клёво. Наверное.... Но это вообще не точно.' \
                 ' Good luck and have Fun. Готов?'

        key = types.InlineKeyboardMarkup()
        keyb = types.InlineKeyboardButton(text='Афкос!', callback_data='afk')
        key.add(keyb)

        bot.send_message(message.chat.id, answer, reply_markup=key)


@bot.callback_query_handler(func=lambda c: True)
def answer_inline(message):

    print(message.message)
    print("id=", message.message.message_id)

    global local_id
    global my_id
    global cur_user

    local_id = message.message.message_id
    my_id = message.message.chat.id
    cur_user = message.message.chat.username

    if message.data == '1':
        in_1()
    if message.data == '2':
        in_2()
    if message.data == '3':
        in_3()
    if message.data == 'class':
        in_class()
    if message.data == 'const':
        in_const()
    if message.data == 'ind':
        in_ind()
    if message.data == 'afk':
        in_afk()
    if message.data == 'inter':
        in_inter()
    if message.data == 'nasik':
        in_nasik()
    if message.data == 'deleg':
        in_del()
    if message.data == 'events':
        in_event()
    if message.data == 'nasik_1':
        in_nasik_1()
    if message.data == 'nasik_3':
        in_nasik_3()
    if message.data == 'nasik_4':
        in_nasik_4()
    if message.data == 'ip':
        in_ip()
    if message.data == 'me':
        in_me()
    if message.data == 'xi':
        in_xi()
    if message.data == 'ul':
        in_ul()
    if message.data == 'la':
        in_la()
    if message.data == 'ne':
        in_ne()
    if message.data == 'start_test':
        in_start_test()
    if message.data == 'finish_test':
        in_finish_test()
    if message.data == 'check_access':
        in_check_access()
    if message.data == 'try_get_access':
        in_try_get_access()
    if message.data == 'accept_req':
        in_accept_req()
    if message.data == 'reject_req':
        in_reject_req(0)

    """
    if message.data[0:2] == "С#":
        print("lel")
    else:
        print("NO!")
    """

    if message.data[0:2] == 'C#':
        print("go to C#")
        in_c_test(message.data)

    """
    but_3 = types.InlineKeyboardButton(text='ultrabook', callback_data='ul')
    but_4 = types.InlineKeyboardButton(text='Laptop', callback_data='la')
    but_5 = types.InlineKeyboardButton(text='Neetbook', callback_data='ne')
    """

    # del_last()


bot.polling(timeout=20)

"""
1558791185
1558791212
"""
