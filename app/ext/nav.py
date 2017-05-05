# coding: utf-8
# @Time    : 2017/5/3 0:11
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : nav.py

from flask import url_for
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@nav.navigation()
def ustc_register_nav():
    return Navbar(
        'USTC-Register',
        View('Home', 'index', page = 1)
    )