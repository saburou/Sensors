# coding: utf-8

import redis

class Dao:
    def __init__(self, host='localhost', port=6379, db=0):
        r = redis.Redis(host, port, db)

    def select(self):
        raise NotImplementedError

    def insert(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def close(self):
        self.r.close()
