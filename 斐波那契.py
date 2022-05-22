#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 获取斐波那契数列
# 方法一
def fid(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
print(1,fid(3))
# 1 1 2 3 5 8 13
# 1 2 3 4 5 6 7
# 方法二 递归方法
def feb2(n):
    if n == 1 or n == 2:
        return 1
    return feb2(n-1) + feb2(n-2)
print(feb2(1))
def feb3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(n - 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs;
print(feb3(9))
