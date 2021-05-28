#!/usr/bin/env python3
# -*- coding^ utf-8 -*-

#Дан текст, имеющий вид: « », где di – цифры ( ). Вычислить записанную в тексте алгебраическую сумму.

s = '+' + input()
print(sum([int(s[i : i + 2]) for i in range(0, len(s), 2)]))