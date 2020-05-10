#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/17 9:32
@Site    : 
@File    : singleton.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   : 单例
"""
import os
import logging
from functools import wraps

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


class Test(metaclass=Singleton):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_b(self):
        return self.b

    def get_a(self):
        return self.a


@singleton
class Test1(metaclass=Singleton):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_b(self):
        return self.b

    def get_a(self):
        return self.a


def main():
    t = Test('a', 'a')
    print(t.get_a())
    t1 = Test('t1', 't1')
    print(t1.get_a())
    t = Test1('a', 'a')
    print(t.get_a())
    t1 = Test1('t1', 't1')
    print(t1.get_a())


if __name__ == '__main__':
    main()
    pass
