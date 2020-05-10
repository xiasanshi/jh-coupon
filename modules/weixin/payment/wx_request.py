#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/2 20:31
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : wx_request.py
# @Software: PyCharm
# @Note    :
"""
import logging
import requests
from modules.weixin.model.base import WXBaseModel
from modules.weixin.config.config import BaseConfig
from modules.lib import typeassert
import json

try:
    from xml.etree import cElementTree as ETree
except ImportError:
    from xml.etree import ElementTree as ETree

_logger = logging.getLogger(__name__)
__author__ = "xialei"


@typeassert(model=WXBaseModel, wx_config=BaseConfig)
class WRequest:
    def __init__(self, model, wx_config):
        wx_config.init_check()
        self._model = model
        self._wxconfig = wx_config
        self._url = f"{wx_config.HOST}{self._model.path}"
        _logger.info(f"Requests url: {self._url}")

    def option_request(self, with_ca=False):
        """
        发送https请求，也可以带证书
        Args:
            url(str): 请求地址
            xml_str(str): 格式为xml类型的字符串
            with_ca: 是否带证书

        Returns:
            返回字典形式的请求响应内容

        """

        xml = self._model.dict2xml(self._wxconfig.APP_KEY)
        _logger.debug(f"XML: {xml}")
        if with_ca:
            res = requests.post(self._url,
                                data=json.dumps(xml, ensure_ascii=False).encode('utf8'),
                                cert=(self.API_CLIENT_CERT_PATH, self.API_CLIENT_KEY_PATH))
        else:
            res = requests.post(self._url,
                                data=xml)

        res_content_dict = self._model.xml2dict(res.content)

        return res_content_dict

    @staticmethod
    def to_dict(content):
        raw = {}
        root = ETree.fromstring(content)
        for child in root:
            raw[child.tag] = child.text
        return raw


def main():
    from modules.weixin.model.payment import OrderModel
    from modules.weixin.config.config import PAYConfig
    data = {'appid': 'wx95721d88a471e1d1',
            'mch_id': '1493595992',
            'sub_appid': '',
            'sub_mch_id': '1517807851',
            'device_info': 'WEB',
            'receipt': 'Y',
            'auth_code': '13484923',
            'body': 'JSAPI支付测试',
            'detail': {"goods_detail": [
                {"goods_id": "iphone6s_16G", "wxpay_goods_id": "1001", "goods_name": "iPhone6s 16G", "quantity": 1,
                 "price": 528800, "goods_category": "123456", "body": "苹果手机"}]},
            'attach': '支付测试',
            'out_trade_no': '141565991',
            'total_fee': '0.01',
            'spbill_create_ip': '47.97.115.141',
            'trade_type': 'JSAPI',
            'product_id': '',
            'openid': 'oeeRzxLaCin4AcZ5_K7ie7S5KPng',
            'sub_openid': ''}

    print(json.dumps(data))
    order = OrderModel(data)
    wx_request = WRequest(model=order, wx_config=PAYConfig())
    print(wx_request.option_request())


if __name__ == "__main__":
    main()
