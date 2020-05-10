#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/11/27 10:45
@Site    : 
@File    : biz_content.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
from modules.alipay.model.base import AliBaseModel

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class BizContentModel(AliBaseModel):
    field_list = ['out_trade_no']

    @classmethod
    def create_model_factory(cls, data, tag=None, **kwargs):
        if tag == 'create':
            field_list = ["out_trade_no", "subject", "total_amount", "buyer_id"]
        elif tag == 'pay':
            field_list = ["out_trade_no", "scene", "auth_code", "subject", "total_amount"]
        elif tag == 'query':
            field_list = ["trade_no"]
        elif tag == 'fund_trans':
            field_list = ["out_biz_no", "trans_amount", "product_code", "payee_info"]
        elif tag == 'fund_query':
            field_list = []
        else:
            field_list = cls.field_list
        field_list.extend(kwargs.keys())
        data.update(kwargs)
        cls.field_list = field_list
        return cls(data)


class PayeeInfo(AliBaseModel):
    field_list = ['identity']
