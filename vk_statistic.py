#!/usr/bin/python3
import json
from urllib.request import urlopen
import random
import os

#Для того, чтобы придать программе более эстетичный вид, почистим консоль и уберем курсор (для Linux).
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    os.system('setterm -cursor off')

#Количество пользователей в выборке, по которой будет оцениваться генеральная совокупность. Все uid генерируются
#псевдослучайным образом.
records_total_num = 6000
one_percent = records_total_num // 100
percents = 1
subscription = {}

print('  0% done', end='')

#Основной цикл, с помощью которого собирается статистика
records_num = 0
while records_num < records_total_num:
    uid = str(random.randint(1, 270000000))
    url = 'http://api.vk.com/method/users.getSubscriptions.json?uid=' + uid

    try:
        data = urlopen(url).read().decode('utf8')
        data = json.loads(data)
    except Exception:
        continue

    users = data['response']['users']['items']

    #Нет смысла учитывать пользователей, которые не имеют подписок, так как в данном случае они не несут плезной
    #информации.
    if users.__len__() == 0:
        continue

    for user in users:
        if user in subscription.keys():
            subscription[user] += 1
        else:
            subscription[user] = 1
    records_num += 1
    if records_num % one_percent == 0:
        print('\r%3d' % percents, end='')
        percents += 1

print()

output = list(subscription.items())
output.sort(key=lambda item: item[1], reverse=True)

del subscription

#Вывод самых популярных пользователей среди просмотренных
for user in output[:30]:
    try:
        uid = user[0]
        url = 'http://api.vk.com/method/users.get.json?uid=' + str(uid)
        data = urlopen(url).read().decode('utf8')
        data = json.loads(data)
    except Exception:
        continue
    print('id%-9d    %s %s' % (uid, data['response'][0]['first_name'], data['response'][0]['last_name']))

#Возвращаем курсор (для Linux)
if os.name != 'nt':
    os.system('setterm -cursor on')

#TODO посчитать нормальное количество элементов в выборке для нормальной оценки генеральной совокупности