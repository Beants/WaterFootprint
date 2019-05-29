#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/29 12:24 AM
# @Author : maxu
# @Site : 
# @File : init.py
# @Software: PyCharm
from flask import Flask, render_template, request, redirect, url_for, session

import sql

app = Flask(__name__)
app.secret_key = 'dhakjshdkhaksjdhjkaasdlashdfishvnbaiuorh'
sqlManager = sql.Sql()


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('login.html')


@app.route('/main/', methods=['POST', 'GET'])
def main():
    name = session.get('name')
    return render_template('index.html',name=name)


@app.route('/reg/', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        temp = sqlManager.reg(username, password, name, email)
        if temp['code'] == 1:
            return render_template('reg.html', info='账号已存在!')
        else:
            return render_template('login.html')
    else:
        return render_template('reg.html', info=None)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        temp = sqlManager.login(username, password)
        if temp['code'] == 1:
            return render_template('login.html', info='')
        else:
            session['name'] = temp['data']['name']
            print(session)
            return redirect(url_for('mian'))
    else:
        return render_template('login.html', info=None)


@app.route('/logout/', methods=['POST', 'GET'])
def logout():
    if request.method == 'POST':
        name = request.form['name']
        # password = request.form['password']
        if 'name' in session:
            session.pop('name', None)
            return render_template('login.html', info='')
        else:
            return redirect(url_for('login'))
    # else:
    #     return render_template('login.html', info=None)


if __name__ == '__main__':
    app.run()
