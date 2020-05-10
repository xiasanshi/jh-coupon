#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/18 21:33
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : request.py
# @Software: PyCharm
# @Note    :
"""
import logging
import requests
from modules.lib.commen.typeasserts import typeassert
from modules.juhui.config.config import BaseConfig
from modules.juhui.model.base import JHBaseModel
from modules.juhui.execptions import JHException

_logger = logging.getLogger(__name__)
__author__ = "xialei"


@typeassert(config=BaseConfig, jh_model=JHBaseModel)
class JHRequest:
    def __init__(self, config, jh_model):
        config.init_check()
        self._model = jh_model
        self._wxconfig = config
        self._url = f"{config.HOST}{self._model.uri}"
        _logger.info(f"Requests url: {self._url}")

    def send_request_by_id(self, id):
        url = f"{self._url}/{id}"
        print(url)
        _logger.debug(f"Request url is {url}")
        r = requests.get(url, headers={'content-type': 'application/json'})
        if r.status_code == 200:
            return r.json()
        else:
            raise JHException(r.content)

    def query_by_shop_id(self, shop_id):
        url = f"{self._url}".replace('shop_id', shop_id)
        print(url)
        _logger.debug(f"Request url is {url}")
        r = requests.post(url, headers={'Content-Type': 'application/json'}, data=self._model.get_data)
        if r.status_code == 200:
            return r.json()
        else:
            raise JHException(r.content)

    def query(self):
        url = self._url.format(**self._model.get_data)
        _logger.debug(f"Request url is {url}")
        r = requests.post(url, headers={'Content-Type': 'application/json'}, verify=False)
        if r.status_code == 200:
            return r.json()
        else:
            raise JHException(r.content)

    def update(self):
        url = self._url
        _logger.debug(f"Request url is {url}")
        r = requests.put(url, headers={'content-type': 'application/json'}, data=self._model.get_json, verify=False)
        if r.status_code == 200:
            return r.json()
        else:
            raise JHException(r.content)
