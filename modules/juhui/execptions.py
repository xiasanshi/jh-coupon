#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/18 21:22
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : execptions.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class JHException(Exception):
    def __init__(self, msg):
        super(JHException, self).__init__(msg)

