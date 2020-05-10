#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/29 21:47
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : unifiedorder.py
# @Software: PyCharm
# @Note    : 微信支付 统一下单 trade_type （类型）
#            JSAPI -JSAPI支付/小程序支付
#
#            NATIVE -Native支付
#
#            APP -APP支付
"""
import logging
from modules.weixin.model.base import WXBaseModel
from modules.weixin.config.wx_const import WX_URI

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class OrderModel(WXBaseModel):
    field_list = ["appid", "mch_id", "sub_appid", "sub_mch_id", "device_info", "receipt", "body", "detail", "attach",
                  "out_trade_no", "total_fee", "spbill_create_ip", "notify_url", "trade_type", "product_id", "openid",
                  "sub_openid"]
    path = WX_URI.unifiedorder

    def __init__(self, data):
        if 'total_fee' in data:
            data['total_fee'] = int(float(data['total_fee']) * 100)  # 微信支付金额单位为分
        super(OrderModel, self).__init__(data)


def main():
    data = {'appid': 'wx2421b1c4370ec43b',
            'mch_id': '10000100',
            'sub_appid': '',
            'sub_mch_id': '',
            'device_info': 'WEB',
            'receipt': 'Y',
            'body': 'JSAPI支付测试',
            'detail': {"goods_detail": [
                {"goods_id": "iphone6s_16G", "wxpay_goods_id": "1001", "goods_name": "iPhone6s 16G", "quantity": 1,
                 "price": 528800, "goods_category": "123456", "body": "苹果手机"},
                {"goods_id": "iphone6s_32G", "wxpay_goods_id": "1002", "goods_name": "iPhone6s 32G", "quantity": 1,
                 "price": 608800, "goods_category": "123789", "body": "苹果手机"}]},
            'attach': '支付测试',
            'out_trade_no': '141565999',
            'total_fee': 1,
            'spbill_create_ip': '47.97.115.141',
            'notify_url': 'http://wxpay.wxutil.com/pub_v2/pay/notify.v2.php',
            'trade_type': 'JSAPI',
            'product_id': '',
            'openid': 'oUpF8uMuAJO_M2pxb1Q9zNjWeS6o',
            'sub_openid': ''}

    a = OrderModel(data=data)
    print(a.dict2xml())


if __name__ == "__main__":
    main()
