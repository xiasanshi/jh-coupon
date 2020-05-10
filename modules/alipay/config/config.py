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

from ..error import AliException

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class BaseConfig(object):
    # 开发者在线上或测试环境的app_key与app_secret是一样
    ACCESS_TOKEN = ""
    HOST = ""

    @classmethod
    def init_check(cls):
        if not cls.ACCESS_TOKEN:
            raise AliException("APP_KEY can not be empty, please assign a value")

        if not cls.HOST:
            raise AliException("host can not be empty, please assign a value")

        return True


class ALIConfig(BaseConfig):
    HOST = "https://openapi.alipay.com/gateway.do?"
    ACCESS_TOKEN = "Qw5h8nKMY5pV6mo9d4Ez0nfHO9Q10N11"


def main():
    pass


if __name__ == "__main__":
    main()
