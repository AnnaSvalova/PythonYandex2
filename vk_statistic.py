#!/usr/bin/python3
import json
from urllib.request import urlopen
import random
import os

#Для того, чтобы придать программе более эстетичный вид, почистим консоль и уберем курсор.
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# try:
#     os.system('setterm -cursor off')
# except Exception:
#     pass

#Количество пользователей в выборке, по которой бдет оцениваться генеральная совокупность. Все uid генерируются
#псевдослучайным образом.
num_in_sample = 6000
one_percent = num_in_sample // 100
percent = 1
subscript = {}

print('  0% done', end='')

#Основной цикл, с помощью которого собирается статистика
i = 0
while i < num_in_sample:
    uid = str(int(random.random() * 270000000) + 1)
    url = 'http://api.vk.com/method/users.getSubscriptions.json?uid=' + uid
    try:
        data = urlopen(url).read().decode('utf8')
        data = json.loads(data)
    except Exception:
        continue
    users = data['response']['users']['items']
    if users.__len__() == 0:
        continue
    for user in users:
        if user in subscript.keys():
            subscript[user] += 1
        else:
            subscript[user] = 1
    i += 1
    if i % one_percent == 0:
        print('\r%3d' % percent, end='')
        percent += 1

print()

output = []
for id in subscript.keys():
    output.append([subscript[id], id])

#Вывод самых популярных пользователей среди просмотренных
output = sorted(output)[-30:]
for user in output:
    try:
        uid = user[1]
        url = 'http://api.vk.com/method/users.get.json?uid=' + str(uid)
        data = urlopen(url).read().decode('utf8')
        data = json.loads(data)
    except Exception:
        continue
    print('id%-9d    %s %s' % (uid, data['response'][0]['first_name'], data['response'][0]['last_name']))

#Возвращаем курсор
try:
    os.system('setterm -cursor on')
except Exception:
    pass

#TODO сделать скрытие курсора в Windows
#TODO посчитать нормальное количество элементов в выборке для нормальной оценки генеральной совокупности