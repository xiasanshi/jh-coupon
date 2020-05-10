#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/11/27 10:32
@Site    : 
@File    : goods_detail.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
from modules.alipay.model.base import AliBaseModel

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class GoodsDetailModel(AliBaseModel):
    field_list = ['goods_id', 'goods_name', 'quantity', 'price']

    @classmethod
    def create_model_factory(cls, data, tag=None, **kwargs):
        if tag == 'create':
            field_list = ['goods_id', 'goods_name', 'quantity', 'price']
        elif tag == 'test':
            field_list = []
        else:
            field_list = cls.field_list
        field_list.extend(kwargs.keys())
        data.update(kwargs)
        cls.field_list = field_list
        return cls(data)


def main():
    INPUT = {"name": 1}
    a = GoodsDetailModel.create_model_factory(INPUT, tag='test', **INPUT)
    print(a)
    print(a.dump_sort_data)


if __name__ == '__main__':
    main()
