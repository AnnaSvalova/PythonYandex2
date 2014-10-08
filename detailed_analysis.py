#!/usr/bin/python3
#В этом модуле проводится проверка всех пользователей сервиса vk.com. Простая ручная проверка показала, что теоретически
#может существовать пользователь с uid=2147483647. Дальше по этому параметру происходит переполнение. Поэтому
#проверяются все uid от 1 до 2147483647. Работает очень долго.
import json
from urllib.request import urlopen
import datetime

def get_count(new_uid):
    url = 'http://api.vk.com/method/users.getFollowers.json?uid=' + new_uid
    data = urlopen(url).read().decode('utf8')
    data = json.loads(data)
    return int(data['response']['count'])

popular = {}
errors = []
count_of_popular = 0

start = datetime.datetime.now()
print(start)

for i in range(2147483647):
    uid = str(i + 1)
    try:
        count = get_count(uid)
        if count > 100000:
            popular[uid] = count
            print(uid)
    except Exception:
        errors.append(uid)

for i in range(10):
    for j in range(errors.__len__()):
        try:
            count = get_count(errors[j])
            if count > 100000:
                popular[errors[j]] = count
            errors.__delitem__(j)
        except Exception:
            pass

stop = datetime.datetime.now()
print(stop)

print(popular)
