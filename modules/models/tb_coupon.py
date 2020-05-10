#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/10 12:34
@Site    : 
@File    : tb_coupon.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import os
import logging
from sqlalchemy import func

from modules.lib.emuns.coupon_enums import CouponStatusEnum, CouponTypeEnum
from modules.models import db, JhModel

__author__ = 'xialei'
_logger = logging.getLogger(__name__)

"""
base_amount  最低可用消费金额
start_time 可用时间段开始
end_time  可用时间段结束
start_date  使用有效期开始
end_date    使用有效期结束
"""

status = [_.value for _ in CouponStatusEnum.__members__.values()]
types = [_.value for _ in CouponTypeEnum.__members__.values()]


class TbCoupon(db.Model, JhModel):
    __tablename__ = 'tb_coupon'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    shop_id = db.Column(db.String(64), nullable=False)  # 指定品牌
    brand_id = db.Column(db.String(64), nullable=False)  # 指定商家
    status = db.Column(db.Enum(*status))
    coupon_type = db.Column(db.Enum(*types))
    icon = db.Column(db.String(64))
    fee = db.Column(db.Integer, nullable=False)  # 金额 单位分
    price = db.Column(db.Integer, default=0, nullable=False)  # 售卖金额 单位分
    stock = db.Column(db.Integer, nullable=False)  # 当前库存
    stock_total = db.Column(db.Integer, nullable=False)  # 总数量
    desc = db.Column(db.Text)  # 优惠券描述
    note = db.Column(db.String(256))  # 优惠券备注
    base_amount = db.Column(db.Integer, nullable=False)  # 最低消费金额
    start_time = db.Column(db.DateTime, nullable=False, default=func.now())  # 可用时间段开始
    end_time = db.Column(db.DateTime, nullable=False)  # 可用时间段结束
    start_date = db.Column(db.DateTime, nullable=False, default=func.now())  # 使用有效期开始
    end_date = db.Column(db.DateTime, nullable=False)  # 使用有效期结束
    created_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now())


def main():
    INPUT = ''


if __name__ == '__main__':
    main()
