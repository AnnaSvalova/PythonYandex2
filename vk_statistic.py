#!/usr/bin/python3
import json
from urllib.request import urlopen
import random

#Количество пользователей в выборке, по которой бдет оцениваться генеральная совокупность
num_in_sample = 500
subscript = {}
max = 0

#Основной цикл, с помощью которого собирается статистика
i = 0
while i < num_in_sample:
    uid = str(int(random.random() * 270000000) + 1)
    url = 'http://api.vk.com/method/users.getSubscriptions.json?uid=' + uid
    try:
        data = urlopen(url).read().decode('utf8')
        data = json.loads(data)
    except Exception:
        i -= 1
        continue
    users = data['response']['users']['items']
    if users.__len__() == 0:
        i -= 1
        continue
    for user in users:
        if user in subscript.keys():
            subscript[user] += 1
        else:
            subscript[user] = 1
        if subscript[user] > max:
            max = subscript[user]
    i += 1

print(max)
output = []
for id in subscript.keys():
    output.append([subscript[id], id])
print(output)

#Вывод самых популярных пользователей среди просмотренных
output = sorted(output)
for i in range(30):
    print('id' + str(output[i][1]) + ' ' + str(output[i][0]))

#print(subscript)
