#-*-coding:utf-8-*-
import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('hello, world')

class SendWebSocket(tornado.websocket.WebSocketHandler):

  def check_origin(self, origin):
    return True

  def open(self):
    self.i = 0
    self.callback = PeriodicCallback(self._send_message, 400)
    self.callback.start()
    print('WebSocket opendやで')

  def on_message(self, message):
    print(message)

  def _send_message(self):
    self.i += 1
    self.write_message(str(self.i))

  def on_close(self):
    self.callback.stop()
    print('WebSocket closed')

app = tornado.web.Application([
  (r'/',SendWebSocket),
  (r'/test',MainHandler),
])

if __name__ == '__main__':
  app.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
