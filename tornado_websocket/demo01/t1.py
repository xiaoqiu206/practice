# coding=utf-8
'''
Created on 2016年4月9日
tornado websocket的练习1
@author: xiaoq
'''
import tornado.ioloop
import tornado.options
import tornado.websocket
import tornadoredis
import tornado.gen
from tornado.web import asynchronous

import logging
import os.path

from tornado.options import define, options

define('port', default=80, help='run on the given port')
define('host', default='0.0.0.0', help="run on the given host")

rc = tornadoredis.Client()
rc.connect()


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/', MainHandler),
            (r'/chat', ChatSocketHandler),
            (r'/msg', NewMessageHandler),
        ]
        settings = dict(
            cookie_secret="lsadjfolasjfd",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class NewMessageHandler(tornado.web.RequestHandler):

    @asynchronous
    def post(self):
        message = self.get_argument('message')
        rc.publish('chat', message)
        self.set_header('Content-Type', 'text/plain')
        self.write('sent: %s' % message)


class MainHandler(tornado.web.RequestHandler):

    @asynchronous
    def get(self):
        self.render("index1.html")


class ChatSocketHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, *args, **kwargs):
        super(ChatSocketHandler, self).__init__(*args, **kwargs)
        self.listen()

    @tornado.gen.engine
    def listen(self):
        self.client = tornadoredis.Client()
        self.client.connect()
        yield tornado.gen.Task(self.client.subscribe, 'chat')
        self.client.listen(self.on_message)

    def open(self):
        logging.info("%s websocket connect" % self.request.remote_ip)

    def on_message(self, msg):
        logging.info("%s get message %s" % (self.request.remote_ip, msg))
        if msg.kind == 'message':
            self.write_message(msg.body.encode('utf-8'))
        if msg.kind == 'disconnect':
            self.write_message("The connection terminated"
                               "due to a Redis server error.")
            self.close()

    def on_close(self):
        if self.client.subscribed:
            self.client.unsubscribe('chat')
            self.client.disconnect()
        logging.info("%s websocket close" % self.request.remote_ip)


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
