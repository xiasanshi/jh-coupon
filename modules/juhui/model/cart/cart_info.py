#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/6 9:39
@Site    : 
@File    : cart_info.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import os
import logging
from ..base import JHBaseModel
from ...config.jh_const import JH_URI

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class CartModel(JHBaseModel):
    fields = ['cart_id']
    uri = JH_URI.cart_info


def main():
    INPUT = ''


if __name__ == '__main__':
    main()
