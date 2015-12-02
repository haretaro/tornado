import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

class MainPage(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')

class SendWebSocket(tornado.websocket.WebSocketHandler):

    def on_message(self, message):
        print(message)

app = tornado.web.Application([
    (r'/',Mainpage),
    (r'/socket',SendWebSocket)
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
