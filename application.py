#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/5/26 15:39
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : application.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging
from flask import Flask, request
from flask_cors import CORS
from flask.logging import default_handler
from modules.apis import create_ns
from werkzeug.exceptions import HTTPException
from modules.lib.commen.error import APIException
from modules.lib.commen.cache import cache
from modules.lib.commen.responser import ServerError
from modules.models import db
import traceback

from celery import Celery

_logger = logging.getLogger(__name__)
__author__ = "xialei"


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def register_plugin(app):
    # 解决跨域问题
    cors = CORS()
    cors.init_app(app, resources={"/*": {"origins": "*"}})
    db.init_app(app)
    cache.init_app(app)
    with app.app_context():  # 手动将app推入栈
        db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表; 初始化使用


def create_app():
    app = Flask(__name__)
    app.logger.removeHandler(default_handler)
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s [%(thread)d] %(levelname)s [%(filename)s:%(lineno)d]-%(message)s")
    if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV'].lower() == 'production':
        app.config.from_object('modules.config.product')
    else:
        app.config.from_object('modules.config.local')
    apis = create_ns()
    for each in apis:
        app.register_blueprint(each)

    @app.after_request
    def after_request(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
        # response.headers.append('Access-Control-Allow-Credentials', 'true')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response

    @app.errorhandler(Exception)
    def framework_error(e):
        if isinstance(e, APIException):
            return e.get_body()
        elif isinstance(e, HTTPException):
            code = e.code
            msg = e.description
            error_code = 1007
            return APIException(code, error_code, msg).get_body()
        else:
            if "FLASK_ENV" in os.environ and os.environ['FLASK_ENV'] == 'production':
                return ServerError().get_body()
            return APIException(error_code=500, msg=str(e)).get_body()

    register_plugin(app)

    return app


def main():
    pass


if __name__ == "__main__":
    main()
