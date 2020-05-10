#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/5/21 21:26
# @Author  : xialei
# @Email   : 15755372104@126.com
# @File    : manager.py
# @Software: PyCharm
# @Note    :
"""
import logging
from flask.cli import FlaskGroup
import click
from application import create_app

_logger = logging.getLogger(__name__)
__author__ = "xialei"

app = create_app()


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    click.echo('flask run')


if __name__ == "__main__":
    cli()
