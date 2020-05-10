# _*_ coding: utf-8 _*_
"""
# @Time    : 2019/5/26 15:39
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : responser.py
# @Software: PyCharm
# @Note    :
"""
from flask import jsonify
from modules.lib.commen.error import APIException

from functools import wraps
import logging
from flask import jsonify
from flask_sqlalchemy import Pagination
from modules.lib.commen.error import APIException
from modules.models import JhModel

_logger = logging.getLogger(__name__)


class Success(APIException):
    code = 200
    error_code = 200
    data = None  # 结果可以是{} 或 []
    msg = '成功'

    def __init__(self, data=None, code=None, error_code=None, msg=None, **kwargs):
        """
        :param data: model object
        :param code:
        :param error_code: default 200
        :param msg:
        :param filter_fields: Fields not shown
        :param kwargs: Fields that need to be displayed outside of the model
        """
        if isinstance(data, JhModel):
            self.data = data.get_dict()
        self.data = data
        if code == 201:
            msg = msg if msg else '创建 | 更新成功'
        if code == 202:
            msg = msg if msg else '删除成功'

        super(Success, self).__init__(code, error_code, msg)

    def get_body(self, environ=None):
        body = dict(
            code=self.code,
            msg=self.msg,
            data=self.data
        )
        # text = json.dumps(body)  # 返回文本
        return jsonify(**body)

    @classmethod
    def resp(cls, code=None, error_code=None, msg=None):
        def decorate(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                r = func(*args, **kwargs)
                _logger.debug(f"Responce Data if {r}")
                if isinstance(r, Pagination):
                    res_dict = {
                        "results": [_.get_dict() for _ in r.items],
                        "pages": r.pages,
                        "next_num": r.next_num,
                        "has_next": r.has_next,
                        "prev_num": r.prev_num,
                        "total": r.total
                    }
                    r = res_dict
                elif isinstance(r, JhModel):
                    r = r.get_dict()
                return cls(data=r, code=code, error_code=error_code, msg=msg).get_body()

            return wrapper

        return decorate


class ClientTypeError(APIException):
    code = 400
    error_code = 1006
    msg = 'clinet is invalid'


class ServerError(APIException):
    code = 500
    error_code = 999
    msg = '服务器端异常'


class WeChatException(ServerError):
    code = 500
    error_code = 999
    msg = '微信服务器接口调用失败'


class ParameterException(APIException):
    code = 400
    error_code = 1000
    msg = 'invalid parameter'


class TokenException(APIException):
    code = 401
    error_code = 1001
    msg = 'Token已过期或无效Token'


class ForbiddenException(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = '签名错误'


class IllegalOperation(APIException):
    code = 401
    error_code = 1007
    msg = '非法操作'


class NotFound(APIException):
    code = 404  # http 状态码
    error_code = 1001  # 约定的异常码
    msg = '未查询到数据'  # 异常信息


class UserException(NotFound):
    code = 404
    error_code = 6000
    msg = '用户不存在'


class NoneUserIdException(NotFound):
    code = 404
    error_code = 6000
    msg = '用户id不存在'


class DuplicateException(APIException):
    code = 400
    error_code = 2001
    msg = '重复数据'


class ProductException(NotFound):
    code = 404
    error_code = 2000
    msg = '指定的商品不存在，请检查参数'


class ThemeException(NotFound):
    code = 404
    error_code = 3000
    msg = '请求的主题不存在，请检查主题ID'


class BannerMissException(NotFound):
    code = 404
    error_code = 4000
    msg = '请求的Banner不存在'


class CategoryException(NotFound):
    code = 404
    error_code = 5000
    msg = '指定的类目不存在, 请检查参数'


class UserException(NotFound):
    code = 404
    error_code = 6000
    msg = '用户不存在'


class OrderException(NotFound):
    code = 404
    error_code = 8000
    msg = '订单不存在，请检查ID'


class UploadException(NotFound):
    code = 500
    error_code = 9000
    msg = '文件上传失败'


class IllegalUploadException(UploadException):
    error_code = 9001
    msg = '非法的文件类型'


class UploadSizeException(UploadException):
    error_code = 9002
    msg = '文件大小超过限制，默认不能超过16Mb'


class ImgSizeException(UploadException):
    error_code = 9003
    msg = '图片大小超过限制，默认不能超过1Mb'
