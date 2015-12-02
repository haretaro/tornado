#-*-coding:utf-8-*-
import os
import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

class MainPage(tornado.web.RequestHandler):

    def get(self):
        self.render('jsay.html')

class SendWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        print('connected')

    def on_close(self):
        print('closed')

    def on_message(self, message):
        #TODO:かなりひどいセキュリティホールがある
        command = 'jsay "' + message.encode('utf-8') + '"'
        os.system(command)
        print(message)

app = tornado.web.Application([
    (r'/',MainPage),
    (r'/websocket',SendWebSocket)
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
