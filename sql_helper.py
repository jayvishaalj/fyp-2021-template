import mysql.connector as MySQLdb
import datetime
import logging
import os
from regex_layer import check_regex
from ml_layer import check_ml
test = '/test'


class DB:
    def __init__(self, db_dict, socketio):
        print(db_dict)
        logging.basicConfig(filename='test.log', format='%(filename)s: %(message)s',
                            level=logging.DEBUG)
        self.host = db_dict['HOST']
        self.user = db_dict['USER']
        self.pswd = db_dict['PASSWORD']
        self.db = db_dict['DB']
        self.conn = None
        self.cur = None
        self.socketio = socketio
        socketio.emit('my_response',
                      {'data': 'New Response', 'count': 1}, namespace=test, broadcast=True)
        logging.debug('DB Dictionary'+str(db_dict))

    def db_connect(self):
        self.conn = MySQLdb.connect(
            user=self.user, password=self.pswd, host=self.host, database=self.db)
        self.cur = self.conn.cursor()
        logging.debug('Connect Function Called')

    def query(self, sql, value):
        self.db_connect()
        logging.debug('Query Executing ' + sql)
        # First Layer
        if (check_regex(sql)):
            self.socketio.emit('my_red_response',
                               {'data': sql, 'count': 1}, namespace=test, broadcast=True)
            return None
        # Second Layer
        if(check_ml(value) == 1):
            self.socketio.emit('my_red_response',
                               {'data': sql, 'count': 1}, namespace=test, broadcast=True)
            return None
        # Third Layer
        self.socketio.emit('my_response',
                           {'data': sql, 'count': 1}, namespace=test, broadcast=True)
        self.cur.execute(sql)
        return self.cur
