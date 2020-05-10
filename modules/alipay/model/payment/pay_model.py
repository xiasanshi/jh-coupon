#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019.12.10 二 15:50
# @Author  : Hui
# @Email   : 719923505@qq.com
# @File    : pay_model.py
# @Software: PyCharm
# @Note    :
"""

import logging

from modules.alipay import AliBaseModel

__author__ = 'Hui'
_logger = logging.getLogger(__name__)


class AliPayCreateModel(AliBaseModel):
    field_list = ['app_id', 'method', 'charset', 'sign_type', 'timestamp',
                  'version', 'biz_content']
    method = "alipay.trade.create"


class AliPayPayModel(AliBaseModel):
    field_list = ['app_id', 'method', 'charset', 'sign_type', 'timestamp',
                  'version', 'biz_content']
    method = "alipay.trade.pay"


class AliPayQueryModel(AliBaseModel):
    field_list = ['app_id', 'method', 'charset', 'sign_type', 'timestamp',
                  'version', 'biz_content']
    method = "alipay.trade.query"
