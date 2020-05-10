#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/9/15 16:56
@Site    : 
@File    : wx_biz_data_crypt.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import os
import base64
import json
# from Crypto.Cipher import AES
# from Crypto.Cipher import AES

from Cryptodome.Cipher import AES

import logging

__author__ = 'xialei'
_logger = logging.getLogger(__name__)


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)).decode())

        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]


# def _encrypt(key, plain_text):
#     mod = len(plain_text) % 16
#     if mod > 0:
#         # 补齐16的倍数
#         zero = '\0' * (16 - mod)
#         plain_text += zero
#     aes = AES.new(key.encode(), AES.MODE_ECB)
#     cipher_text = binascii.hexlify(aes.encrypt(plain_text.encode())).decode()
#     return cipher_text
#
#
# def _decrypt(key, cipher_text):
#     aes = AES.new(key.encode(), AES.MODE_ECB)
#     plain_text = aes.decrypt(binascii.unhexlify(cipher_text)).decode().rstrip('\0')
#     return plain_text

if __name__ == '__main__':
    appId = 'wx4f4bc4dec97d474b'
    sessionKey = 'tiihtNczf5v6AKRyjwEUhQ=='
    encryptedData = 'CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC+oNPdbB+3hVbJSRgv+4lGOETKUQz6OYStslQ142dNCuabNPGBzlooOmB231qMM85d2/fV6ChevvXvQP8Hkue1poOFtnEtpyxVLW1zAo6/1Xx1COxFvrc2d7UL/lmHInNlxuacJXwu0fjpXfz/YqYzBIBzD6WUfTIF9GRHpOn/Hz7saL8xz+W//FRAUid1OksQaQx4CMs8LOddcQhULW4ucetDf96JcR3g0gfRK4PC7E/r7Z6xNrXd2UIeorGj5Ef7b1pJAYB6Y5anaHqZ9J6nKEBvB4DnNLIVWSgARns/8wR2SiRS7MNACwTyrGvt9ts8p12PKFdlqYTopNHR1Vf7XjfhQlVsAJdNiKdYmYVoKlaRv85IfVunYzO0IKXsyl7JCUjCpoG20f0a04COwfneQAGGwd5oa+T8yO5hzuyDb/XcxxmK01EpqOyuxINew=='
    iv = 'r7BXXKkLb8qrSNn05n0qiA=='

    pc = WXBizDataCrypt(appId, sessionKey)

    print(pc.decrypt(encryptedData, iv))