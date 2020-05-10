# _*_ coding: utf-8 _*_
from flask import request, jsonify
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = '服务器未知错误'
    error_code = 999

    def __init__(self, code=None, error_code=None, msg=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__()

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            code=self.code,
            data={"error_code": self.error_code}
        )
        # text = json.dumps(body)  # 返回文本
        text = jsonify(**body)
        return text

    def get_headers(self, environ=None):
        return [('Content-type', 'application/json; charset=utf-8')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')[0]
        return main_path
