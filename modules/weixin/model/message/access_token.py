#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/8 9:49
@Site    : 
@File    : access_token.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
from ..base import WXBaseModel
from modules.weixin.config.wx_const import WX_URI

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class AccessTokenModel(WXBaseModel):
    path = WX_URI.token

    def __init__(self):
        pass


def main():
    INPUT = ''


if __name__ == '__main__':
    main()
