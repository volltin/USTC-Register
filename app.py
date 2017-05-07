# coding: utf-8
# @Time    : 2017/5/7 11:46
# @Author  : Jiyan He <ustchjy@gmail.com>
# @File    : app.py

if __name__ == '__main__':
    # !flask/bin/python
    from app import app
    app.run(host="0.0.0.0", debug=True, threaded=True)
