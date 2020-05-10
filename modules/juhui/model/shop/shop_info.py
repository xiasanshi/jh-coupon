#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/18 21:31
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : shop_info.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from ..base import JHBaseModel
from ...config.jh_const import JH_URI

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class ShopInfoModel(JHBaseModel):

    uri = JH_URI.shop_info

    def __init__(self):
        pass
