#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/29 22:05
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : utils.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
import random
import string

_logger = logging.getLogger(__name__)
__author__ = "xialei"


def get_nonce_str(length=32):
    '''

    Args:
        length(int): 随机数的长度

    Returns:
        返回length长度的随机字符串

    '''
    char = string.ascii_letters + string.digits
    return "".join(random.choice(char) for _ in range(length))


def main():
    print(get_nonce_str())


if __name__ == "__main__":
    main()
