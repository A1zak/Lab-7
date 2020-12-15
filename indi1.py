#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 17
# Ввести список А из 10 элементов, найти квадраты элементов кратных 4 и их количество.Преобразованный массив вывести.

import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    c = 0
    n = []
    for i in A:
        if i % 4 ==0:
            c += i % 4 == 0
            i *= i
        n.append(i)
    print(n)
    print(c)