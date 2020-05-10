#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/29 21:10
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : base.py
# @Software: PyCharm
# @Note    :
"""
import logging
import json
import os
import OpenSSL
import hashlib
from base64 import b64encode
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from modules.alipay.error import AliException
from modules.alipay import basedir
from modules.lib.commen.conf import Config

_logger = logging.getLogger(__name__)
__author__ = "xialei"


# 请求数据封装的model
class AliBaseModel:
    field_list = []
    method = ""

    def __init__(self, data):
        file_path = os.path.join(basedir, '../resources/conf.toml')
        conf = Config(config_path=file_path,
                      propertys=['public_key_path', 'private_key_path', 'name',
                                 'app_private_key_path', 'app_cert_public_key_path',
                                 'alipay_root_cert_path'],
                      keywords='alipay')
        self._conf_file = conf.get_config('key')
        if not isinstance(data, dict):
            raise AliException("Error type of data")
        self._requests_data = data
        self._data = dict()
        self.field_check()

    @classmethod
    def create_model_factory(cls, data, tag=None, **kwargs):
        """
        用于非必要参数时实例化对象
        :param data:
        :param tag:
        :param kwargs: 额外的非必要参数
        :return:
        """
        field_list = cls.field_list
        field_list.extend(kwargs.keys())
        data.update(kwargs)
        cls.field_list = field_list
        return cls(data)

    @staticmethod
    def _sort(params):
        return dict(sorted(params.items(), key=lambda e: e[0], reverse=False))

    def field_check(self):
        for each in self.field_list:
            if each not in self._requests_data:
                raise AliException(f"Missing the required parameters {each}")
            if isinstance(self._requests_data[each], AliBaseModel):
                self._data[each] = self._requests_data[each].dump_sort_data
            elif not self._requests_data[each]:
                raise AliException(f"field {each} is null")
                # _logger.warning(f"field {each} is null")
            else:
                self._data[each] = self._requests_data[each]

    @property
    def dict_data(self):
        self.create_ali_cert_sign()
        return self._data

    @staticmethod
    def _md5_update(cert):
        cert_issue = cert.get_issuer()
        name = 'CN={},OU={},O={},C={}'.format(cert_issue.CN, cert_issue.OU, cert_issue.O, cert_issue.C)
        string = name + str(cert.get_serial_number())
        m = hashlib.md5()
        m.update(bytes(string, encoding="utf8"))
        return m.hexdigest()

    # 获取本应用的证书内置序列号
    @staticmethod
    def get_cert_sn(cert):
        cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        return AliBaseModel._md5_update(cert)

    @staticmethod
    def read_pem_cert_chain(root_cert):
        certs = list()
        for c in root_cert.split('\n\n'):
            cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, c)
            certs.append(cert)
        return certs

    # 获取支付宝根证书的内置序列号
    def get_root_cert_sn(self, root_cert):
        """
        """
        certs = self.read_pem_cert_chain(root_cert)
        root_cert_sn = None
        for cert in certs:
            try:
                sig_alg = cert.get_signature_algorithm()
            except ValueError:
                continue
            if b'rsaEncryption' in sig_alg or b'RSAEncryption' in sig_alg:
                cert_sn = AliBaseModel._md5_update(cert)
                if not root_cert_sn:
                    root_cert_sn = cert_sn
                else:
                    root_cert_sn = root_cert_sn + '_' + cert_sn
        return root_cert_sn

    # 证书签名
    def create_ali_cert_sign(self):
        self._data['method'] = self.method
        self._data['app_cert_sn'] = self.get_cert_sn(open(self._conf_file.app_cert_public_key_path).read())
        self._data['alipay_root_cert_sn'] = self.get_root_cert_sn(open(self._conf_file.alipay_root_cert_path).read())
        self._data = self._sort(self._data)
        raw = []
        self._data = self._sort(self._data)
        for k, v in self._data.items():
            raw.append(f"{k}={v}")
        s = "&".join(raw)
        # 签名
        if self._conf_file.private_key_path.startswith('/'):
            key_file_path = self._conf_file.private_key_path
        else:
            key_file_path = os.path.abspath(os.path.join(basedir, f"../{self._conf_file.app_private_key_path}"))
        _logger.debug(key_file_path)
        with open(key_file_path, 'rb') as fp:
            rsa_text = fp.read()
            private_key = RSA.importKey(rsa_text)
        signer = PKCS1_v1_5.new(private_key)
        signature = signer.sign(SHA256.new(s.encode('utf-8')))
        sign = b64encode(signature).decode("utf-8")
        self._data['sign'] = sign

    @property
    def dump_sort_data(self):
        return json.dumps(self._sort(self._data))

    def to_dict(self):
        return self._data
