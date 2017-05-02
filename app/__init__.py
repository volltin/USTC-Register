# coding: utf-8
# @Time    : 2017/4/30 13:43
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import views, models

from app import admin
admin.admin.init_app(app)

from app import bootstrap
bootstrap.bootstrap.init_app(app)

from app import nav
nav.nav.init_app(app)