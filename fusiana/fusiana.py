#-*-coding:utf-8-*-
import tornado.web
from datetime import datetime

class Fusiana(tornado.web.RequestHandler):
  def get(self):
    print(self.request)
    info = str(datetime.now())+str(self.request)
    f = open('ip.txt')
    history = f.read()
    f.close()
    self.write('''<meta charset="utf-8">
    <h1>IPアドレスを記録したぞ</h1>
    '''+history+info)
    f = open('ip.txt','a')
    f.write(info+'<hr/>\n')
    f.close()

if __name__ == '__main__':
  app = tornado.web.Application([
    (r'/',Fusiana)
  ])
  app.listen(8889)
  tornado.ioloop.IOLoop.instance().start()
