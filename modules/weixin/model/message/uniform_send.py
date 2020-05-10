#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/7 17:00
@Site    : 
@File    : uniform_send.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import logging
from ..base import WXBaseModel
from modules.weixin.config.wx_const import WX_URI

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class WeAppTemplateMsg(WXBaseModel):
    field_list = ["template_id", "page", "form_id", "data", "emphasis_keyword"]


class WeMPTemplateMsg(WXBaseModel):
    field_list = ["template_id", "appid", "url", "miniprogram", "data"]


class UniFormSendModel(WXBaseModel):
    field_list = ["access_token", "touser", "weapp_template_msg", "mp_template_msg"]
    path = WX_URI.message

    def __init__(self, data):
        # data['weapp_template_msg'] = WeAppTemplateMsg(data['weapp_template_msg']).to_json()
        # data['mp_template_msg'] = WeMPTemplateMsg(data['mp_template_msg']).to_json()
        super(UniFormSendModel, self).__init__(data)


def main():
    INPUT = ''


if __name__ == '__main__':
    main()
