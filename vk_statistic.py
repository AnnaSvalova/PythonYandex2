#!/usr/bin/python3
import json
from urllib.request import urlopen
import random

#Количество пользователей в выборке, по которой бдет оцениваться генеральная совокупность
num_in_sample = 1
subscript = {}

#Основной цикл, с помощью которого собирается статистика
for i in range(num_in_sample):
    uid = str(int(random.random() * 21000000) + 1)
    url = 'http://api.vk.com/method/users.getSubscriptions.json?uid=' + uid
    try:
        data = urlopen(url).read().decode('utf8')
        data = json.loads(data)
    except Exception:
        i -= 1
        continue
    print(uid)
    users = data['response']['users']['items']
    print(users)
    for user in users:
        if user in subscript.keys():
            print('OK')
            subscript[user] += 1
        else:
            subscript[user] = 1

output = []
for id in subscript.keys():
    output.append([subscript[id], id])

#Вывод самых популярных пользователей среди просмотренных
output = sorted(output)
for i in range(30):
    print('id' + str(output[i][1]) + ' ' + str(output[i][0]))

print(subscript)
