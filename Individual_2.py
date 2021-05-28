#!/usr/bin/env python3
# -*- coding^ utf-8 -*-

#Дано слово. Поменять местами его вторую и пятую буквы.

s = input("Введите слово: ")
r = s.split()
d = []
for i in r:
    d.append(i[0] + i[4] + i[2] + i[3] + i[1] + i[5:])
print (d)
