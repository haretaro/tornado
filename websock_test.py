#-*-coding:utf-8-*-
import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('hello, world')

class SendWebSocket(tornado.websocket.WebSocketHandler):

  num = 0 #インクリメントする数字
  conn = 0 #接続中のホスト数

  @classmethod
  def update_num(cls):
    cls.num += 1

  @classmethod
  def inclement_conn(cls):
    cls.conn += 1

  @classmethod
  def decrement_conn(cls):
    cls.conn -= 1

  @classmethod
  def get_conn(cls):
    return cls.conn

  def check_origin(self, origin):
    return True

  def open(self):
    self.callback = PeriodicCallback(self._send_message, 400)#メッセージをクライアントに送るコールバック
    self.callback.start()

    self.increment_callback = PeriodicCallback(self.update_num,400)#値をインクリメントするコールバック
    self.inclement_conn()
    if self.get_conn() == 1 :
      self.increment_callback.start()#接続ホスト数が1になった時インクリメントをスタートする

    print('WebSocket opendやで')

  def on_message(self, message):
    print(message)

  def _send_message(self):
    self.write_message(str(self.num) + ' 接続中のホスト数=' + str(self.conn))

  def on_close(self):
    self.callback.stop()

    self.decrement_conn()
    if self.get_conn() == 0:
      self.increment_callback.stop()#接続ホストが0になったらインクリメントをストップ

    print('WebSocket closed')

app = tornado.web.Application([
  (r'/',SendWebSocket),
  (r'/test',MainHandler),
])

if __name__ == '__main__':
  i = 0
  app.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
