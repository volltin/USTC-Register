# coding: utf-8
# @Time    : 2017/4/30 14:13
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : forms.py

from app import app
from flask import session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp

from datetime import datetime

from app.models import Registrant, Event

class RegisterForm(FlaskForm):
    event_id = HiddenField(u'活动编号', validators=[DataRequired()])
    event_name = StringField(u'活动名称', render_kw={'readonly': True})
    ustc_id = StringField(u'学号', validators=[], render_kw={'readonly': True})
    name = StringField(u'姓名', validators=[DataRequired(), Length(0, 30)])
    gender = SelectField(u'性别', choices=[(u'0', u'男生'), (u'1', u'女生')])
    reason = TextAreaField(u'报名理由', description=u"200 字以内（可空）", validators=[Length(0, 200)])
    email = StringField(u'E-mail', validators=[DataRequired(), Email(), Length(0, 64)])
    mobile = StringField(u'联系电话', validators=[DataRequired(), Regexp(r'^1[3|4|5|7|8][0-9]\d{8}$')])
    submit = SubmitField(u'提交')

    def validate_ustc_id(self, data):
        if not session.get("ustc_id"):
            self.ustc_id.data = None
            self.ustc_id.errors.append('Login from USTC again.')
            return False
        if session.get("ustc_id") != self.ustc_id.data:
            session["ustc_id"] = None
            self.ustc_id.data = None
            self.ustc_id.errors.append('Go back to index and login from USTC again.')
            return False
        event = Event.query.filter_by(event_id=self.event_id.data).first()
        registrant = event.registrants.filter_by(ustc_id=self.ustc_id.data).first()
        if registrant != None:
            self.ustc_id.errors.append('This ustc id is already registered.')
            return False
        return True

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        event = Event.query.filter_by(event_id=self.event_id.data).first()
        if event != None:
            now_time = datetime.now()
            if now_time < event.register_start_time:
                self.event_name.errors.append('Register not begin.')
                return False
            if event.register_end_time < now_time:
                self.event_name.errors.append('Register ended.')
                return False
            if event.registrants.count() >= event.max_number:
                self.event_name.errors.append('Registrants exceeded.')
                return False
            return True
        else:
            self.event_name.errors.append('Event not found.')
            return False


def creat_register_form(event):
    form = RegisterForm()
    form.event_id.data = event.event_id
    form.event_name.data = event.name

    if not session.get("ustc_id"):
        cas_url = app.config.get("USTC_CAS_URL") % event.event_id
        form.ustc_id.label.text += u' <a href="%s" class="btn btn-info btn-xs" id="bind_ustc_id">点击绑定学号</a>' % cas_url
    if not event.need_email:
        del form.email
    if not event.need_mobile:
        del form.mobile
    if not event.need_ustc_id:
        del form.ustc_id
    if not event.need_gender:
        del form.gender
    if event.need_ustc_id:
        ustc_id = session.get("ustc_id")
        if ustc_id:
            form.ustc_id.data = ustc_id
    return form

class AdminLoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登录')