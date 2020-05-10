#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/1 16:53
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : shop_product.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from ..base import JHBaseModel
from ...config.jh_const import JH_URI

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class ShopProductInfoModel(JHBaseModel):
    uri = JH_URI.product_info
    fields = ['product_id', 'shop_id']


class ShopProductsInfoModel(JHBaseModel):
    uri = JH_URI.products_info
    fields = ['product_ids']
