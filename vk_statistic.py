import json
from urllib.request import urlopen
import random

#Количество пользователей в выборке, по которой бдет оцениваться генеральная совокупность
num_in_sample = 5000

#Основной цикл, с помощью которого собирается статистика
for i in range(num_in_sample):
    uid = int(random.random() * 299999999)
    print(uid)