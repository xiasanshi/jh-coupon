#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/6/13 21:49
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : const.py
# @Software: PyCharm
# @Note    :
"""
import os
import logging

_logger = logging.getLogger(__name__)
__author__ = "xialei"


class ConstError(TypeError): pass


class Const:
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ConstError("Constant unmodifiable")
        self.__dict__[key] = value


# Brand status

BRAND_STATUS = Const()
BRAND_STATUS.ON_SALE = "onSale"
BRAND_STATUS.OFF_SALE = "offSale"

# shop status
SHOP_STATUS = Const()
SHOP_STATUS.ON_SALE = "onSale"
SHOP_STATUS.OFF_SALE = "offSale"

# shop operate
SHOP_OPERATE = Const()
SHOP_OPERATE.OPEN = "OPEN"
SHOP_OPERATE.CLOSE = "CLOSE"

# user sex
USER_SEX = Const()
USER_SEX.MALE = "male"  # 男
USER_SEX.FEMALE = "female"  # 女
USER_SEX.UNKOWN = "unkown"

# user status
USER_STATUS = Const()
USER_STATUS.VALID = 1  # 是
USER_STATUS.INVALID = 0

# role
ROLE_IS_SYS_USER = Const()
ROLE_IS_SYS_USER.TRUE = 1  # 是
ROLE_IS_SYS_USER.FALSE = 0  # 是

# role 管理员
ROLE_IS_ADMIN = Const()
ROLE_IS_ADMIN.TRUE = "YES"
ROLE_IS_ADMIN.FALSE = "NO"

# classify status
CLASSIFY_STATUS = Const()
CLASSIFY_STATUS.ON = "ON"  # 使用中
CLASSIFY_STATUS.OFF = "OFF"  # 废弃

# product status
PRODUCT_STATUS = Const()
PRODUCT_STATUS.ON = "ON_SELL"  # 使用中
PRODUCT_STATUS.OFF = "OUT_SELL"  # 废弃

# secondary classify status
S_CLASSIFY_STATUS = Const()
S_CLASSIFY_STATUS.ON = "ON"  # 使用中
S_CLASSIFY_STATUS.OFF = "OFF"  # 废弃

# delivery status
D_STATUS = Const()
D_STATUS.WAIT_SHIP = 0  # 待发货
D_STATUS.WAIT_RECV = 1  # 待接单
D_STATUS.WAIT_CARRY = 2  # 待取货
D_STATUS.IN_DIST = 3  # 配送中
D_STATUS.COMPLETE = 4  # 完成
D_STATUS.CANCEL = 5  # 取消
D_STATUS.EXPIRE = 7  # 过期
D_STATUS.ASSIGN = 8  # 指派单
D_STATUS.ABNO_IN_BACK = 9  # 妥投异常之物品返回中
D_STATUS.ABNO_BACK_SUCC = 10  # 妥投异常之物品返回完成
D_STATUS.RIDER_IN_SHOP = 100  # 骑士到店
D_STATUS.CREATE_FIAL = 1000  # 创建达达运单失败

ORDER_STATUS_DICT = {
    0: 'noShipping',
    1: 'prepareShipping',
    2: 'alreadyShipping',
    1000: 'exception',
    4: 'complete',
    5: 'exception',
    7: 'exception'
}
'''
商家待接单("wait","商家待接单"),
    商家已拒单("reject","商家已拒单"),
    未发货("noShipping","未发货"),
    待配送("prepareShipping","待配送"),
    已发货("alreadyShipping","已发货"),
    异常("exception","订单异常"),
    完成("complete","完成"),
'''
