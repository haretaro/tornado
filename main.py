#-*-coding:utf-8-*-
import os
import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback
import jsay
from fusiana import Fusiana

app = tornado.web.Application([
    (r'/',jsay.MainPage),
    (r'/websocket',jsay.SendWebSocket),
    (r'/fusiana',Fusiana)
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
