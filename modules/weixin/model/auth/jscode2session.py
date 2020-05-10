#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/15 15:56
@Site    : 
@File    : jscode2session.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
from modules.weixin.config.wx_const import WX_URI
from ..base import WXBaseModel

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class Jscode2sessionModel(WXBaseModel):
    path = WX_URI.openid

    def __init__(self):
        pass


def main():
    INPUT = ''


if __name__ == '__main__':
    main()
