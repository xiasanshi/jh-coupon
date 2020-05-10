#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/29 20:58
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : wx_const.py
# @Software: PyCharm
# @Note    :
"""
import logging
from modules.lib.commen.const import Const

_logger = logging.getLogger(__name__)
__author__ = "xialei"

WX_URI = Const()
WX_URI.unifiedorder = "/pay/unifiedorder"  # 下单
WX_URI.orderquery = "/pay/orderquery"  # 查询
WX_URI.closeorder = "/pay/closeorder"  # 关闭订单
WX_URI.refund = "/secapi/pay/refund"  # 退款
WX_URI.refundquery = "/pay/refundquery"  # 退款查询
WX_URI.micropay = "/pay/micropay"  # 退款查询

WX_URI.callback = "/jh/payment/wx/callback"

WX_URI.token = "/cgi-bin/token"
WX_URI.message = "/cgi-bin/message/wxopen/template/uniform_send"
# 获取openid
WX_URI.openid = '/sns/jscode2session'