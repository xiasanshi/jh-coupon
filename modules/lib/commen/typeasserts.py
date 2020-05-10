#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/2/25 9:13
@Site    :
@File    : typeasserts.py
@Software: PyCharm
@Author  : xialei
@Email   : xialei@gcbi.com.cn
@Notes   :
"""
import os
import logging
from functools import wraps
from inspect import signature

# from collections import namedtuple

__author__ = 'xialei'
_basedir = os.path.dirname(__file__)
_logger = logging.getLogger(__name__)


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(y=int, z=int)
def ss(x, y, z):
    print(x, y, z)


def main():
    t = ss(1, 2, 3)
    t = ss(1, 2, '3')


if __name__ == '__main__':
    main()
