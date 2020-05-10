#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/10 14:57
@Site    : 
@File    : coupon.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import os
import logging
from flask import request

from flask_restplus import Namespace, fields, Resource

from modules.lib.commen.auths import require_login
# import modules.lib.commen.responser as resp
from modules.lib.commen.responser import Success
from modules.lib.emuns.coupon_enums import CouponStatusEnum, CouponTypeEnum
from modules.models.tb_coupon import TbCoupon

_logger = logging.getLogger(__name__)

coupon_api = Namespace('coupon', description="优惠券接口")

parser = coupon_api.parser()
parser.add_argument('Authorization', location='headers')

coupon_fields = coupon_api.model('CouponModel', {
    'name': fields.String(description='优惠券名称', required=True),
    'type': fields.String(description='优惠券类型', enum=list(CouponTypeEnum.__members__.keys())),
    'shop_id': fields.String(description='店铺id', required=True),
    'brand_id': fields.String(description='店铺id', required=True),
    'status': fields.String(description='优惠券状态', enum=list(CouponStatusEnum.__members__.keys()), required=True),
    'icon': fields.String(description='图片id'),
    'fee': fields.Integer(description='优惠券面值', required=True),
    'price': fields.Integer(description='优惠券售价'),
    'stock_total': fields.Integer(description='优惠券总数', required=True),
    'base_amount': fields.Integer(description='优惠券面值', required=True),
    'start_time': fields.DateTime(description='指定消费时间段开始'),
    'end_time': fields.DateTime(description='指定消费时间段结束'),
    'start_date': fields.DateTime(description='优惠券使用开始时间'),
    'end_date': fields.DateTime(description='优惠券使用结束时间')
})

query_fields = coupon_api.model('CouponQueryModel', {
    'shop_id': fields.String(description='店铺id', required=True),
    'brand_id': fields.String(description='店铺id', required=True),
    'status': fields.String(description='优惠券状态', enum=list(CouponStatusEnum.__members__.keys()), required=True),
    'page_size': fields.Integer(description='页大小'),
    'page_num': fields.Integer(description='页码'),
    'sort': fields.String(description='排序字段')
})


def check_product(resq_dict):
    page_size = resq_dict['page_size'] if 'page_size' in resq_dict else 20
    page_num = resq_dict['page_num'] if 'page_num' in resq_dict else 1
    sort_field = resq_dict['sort'] if 'sort' in resq_dict else "created_time"
    if sort_field not in CouponStatusEnum.__members__.keys():
        raise RuntimeError("非法的排序字段")
    return page_size, page_num, sort_field


@coupon_api.route('')
class CouponCreateResource(Resource):
    @coupon_api.expect(parser, coupon_fields, validate=True)
    @coupon_api.doc(description="创建优惠券")
    @Success.resp(code=201)
    def post(self):
        resq_dict = request.json
        resq_dict['stock'] = resq_dict['stock_total']
        TbCoupon.add(resq_dict)

    @coupon_api.expect(query_fields)
    @coupon_api.doc(description="查询优惠券", model=[coupon_fields])
    @Success.resp(code=200)
    def get(self):
        resq_dict = dict() if not request.json else request.json
        page_size = resq_dict['page_size'] if 'page_size' in resq_dict else 20
        page_num = resq_dict['page_num'] if 'page_num' in resq_dict else 1
        sort_field = resq_dict['sort'] if 'sort' in resq_dict else "created_time"
        query_dict = {}
        if "shop_id" in resq_dict:
            query_dict["shop_id"] = resq_dict['shop_id']
        if "brand_id" in resq_dict:
            query_dict["brand_id"] = resq_dict['brand_id']
        if "status" in resq_dict:
            query_dict["status"] = CouponStatusEnum.__members__[resq_dict['status'].value]
        results = TbCoupon.query.filter_by(**query_dict).order_by(
            sort_field).paginate(
            page_num, page_size, error_out=False)
        return results


@coupon_api.route('/<id>')
class CouponResourceById(Resource):
    @coupon_api.expect(parser, coupon_fields, validate=True)
    @coupon_api.doc(description="通过优惠券id修改优惠券")
    @Success.resp(code=201)
    def put(self, id):
        resq_dict = request.json
        resq_dict['id'] = id
        TbCoupon.update(resq_dict)

    @coupon_api.doc(description="通过优惠券id查询优惠券", model=coupon_fields)
    @Success.resp(code=200)
    def get(self, id):
        results = TbCoupon.query.filter_by(id=id).first()
        return results
