#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019.12.10 二 15:50
# @Author  : Hui
# @Email   : 719923505@qq.com
# @File    : trans_model.py
# @Software: PyCharm
# @Note    :
"""
import logging

from modules.alipay import AliBaseModel

__author__ = 'Hui'
_logger = logging.getLogger(__name__)


class AliFundTrans(AliBaseModel):
    field_list = ['app_id', 'method', 'charset', 'sign_type', 'timestamp',
                  'version', 'biz_content']
    method = 'alipay.fund.trans.uni.transfer'


class AliFundTransQuery(AliBaseModel):
    field_list = ['app_id', 'method', 'charset', 'sign_type', 'timestamp',
                  'version', 'biz_content']
    method = 'alipay.fund.trans.common.query'


class AliFundTransOrderChanged(AliBaseModel):
    field_list = ['notify_id', 'utc_timestamp', 'msg_method', 'app_id',
                  'version', 'biz_content', 'sign_type', 'charset']
    method = 'alipay.fund.trans.order.changed'
