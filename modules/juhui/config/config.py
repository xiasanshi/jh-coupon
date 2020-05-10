#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/9/18 21:21
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : config.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from ..execptions import JHException

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class BaseConfig(object):
    # 开发者在线上或测试环境的app_key与app_secret是一样
    ACCESS_TOKEN = ""
    HOST = ""

    @classmethod
    def init_check(cls):
        if not cls.ACCESS_TOKEN:
            raise JHException("APP_KEY can not be empty, please assign a value")

        if not cls.HOST:
            raise JHException("host can not be empty, please assign a value")

        return True


class JHOnlineConfig(BaseConfig):
    HOST = "https://www.fanzone.vip"
    # HOST = "http://173.17.1.6:6000"
    ACCESS_TOKEN = "Qw5h8nKMY5pV6mo9d4Ez0nfHO9Q10N11"


class JHProductConfig(JHOnlineConfig):
    HOST = "http://173.17.1.6:6000"


class JHMangerConfig(JHOnlineConfig):
    HOST = "http://173.17.1.1:6000"


class JHMemberConfig(JHOnlineConfig):
    HOST = "http://173.17.1.5:6000"


class JHMessageConfig(JHOnlineConfig):
    HOST = "http://173.17.1.8:6000"


class JHTestConfig(BaseConfig):
    HOST = "https://master.com"
    ACCESS_TOKEN = "Qw5h8nKMY5pV6mo9d4Ez0nfHO9Q10N11"


def create_config_factory(tag=None):
    # return JHOnlineConfig()
    if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV'] == 'production':
        if tag == 'product':
            return JHProductConfig()
        elif tag == 'manager':
            return JHMangerConfig()
        elif tag == 'member':
            return JHMemberConfig()
        elif tag == 'message':
            return JHMessageConfig()
        else:
            return JHOnlineConfig()
    return JHTestConfig()
