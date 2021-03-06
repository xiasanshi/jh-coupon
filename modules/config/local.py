#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/5/21 21:54
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : local.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging

_logger = logging.getLogger(__name__)
__author__ = "xialei"
DEBUG = True
FLASK_DEBUG = 1

# JWT_AUTH_URL_RULE = '/auth'

# Token 配置
SECRET_KEY = 'But you, Lord , are a shield around me, my glory, the One who lifts my head high.'  # 加密
TOKEN_EXPIRATION = 30 * 24 * 3600  # 有效期: 30天

# MySQL 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENCODING = 'utf-8'
ROLE_SYS_LIST = ["SYS_USER", "BRAND_SYS_USER"]

DEFAULT_PASSWD = 'admin'
DEFAULT_BRAND_ROLE = '4'

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

DEFAULT_PASSWD = 'admin'
DEFAULT_BRAND_ROLE = '4'
# celery mq
# CELERY_BROKER_URL = 'amqp://admin:admin@192.168.71.133:5672/myvhost'
# CELERY_RESULT_BACKEND = 'amqp://'

# cache
CACHE_TYPE = "redis"
CACHE_REDIS_HOST = "47.92.109.217"
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 0
CACHE_REDIS_PASSWORD = "Qz000158!"
