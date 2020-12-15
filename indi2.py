#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант2
# В списке, состоящем из вещественных элементов, вычислить:
# 1) сумму положительных элементов списка;
# 2) произведение элементов списка, расположенных между максимальным по модулю и
# минимальным по модулю элементами.
# Упорядочить элементы списка по убыванию

if __name__ == '__main__':
    A = tuple(map(float, input().split()))
    D = list(A)
    sum = 0
# Задание №1
    for i in A:
        if i > 0:
            sum += i
    print(sum)

# Задание №2
    B = []
    n_min = n_max = A[0]
    i_min = i_max = 0
    b = [abs(i) for i in A]
    for i, item in enumerate(b):
        if item < n_min:
            i_min, n_min = i, item
        if item >= n_max:
            i_max, n_max = i, item
    С = A[i_min:i_max+1]
    sum = 1
    for j in С:
        sum *= j
    print(sum)
    D.sort(reverse=True)
    print(f"{A} ")