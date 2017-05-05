# coding: utf-8
# @Time    : 2017/5/2 23:23
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : admin.py

from flask import session, flash, redirect
from app.forms import AdminLoginForm
from config import ADMIN_USER, ADMIN_PASS
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

from app.models import Event, Registrant
from app import db

class LoginView(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        form = AdminLoginForm()

        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            if username == ADMIN_USER and password == ADMIN_PASS:
                session["admin_username"] = username
                flash('Login successfully!', category='info')
                return redirect('/admin')
            else:
                flash('username or password Wrong', category='warning')
        return self.render('admin_login.html', form=form)

    def is_accessible(self):
        # hide this view when logined
        if session.get("admin_username"):
            return False
        return True

class MyView(ModelView):
    can_create = True
    can_export = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_set_page_size = True

    def __init__(self, cls, **kwargs):
        # You can pass name and other parameters if you want to
        super(MyView, self).__init__(cls, db.session, **kwargs)

    def is_accessible(self):
        if session.get("admin_username"):
            return True
        return False


admin = Admin(name='USTC-Register')

admin.add_view(LoginView(name='Login'))
admin.add_view(MyView(Event))
admin.add_view(MyView(Registrant))