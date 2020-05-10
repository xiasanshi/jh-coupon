#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/12/18 16:39
@Site    :
@File    : conf.py
@Software: PyCharm
@Author  : xialei
@Email: xialei@gcbi.com.cn
'''
import os
import logging
import sys
from collections import namedtuple

try:
    import toml
except ImportError:
    print("ERROR: Module 'toml' import error, please install by: \n\tpip install toml")
    sys.exit(1)

__author__ = 'xialei'
_basedir = os.path.dirname(__file__)
_logger = logging.getLogger(__name__)


class Config(object):
    def __init__(self, propertys, config_path=None, keywords='database'):
        '''
        :param propertys: The list of parameters you want to get
        :param base:
        :param config: path of conf file
        '''
        self.__config = config_path
        # load configuration from toml
        config = toml.load(self.__config)
        self.__databases = {}
        if "name" not in propertys:
            raise RuntimeError("Miss nessary property 'name'")
        Database = namedtuple('Database', propertys)
        # print(config)
        for conf in config:
            if conf == keywords:
                for db in config[keywords]:
                    db = {i: db.get(i, None) for i in propertys}
                    p = Database(**db)
                    self.__databases[p.name] = p

    def has_config(self, name):
        if name not in self.__databases:
            return False
        return True

    def get_config(self, name):
        if name not in self.__databases:
            raise SyntaxError("ERROR: database '%s' no found." % (name))
        return self.__databases[name]

    @property
    def configs(self):
        return self.__databases


def main():
    prolist = ['name', 'map', 'operation']
    conf = Config(config_path="../conf/annovar.conf", propertys=prolist, keywords='annovardb')
    print(conf.configs)


if __name__ == '__main__':
    main()
