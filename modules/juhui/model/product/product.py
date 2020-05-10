#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/7 17:05
@Site    :
@File    : product.py
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


class ProductModel(JHBaseModel):
    fields = ['product_ids']
    uri = JH_URI.product_info

