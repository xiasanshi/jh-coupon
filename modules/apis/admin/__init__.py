#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/9 11:18
@Site    : 
@File    : __init__.py.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
import traceback

from flask import Blueprint, url_for
from flask_restplus import Api
from .coupon import coupon_api
import os

from ...lib.commen.responser import ServerError

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class MyApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = 'http' if '6000' in self.base_url or '5010' in self.base_url else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)


def create_ns():
    admin_blueprint = Blueprint('admin', __name__, url_prefix="/jh/coupon/admin")
    api = MyApi(admin_blueprint, version="1.0", prefix="", catch_all_404s=False, title='聚汇优惠券api',
                description='聚汇优惠券平台api')

    @api.errorhandler(Exception)
    def error(e):
        _logger.error(traceback.format_exc())
        raise e

    api.add_namespace(coupon_api)

    return admin_blueprint
