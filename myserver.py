# coding: utf-8

from bottle import template, run, route
from dao import SensorDao

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/sensor')
def sensor():
    d = SensorDao.SensorDao()
    return str(d.select())

run(host='localhost', port=8080, debug=True)
