#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/29 20:58
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : jh_const.py
# @Software: PyCharm
# @Note    :
"""
import logging
from modules.lib.commen.const import Const

_logger = logging.getLogger(__name__)
__author__ = "xialei"

JH_URI = Const()
JH_URI.shop_info = "/jh/manager/shop"  # 店铺信息

JH_URI.products_info = "/jh/product/shop/shop_id/product/query"  # 产品信息
JH_URI.product_info = "/jh/product/shop/{shop_id}/product/{product_id}/query"  # 产品信息
JH_URI.cart_info = "/jh/member/cart/shop/shop_id/query"  # 购物车信息

JH_URI.product_stock_update = "/jh/product/shop/shop_product/stock/update"  # 扣库存
