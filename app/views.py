# coding: utf-8
# @Time    : 2017/4/30 13:45
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : views.py

from flask import render_template, flash, redirect, request, session, url_for
from app import app, db
from .forms import creat_register_form
from .models import Registrant, Event
from datetime import datetime

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page not found"), 404

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page = 1):
    per_page = app.config["EVENT_PER_PAGE"]
    events_query = Event.query.paginate(page, per_page, False)
    return render_template("index.html",
        events_query = events_query,
        title = 'Home')

@app.route('/register/<int:event_id>', methods = ['GET', 'POST'])
def register(event_id):

    event = Event.query.filter_by(event_id=event_id).first()
    if not event:
        flash("Event not found", "warning")
        return redirect('/')

    if request.args.get('ticket') and request.args.get('service'):
        from app.ext.ustc_cas import USTCCas
        ticket = request.args.get('ticket')
        service = request.args.get('service')
        cas = USTCCas(ticket=ticket, service=service)
        ustc_id = cas.get_ustc_id()
        if ustc_id:
            session["ustc_id"] = ustc_id
            return redirect(url_for('register', event_id=event_id))
        else:
            flash("Login from USTC failed.", "warning")
            return redirect('/')

    form = creat_register_form(event)

    if form.validate_on_submit():
        registrant = Registrant()
        registrant.register_time = datetime.now()
        form.populate_obj(registrant)
        db.session.add(registrant)
        db.session.commit()

        flash("Regiser success.")
        return redirect('/index')

    return render_template('register.html',
        event = event,
        title = 'Register',
        form = form)