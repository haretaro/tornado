#-*-coding:utf-8-*-
import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('hello, world')

class SendWebSocket(tornado.websocket.WebSocketHandler):

  num = 0

  @classmethod
  def update_num(cls):
    cls.num += 1

  def check_origin(self, origin):
    return True

  def open(self):
    self.i = 0
    self.callback = PeriodicCallback(self._send_message, 400)
    self.callback.start()
    self.update_num()
    print('WebSocket opendやで')

  def on_message(self, message):
    print(message)

  @classmethod
  def get_num(cls):
    return cls.num

  def _send_message(self):
    self.i += 1
    self.i += 1
    self.write_message(str(self.i)+' num='+str(self.get_num()))

  def on_close(self):
    self.callback.stop()
    print('WebSocket closed')

app = tornado.web.Application([
  (r'/',SendWebSocket),
  (r'/test',MainHandler),
])

if __name__ == '__main__':
  i = 0
  app.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
