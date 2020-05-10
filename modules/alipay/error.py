#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/29 21:00
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : error.py
# @Software: PyCharm
# @Note    :
"""
import logging

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class AliException(Exception):
    def __init__(self, msg):
        super(AliException, self).__init__(msg)


class PAYError(AliException):
    pass


class NotifyError(AliException):
    pass


class RequestError(AliException):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
