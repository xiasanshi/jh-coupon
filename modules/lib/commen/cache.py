#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/12 9:05
@Site    : 
@File    : cache.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import os
import logging
from flask_caching import Cache

__author__ = 'xialei'
_logger = logging.getLogger(__name__)

cache = Cache()
