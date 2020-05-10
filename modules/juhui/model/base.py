#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/18 21:27
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : base.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
import json
from ..execptions import JHException

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class JHBaseModel:
    fields = []
    uri = ''

    def __init__(self, data):
        self._data = data
        self.field_check()

    def field_check(self):
        for each in JHBaseModel.fields:
            if each not in self._data:
                raise JHException(f"Missing the necessary parameters {each}")

    @property
    def get_json(self):
        return json.dumps(self._data)

    @property
    def get_data(self):
        return self._data

    @property
    def uri(self):
        return JHBaseModel.uri


def main():
    pass


if __name__ == "__main__":
    main()
