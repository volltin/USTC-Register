# coding: utf-8
# @Time    : 2017/4/30 13:41
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# 管理员用户名
ADMIN_USER = 'admin'

# 管理员密码
ADMIN_PASS = '-1s-1s-1s-1s'

# 首页上每一页的显示数量
EVENT_PER_PAGE = 10

# 统一认证登陆地址 (See: https://github.com/volltin/USTC-CAS-Redirect)
USTC_CAS_URL = "http://home.ustc.edu.cn/~yourname/index.html?id=%d"

# 用于防止 CRRF 攻击的 key
SECRET_KEY = '+1s+1s+1s+1s'
CSRF_ENABLED = True

# 数据库配置

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
