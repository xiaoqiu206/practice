# coding=utf-8
'''
Created on 2016年4月10日
客户端使用post发送消息,服务端使用websocket推送消息
@author: xiaoq
'''
import tornado.httpserver
import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.gen
import tornadoredis
from tornado.options import define, options

import logging
import os.path


define('port', default=80, help='run on the given port')
define('host', default='0.0.0.0', help="run on the given host")


rc = tornadoredis.Client()
rc.connect()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index2.html", title="PubSub + WebSocket Demo")


class NewMessageHandler(tornado.web.RequestHandler):

    def post(self):
        message = self.get_argument("message")
        rc.publish("chat", message)
        self.set_header('Content-Type', 'text/plain')
        self.write('sent: %s' % message)


class MessageHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, *args, **kwargs):
        super(MessageHandler, self).__init__(*args, **kwargs)
        self.listen

    @tornado.gen.engine
    def listen(self):
        self.client = tornadoredis.Client()
        self.client.connect()
        yield tornado.gen.Task(self.client.subscribe, 'chat')
        self.client.listen(self.on_message)

    def on_message(self, msg):
        if msg.kind == 'message':
            self.write_message(str(msg.body))
        if msg.kind == 'disconnect':
            # Do not try to reconnect, just send a message back
            # to the client and close the client connection
            self.write_message('The connection terminated'
                               ' due to a Redis server error.')
            self.close()

    def on_close(self):
        if self.client.subscribed:
            self.client.unsubscribe('chat')
            self.client.disconnect()


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/', MainHandler),
            (r'/msg', NewMessageHandler),
            (r'/track', MessageHandler),
        ]
        settings = dict(
            cookie_secret="lsadjfolasjfd",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
