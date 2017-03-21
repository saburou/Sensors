# coding: utf-8

import mysql.connector
from dao import Dao
class SensorDao():

    # DB名固定 or インスタンス生成時取得なのにテーブル名は固定なの？
    _tableName = 'sensor'

    def __init__(self, user='root', password='root', host='127.0.0.1', database='test'):
        '''
            Setting database connection.
        '''

        self._user = user
        self._password = password
        self._host = host
        self._database = database

    def select(self):
        '''
            select all records from target table.
        '''

        con = mysql.connector.connect(user=self._user, password=self._password, host=self._host, database=self._database)
        cur = con.cursor()
        cur.execute("select id, name, pinNo, available, direction, mode from sensor")

        list = []

        try:
            for row in cur.fetchall():
                # オブジェクトにする
                list.append([row[0],row[1],row[2],row[3],row[4],row[5]])
        finally:
            cur.close
            con.close

        return list
