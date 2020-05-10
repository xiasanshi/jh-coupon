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
from modules.weixin import RequestError
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
class WxMessageRequest:
    def __init__(self, model, wx_config):
        wx_config.init_check()
        self._model = model
        self._wxconfig = wx_config
        self._url = f"{wx_config.HOST}{self._model.path}"
        _logger.info(f"Requests url: {self._url}")

    def option_request(self, access_token, with_ca=False):
        """
        发送https请求，也可以带证书
        Args:
            url(str): 请求地址
            xml_str(str): 格式为xml类型的字符串
            with_ca: 是否带证书

        Returns:
            返回字典形式的请求响应内容

        """

        jsonp = self._model.to_json()
        _logger.debug(f"json: {jsonp}")
        if with_ca:
            res = requests.post(f"{self._url}?access_token={access_token}",
                                data=json.dumps(jsonp, ensure_ascii=False).encode('utf8'),
                                cert=(self.API_CLIENT_CERT_PATH, self.API_CLIENT_KEY_PATH))
        else:
            res = requests.post(f"{self._url}?access_token={access_token}",
                                data=jsonp)

        if res.status_code != 200:
            raise RequestError(f"Error code: {res.status_code},Error message: {res.content}")
        res_content_dict = json.loads(res.content)

        return res_content_dict

    def get_access_token(self, appid, secret):
        """
        https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
        :return:
        """
        uri = f"{self._url}?grant_type=client_credential&appid={appid}&secret={secret}"
        _logger.debug(f"Request access token uri is {uri}")
        r = requests.get(uri)
        _logger.debug(r.content)

        if r.status_code != 200:
            raise RequestError(f"Error code: {r.status_code},Error message: {r.content}")
        res_content_dict = json.loads(r.content)

        return res_content_dict

    @staticmethod
    def to_dict(content):
        raw = {}
        root = ETree.fromstring(content)
        for child in root:
            raw[child.tag] = child.text
        return raw


def main():
    from modules.weixin.config.config import WXConfig
    data = {
        "touser": "oYJ1d5S1Jh0XE5mwLT_htCHuK1b8",
        "weapp_template_msg": {
            "template_id": "yHM5yWK-3ixkcQOIUGwGxZSWUbZ8PubF7zjQpD73ot8",
            "page": "page/index/index",
            "form_id": "18082da57f0c4038b35ae496f13bdf18",
            "data": {
                "keyword1": {
                    "value": "339208499"
                },
                "keyword2": {
                    "value": "2015年01月05日 12:30"
                },
                "keyword3": {
                    "value": "腾讯微信总部"
                }
            },
            "emphasis_keyword": "keyword1.DATA"
        },
        "mp_template_msg": {
            "appid": "APPID ",
            "template_id": "TEMPLATE_ID",
            "url": "http://weixin.qq.com/download",
            "miniprogram": {
                "appid": "xiaochengxuappid12345",
                "pagepath": "index?foo=bar"
            },
            "data": {
                "first": {
                    "value": "恭喜你购买成功！",
                    "color": "#173177"
                },
                "keyword1": {
                    "value": "巧克力",
                    "color": "#173177"
                },
                "keyword2": {
                    "value": "39.8元",
                    "color": "#173177"
                },
                "keyword3": {
                    "value": "2014年9月22日",
                    "color": "#173177"
                },
                "remark": {
                    "value": "欢迎再次购买！",
                    "color": "#173177"
                }
            }
        }
    }
    # access_token = "25_mL7zqw2M9LTowwqX3nmUIxDUZGE_X3v55V3VBgfTouAZ7WJNl8-hRHXCbAC1KcGnn63odIGdgNwl2QeyYvemkyOgj-r18RemH7n4b93_SBgWtSTAaXstiJbr6aBOxInEVVLEqMpT1WZBjO2lCYLdAAAIER"
    # data["access_token"] = access_token
    # print(json.dumps(data))
    # order = UniFormSendModel(data)
    # wx_request = WxMessageRequest(model=order, wx_config=WXConfig())
    # print(wx_request.option_request(access_token))
    from modules.weixin.model.message import AccessTokenModel
    wx_request = WxMessageRequest(model=AccessTokenModel(), wx_config=WXConfig())
    data = {'appid': 'wx4b4764b837a57863',
            "secret": "96ac3cd638ffe5c85f8d7deb4e9bbb71"
            }
    print(wx_request.get_access_token(**data))


if __name__ == "__main__":
    main()
