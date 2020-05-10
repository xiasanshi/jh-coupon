#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/2 21:10
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : notify.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from ..base import WXBaseModel

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class WXNotify(WXBaseModel):
    field_list = ["return_code", "return_message"]

    def dict2xml(self):
        request_xml_str = '<xml>'
        for key, value in self._data.items():
            if not self.is_compatible and not value: continue
            request_xml_str = f'{request_xml_str}<{key}><![CDATA[{value}]]></{key}>'
        request_xml_str = '%s</xml>' % request_xml_str
        return request_xml_str


def main():
    pass


if __name__ == "__main__":
    main()
