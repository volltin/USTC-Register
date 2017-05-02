# coding: utf-8
# @Time    : 2017/4/30 14:13
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

from datetime import datetime

from app.models import Registrant, Event

class RegisterForm(FlaskForm):
    event_id = HiddenField('event_id', validators=[DataRequired()])
    event_name = StringField('event name', render_kw={'readonly': True})
    name = StringField('name', validators=[DataRequired()])
    reason = TextAreaField('reason', description="Less than 500 words", validators=[Length(0, 500)])
    email = StringField('email', validators=[DataRequired(), Email()])
    mobile = StringField('mobile', validators=[DataRequired()])
    ustc_id = StringField('ustc id', validators=[DataRequired()])
    submit = SubmitField('Submit')

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
        else:
            self.event_name.errors.append('Event not found.')
            return False

        if event.need_ustc_id:
            registrant = Registrant.query.filter_by(event_id=self.event_id.data, ustc_id=self.ustc_id.data).first()
            if registrant != None:
                self.ustc_id.errors.append('This ustc id is already registered.')
                return False
            return True

def creat_register_form(event):
    form = RegisterForm()
    form.event_id.data = event.event_id
    form.event_name.data = event.name
    if not event.need_email:
        del form.email
    if not event.need_mobile:
        del form.mobile
    if not event.need_ustc_id:
        del form.ustc_id
    return form
