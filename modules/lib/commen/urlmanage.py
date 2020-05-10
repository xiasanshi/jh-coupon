#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/26 6:58
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : urlmanage.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from modules.lib.commen.conf import Config
from modules.lib import _basedir

# from application import create_app

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class UrlManage:
    def __init__(self):
        file_path = os.path.join(_basedir, '../../resources/conf.toml')
        conf = Config(config_path=file_path, propertys=['store_path', 'rout_path', 'name', 'ext'], keywords='file')
        self._conf_file = conf.get_config('file')

    @property
    def store_path(self):
        return self._conf_file.store_path

    @property
    def rout_path(self):
        return self._conf_file.rout_path

    @property
    def img_path(self):
        return "{}/images/".format(self._conf_file.store_path)

    @property
    def img_rout(self):
        return "{}/img/".format(self._conf_file.rout_path)

    @property
    def ext(self):
        return self._conf_file.ext


def main():
    pass


if __name__ == "__main__":
    main()
