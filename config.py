# coding: utf-8
# @Time    : 2017/4/30 13:41
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'glgjssy.qyhfbqz'

# 首页上每一页的显示数量
EVENT_PER_PAGE = 10
# 统一认证登陆地址(See: https://github.com/volltin/USTC-CAS-Redirect)
USTC_CAS_URL = "https://ustcoj.com/tmp/index.html?id=%d"

CSRF_ENABLED = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
