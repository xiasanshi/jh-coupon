#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/7/21 10:49
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : notify.py
# @Software: PyCharm
# @Note    :
"""
import sys
import logging
import time
import os
from concurrent.futures import ThreadPoolExecutor

try:
    import urlparse
except:
    import urllib.parse as urlparse

try:
    import toml
except ImportError:
    print("ERROR: Module 'toml' import error, please install by: \n\tpip install toml")
    sys.exit(1)
try:
    import pika
except ImportError:
    print("ERROR: Module 'pika' import error, please install by: \n\tpip install pika")
    sys.exit(1)

_logger = logging.getLogger(__name__)


class MQTask(object):
    def __init__(self, url, routingkey, exchange="gcsasExchange"):
        self._uri = "amqp://{}/%2F".format(url)
        self._exchange = exchange
        self._routingkey = routingkey

    def send_message(self, message):
        _logger.debug("RabbitMQ paramters: (uri: %s, exchange: %s, routingkey: %s)" % (
            self._uri, self._exchange, self._routingkey))
        _logger.info("MESSAGE: %s" % message)
        params = pika.URLParameters(self._uri)
        params.heartbeat = 10
        params.connection_attempts = 3
        params.retry_delay = 1
        params.blocked_connection_timeout = 10

        connection = pika.BlockingConnection(params)

        channel = connection.channel()

        _logger.debug("RabbitMQ connected.")

        channel.basic_publish(self._exchange, self._routingkey, message,
                              pika.BasicProperties(content_type='application/json',
                                                   content_encoding='UTF-8'))
        connection.close()
        _logger.info(f"Callback successful({message})")
        return True

    def send_asyc_message(self, message):
        _logger.info(f"Callback data: {message}")
        exec = ThreadPoolExecutor(128)
        exec.submit(self.send_message, message)


def mq_factory():
    if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV'].lower() == 'production':
        _logger.info('product envroment; mq url 39.98.203.73:5672')
        mq = MQTask('admin:admin@39.98.203.73:5672', routingkey='deliveryBackRoutingKey', exchange='fruitExchange')
    else:
        _logger.info('development envroment; mq url 192.168.71.133:5672')
        mq = MQTask('admin:admin@192.168.71.133:5672', routingkey='deliveryBackRoutingKey', exchange='fruitExchange')
    return mq


if __name__ == '__main__':
    mq = MQTask('admin:admin@192.168.71.133:5672', routingkey='deliveryBackRoutingKey', exchange='fruitExchange')
    # mq = MQTask('admin:admin@39.98.203.73:5672', routingkey='deliveryBackRoutingKey', exchange='fruitExchange')
    mq.send_message('sss')
    print('doner')
