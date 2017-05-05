# coding: utf-8
# @Time    : 2017/4/30 13:43
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import models

from app.ext import bootstrap, nav, admin

admin.admin.init_app(app)
bootstrap.bootstrap.init_app(app)
nav.nav.init_app(app)

from app import views
