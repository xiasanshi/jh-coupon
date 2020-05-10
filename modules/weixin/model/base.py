#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/29 21:10
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : base.py
# @Software: PyCharm
# @Note    :
"""
import logging
import json
import hashlib

import string
import random

try:
    from xml.etree import cElementTree as ETree
except ImportError:
    from xml.etree import ElementTree as ETree

from modules.weixin import WXException

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class WXBaseModel:
    field_list = []
    path = ''

    def __init__(self, data, is_compatible=False):
        if not isinstance(data, dict):
            raise WXException("Error type of data,")
        self._data = data
        self.is_compatible = is_compatible
        self.field_check()

    def field_check(self):
        for each in WXBaseModel.field_list:
            if each not in self._data:
                raise WXException(f"Missing the necessary parameters {each}")

    def dict2xml(self, key=None):
        self.create_nonce_str()
        self.create_sign(key)
        request_xml_str = '<xml>'
        for key, value in self._data.items():
            if not self.is_compatible and not value: continue
            if key == 'detail':
                request_xml_str = f'{request_xml_str}<{key}><![CDATA[{json.dumps(value)}]]></{key}>'
            else:
                request_xml_str = f'{request_xml_str}<{key}>{value}</{key}>'
        request_xml_str = '%s</xml>' % request_xml_str

        return request_xml_str.encode("utf-8")

    def to_json(self):
        return json.dumps(self._data)

    def create_sign(self, key):
        # raw = [(k, str(self._data[k]) if isinstance(self._data[k], (int, float)) else self._data[k]) for k in
        #        sorted(self._data.keys())]
        raw = []
        for k, v in sorted(self._data.items(), key=lambda e: e[0], reverse=False):
            if isinstance(self._data[k], str):
                raw.append((k, self._data[k]))
            elif isinstance(self._data[k], (int, float)):
                raw.append((k, str(self._data[k])))
            else:
                raw.append((k, json.dumps(self._data[k])))

        if self.is_compatible:
            s = "&".join("=".join(kv) for kv in raw)
        else:
            s = "&".join("=".join(kv) for kv in raw if kv[1])
        s += "&key={0}".format(key)
        s = s.encode('utf8')
        self._data['sign'] = hashlib.md5(
            s).hexdigest().upper()

    def create_nonce_str(self, length=32):
        '''

        Args:
            length(int): 随机数的长度

        Returns:
            返回length长度的随机字符串

        '''
        char = string.ascii_letters + string.digits
        self._data['nonce_str'] = "".join(random.choice(char) for _ in range(length))

    def xml2dict(self, content):
        raw = {}
        root = ETree.fromstring(content)
        for child in root:
            raw[child.tag] = child.text
        return raw

    def json2dict(self, content):
        return json.loads(content)
