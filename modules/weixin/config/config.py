#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/2 21:39
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : config.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from builtins import object

from ..error import WXException

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class BaseConfig(object):
    # 开发者在线上或测试环境的app_key与app_secret是一样
    ACCESS_TOKEN = ""
    HOST = ""

    @classmethod
    def init_check(cls):
        if not cls.ACCESS_TOKEN:
            raise WXException("APP_KEY can not be empty, please assign a value")

        if not cls.HOST:
            raise WXException("host can not be empty, please assign a value")

        return True


class WXConfig(BaseConfig):
    HOST = "https://api.weixin.qq.com"
    ACCESS_TOKEN = "*************"


def main():
    pass


if __name__ == "__main__":
    main()
