#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/5/26 16:52
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : auths.py
# @Software: PyCharm
# @Note    :
"""
import jwt
from modules.config import local
from flask import g, request
from modules.lib.emuns.role_enums import ISAdminEnum, ISSystemEnum
from modules.lib import *
from functools import wraps
import datetime

_logger = logging.getLogger(__name__)


class Auth(object):
    @staticmethod
    def encode_auth_token(user_id, signature):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10, seconds=0),  # 过期时间10天
                'iat': datetime.datetime.utcnow(),
                'iss': 'xialei',
                'data': {
                    'id': user_id,
                    'signature': signature
                }
            }
            return jwt.encode(
                payload,
                local.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            # 是否取消过期时间验证 False 取消
            # payload = jwt.decode(auth_token, local.SECRET_KEY, options={'verify_exp': True})
            payload = jwt.decode(auth_token, local.SECRET_KEY, algorithms=['HS256'])
            if 'data' in payload and 'id' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    def identify(self):
        """
        用户鉴权
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token_arr = auth_header.split("#")
            if not auth_token_arr or auth_token_arr[0] != 'JWT' or len(auth_token_arr) != 2:
                _logger.debug('Illegal token')
                return AuthFailed()
            else:
                auth_token = auth_token_arr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    return payload
                else:
                    _logger.debug(payload)
                    return TokenException()
        else:
            _logger.debug('Illegal user')
            return ForbiddenException()


def require_login(check_brand=False, check_shop=False, check_admin=False, check_sys_user=False):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth = Auth()
            user_info = auth.identify()
            g.user_info = user_info
            role = user_info['data']['role']
            if check_admin:
                if not role or role.get('is_admin', '') != ISAdminEnum.yes.value:
                    raise IllegalOperation(msg="当前不是admin用户，操作不合法")
            if check_sys_user:
                if not role or role.get('is_sys_user', '') != ISSystemEnum.yes.value:
                    raise IllegalOperation(msg="当前不是系统用户，操作不合法")
            if check_brand:
                resq_dict = request.json
                if not (role and 'brand_id' in role and role['brand_id'] == resq_dict['brand_id']):
                    raise IllegalOperation()
            if check_shop:
                resq_dict = request.json
                if not (role and 'shop_id' in role and role['shop_id'] == resq_dict['shop_id']):
                    raise IllegalOperation()
            r = func(*args, **kwargs)
            return r

        return wrapper

    return decorate
