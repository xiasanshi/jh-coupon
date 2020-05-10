#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/9 11:12
@Site    : 
@File    : __init__.py.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import copy
import datetime
import decimal
import json
import logging
from modules.lib.utils import is_number
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()  # 事务
        except Exception as e:
            self.session.rollback()  # 回滚
            raise e

    @contextmanager
    def auto_check_empty(self, e):
        try:
            yield
        except Exception:
            raise e


db = SQLAlchemy()


class JhModel:
    def get_dict(self):
        t = copy.deepcopy(self.__dict__)
        return self.format_json(t)

    @classmethod
    def format_json(cls, tmp_dict, filter_fields=None):
        filter_fields = filter_fields if filter_fields is not None else []
        if '_sa_instance_state' in tmp_dict:
            del tmp_dict['_sa_instance_state']
        filter_fields.extend(['login_pwd', 'login_salt'])
        res_dict = {}
        for k, v in tmp_dict.items():
            if k in filter_fields:
                continue
            elif isinstance(v, decimal.Decimal):
                res_dict[k] = float(v)
            elif isinstance(v, datetime.datetime):
                res_dict[k] = v.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(v, datetime.date):
                res_dict[k] = v.strftime("%Y-%m-%d")
            elif isinstance(v, datetime.timedelta):
                res_dict[k] = (datetime.datetime.today() + v).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(v, JhModel):
                res_dict[k] = v.get_dict
            elif isinstance(v, list):
                res_dict[k] = [_.get_dict for _ in v]
            else:
                res_dict[k] = v
        return res_dict

    @classmethod
    def add(cls, info):
        model = cls._deal_with_model(info, cls())
        with db.auto_commit():
            db.session.add(model)

    @classmethod
    def update(cls, info):
        model = cls.query.filter_by(id=info['id']).first()
        if not model:
            raise RuntimeError("指定id不存在")
        with db.auto_commit():
            cls._deal_with_model(info, model)

    @staticmethod
    def _deal_with_model(info, model):
        for k, v in info.items():
            if k.endswith('_time') or k.endswith('_date'):
                # v = v.replace("T"," ")
                if 'T' in v:
                    v = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%fZ')
                elif is_number(v):
                    v = float(v) / 1000
                    v = datetime.datetime.fromtimestamp(v)
                else:
                    try:
                        v = datetime.datetime.strptime(v, '%Y-%m-%d %H:%M:%S')
                    except Exception as e:
                        raise RuntimeError("unknow date format {}".format(v)) from e
            if isinstance(v, dict):
                v = json.dumps(v)
            setattr(model, k, v)
        return model


if __name__ == '__main__':
    pass
