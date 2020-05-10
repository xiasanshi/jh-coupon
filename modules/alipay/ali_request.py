#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/11/13 19:24
@Site    :
@File    : ali_request.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import json
import logging
import time
import requests
from modules.alipay.error import RequestError
from modules.alipay.model.base import AliBaseModel
from modules.alipay.config.config import ALIConfig
from modules.lib.commen.typeasserts import typeassert

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


@typeassert(config=ALIConfig, model=AliBaseModel)
class AliRequest:
    def __init__(self, config, model):
        config.init_check()
        self._model = model
        self._config = config
        self._url = f"{config.HOST}"
        _logger.info(f"Requests url: {self._url}")

    def get_request(self, with_ca=False):
        jsonp = self._model.dict_data
        _logger.debug(f"json: {jsonp}")
        if with_ca:
            res = requests.post(f"{self._url}",
                                data=jsonp)
        else:
            res = requests.post(f"{self._url}", data=jsonp)
            # data = parse.urlencode(jsonp)
            # res = request.urlopen(self._url, data=data.encode('utf-8')).read()

        if res.status_code != 200:
            raise RequestError(f"Error code: {res.status_code},Error message: {res.content}")
        res_content_dict = json.loads(res.content.decode("gbk"))
        _logger.info(f"ali response data is {res_content_dict}")
        return res_content_dict


def main():
    from datetime import datetime
    from modules.alipay.model.payment.pay_model import AliPayCreateModel
    from modules.alipay.model.biz_content import BizContentModel
    from modules.alipay.config.config import ALIConfig
    d = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    out_trade_no = str(int(time.time())) + '78966'
    biz_content = BizContentModel.create_model_factory({
        'out_trade_no': out_trade_no,
        'subject': '123',
        'total_amount': 0.01,
        'buyer_id': '2088902141310971'
    }, tag='create')
    data = {'app_id': '2019111969288384',
            'method': 'alipay.trade.create',
            'charset': 'utf-8',
            'sign_type': 'RSA2',
            'timestamp': d,
            'version': '1.0',
            'biz_content': biz_content
            }
    r = AliRequest(ALIConfig(), AliPayCreateModel(data))
    print(r.get_request())


if __name__ == '__main__':
    main()
