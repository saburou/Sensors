# coding: utf-8

from bottle import template, route

@get('/sensor')
def sensorEdit():
    return template('sensor', id=1, name='test', pinNo=1, available=True, direction=1, mode=10)
