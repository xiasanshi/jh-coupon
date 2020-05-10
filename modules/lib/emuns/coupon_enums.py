#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/5/10 13:50
@Site    : 
@File    : coupon_enums.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import os
import logging

__author__ = 'xialei'

from enum import Enum, unique

_logger = logging.getLogger(__name__)


@unique
class CouponStatusEnum(Enum):
    """
    ON(正在使用),OFF（不可使用）,ERROR（异常）
    """
    ON = "ON"
    OFF = "OFF"
    ERROR = "ERROR"


@unique
class CouponTypeEnum(Enum):
    """
    满减、立减、折扣券或优惠码
    """
    discount = "discount"
    reduction = "reduction"  # 红包


if __name__ == '__main__':
    l = [_.value for _ in CouponStatusEnum.__members__.values()]
    print(*l)
