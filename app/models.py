# coding: utf-8
# @Time    : 2017/4/30 13:44
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : models.py

from app import db

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    desc = db.Column(db.Text)
    register_start_time = db.Column(db.DateTime)
    register_end_time = db.Column(db.DateTime)
    max_number = db.Column(db.Integer)
    need_ustc_id = db.Column(db.Boolean)
    need_mobile = db.Column(db.Boolean)
    need_email = db.Column(db.Boolean)
    need_gender = db.Column(db.Boolean)
    registrants = db.relationship('Registrant', backref='event', lazy='dynamic')

    def __repr__(self):
        return '<Event %r>' % (self.name)

class Registrant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    name = db.Column(db.String(50))
    ustc_id = db.Column(db.String(50))
    gender = db.Column(db.Integer)
    mobile = db.Column(db.String(50))
    email = db.Column(db.String(50))
    reason = db.Column(db.String(1000))
    register_time = db.Column(db.DateTime)
    reject = db.Column(db.Boolean, default=False)

    def __repr__(self):
        info = self.name
        if (self.ustc_id):
            info += "(%s)" % self.ustc_id
        return '<Registrant %r>' % info

