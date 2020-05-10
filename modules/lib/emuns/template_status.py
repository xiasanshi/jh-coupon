#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/11/17 16:52
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : template_status.py
# @Software: PyCharm
# @Note    :
"""
import logging
from enum import unique, Enum

_logger = logging.getLogger(__name__)
__author__ = "xialei"


@unique
class TemplateStatusEnum(Enum):
    ON = "ON"
    OFF = "OFF"
