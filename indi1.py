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
    print(A)

    j = 0
    for i, item in enumerate(A):
        if item % 4 == 0:
            A[i] *= A[i]
            j += 1

    print(f"Преобразованный массив = {A} \nКол-во элементов возведенных в квадрат = {j}")
