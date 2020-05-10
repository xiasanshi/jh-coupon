#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/27 12:49
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : shop_product_stock_update.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from ..base import JHBaseModel
from ...config.jh_const import JH_URI

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class ShopProductStockUpdateModel(JHBaseModel):
    uri = JH_URI.product_stock_update
    fields = ['products']

def main():
    pass


if __name__ == "__main__":
    main()
