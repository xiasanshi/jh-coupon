#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/15 10:20
@Site    : 
@File    : role_emuns.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
from enum import unique, Enum

_logger = logging.getLogger(__name__)
__author__ = "xialei"


@unique
class ISAdminEnum(Enum):
    yes = "YES"  # 系统用户
    no = "NO"


@unique
class ISSystemEnum(Enum):
    yes = 1  # 系统用户
    no = 0
