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

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class MyApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = 'http' if '6000' in self.base_url or '5000' in self.base_url else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)


def create_ns():
    api_blueprint = Blueprint('api', __name__, url_prefix="/jh/coupon")
    api = MyApi(api_blueprint, version="1.0", prefix="", catch_all_404s=False)

    @api.errorhandler(Exception)
    def error(e):
        _logger.error(traceback.format_exc())
        raise e

    return api_blueprint
