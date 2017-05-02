# coding: utf-8
# @Time    : 2017/5/2 23:23
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : admin.py
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models import Event, Registrant
from app import db

admin = Admin(name='USTC-Register')
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Registrant, db.session))