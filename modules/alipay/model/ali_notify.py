#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019.12.1
# @Author  :
# @Email   :
# @File    : notify.py
# @Software: PyCharm
# @Note    :
"""
import logging
from ..model.base import AliBaseModel

_logger = logging.getLogger(__name__)


class AliNotify(AliBaseModel):
    field_list = ["code", "msg"]
