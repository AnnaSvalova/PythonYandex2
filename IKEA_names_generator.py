#!/usr/bin/python3
from random import choice, randint

letters_and_syllables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'au', 'eu', 'ou', 'sc', 'sk', 'und', 'tion',
                         'sion', 'ssion', 'ti', 'ia', 'jo', 'la']

print('Enter number of names > ', end='')
num = int(input())

for i in range(num):
    syllables_num = randint(3, 7)
    name = ''.join([choice(letters_and_syllables) for syllable in range(syllables_num)])
    print(name)