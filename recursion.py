#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
"""Implementing functions using recursion"""


def fibonacci(number):
    if number ==0:
        return number
    elif number <= 2:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


def gcd(x, y):
    if (x == 0):
        return y
    else:
        return gcd((y % x), x)


def compareTo(s1, s2):
    if (len(s1)>1) and (len(s2)>1):
        if s1[0] == s2[0]:
            return 0
        elif s1[0] < s2[0]:
            return -1
        else:
            return bool(s1[0]>s2[0]) + compareTo(s1[1:], s2[1:])

if __name__ == '__main__':
    print(fibonacci(7))
    print(fibonacci(13))
    print(gcd(42, 28))
    print(compareTo('Hello', 'hello'))
