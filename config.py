# coding: utf-8
# @Time    : 2017/4/30 13:41
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

EVENT_PER_PAGE = 10

CSRF_ENABLED = True
SECRET_KEY = 'glgjssy.qyhfbqz'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True