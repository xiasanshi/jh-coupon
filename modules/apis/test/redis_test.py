#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/12 9:27
@Site    : 
@File    : redis_test.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
from flask import request
from flask_restplus import Resource, Namespace, fields
from modules.lib.commen.cache import cache
from modules.lib.commen.responser import Success

__author__ = 'xialei'
_logger = logging.getLogger(__name__)

test_redis_api = Namespace('redis')

test_fields = test_redis_api.model('TestRedis', {
    'input': fields.String()
})


@cache.memoize(timeout=60, make_name='_cache')
def _cache(input_):
    _logger.info("test.....")
    return input_


@test_redis_api.route('')
class RedisTestApi(Resource):
    @test_redis_api.expect(test_fields)
    def post(self):
        resq_dict = request.json
        _logger.info(resq_dict)
        out = _cache(resq_dict.get('input'))
        return Success(data=out).get_body()
