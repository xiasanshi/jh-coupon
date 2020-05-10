#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/7 9:54
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : micropay.py
# @Software: PyCharm
# @Note    :
"""
import logging

_logger = logging.getLogger(__name__)
__author__ = "xialei"

import logging
from modules.weixin.model.base import WXBaseModel
from modules.weixin.config.wx_const import WX_URI

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class OrderModel(WXBaseModel):
    field_list = ["appid", "mch_id", "sub_appid", "sub_mch_id", "device_info", "receipt", "body", "detail", "attach",
                  "out_trade_no", "total_fee", "spbill_create_ip", "product_id", "auth_code"]
    path = WX_URI.micropay

    def __init__(self, data):
        if 'total_fee' in data:
            data['total_fee'] = int(float(data['total_fee']) * 100)  # 微信支付金额单位为分
        super(OrderModel, self).__init__(data)


def main():
    pass


if __name__ == "__main__":
    main()
