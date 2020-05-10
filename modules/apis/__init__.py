#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/9 11:16
@Site    : 
@File    : __init__.py.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
from .admin import create_ns as api_admin
from .v1 import create_ns as api_v1
from .test import create_ns as test_api


def create_ns():
    return [api_admin(), api_v1(), test_api()]
