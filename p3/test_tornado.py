# coding=utf-8
'''
Created on 2016年8月19日

@author: qiu
'''
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.gen import coroutine


class MainHandler(RequestHandler):

    @coroutine
    def get(self):
        client = AsyncHTTPClient()
        response = yield client.fetch('http://steve.office.mieasy.com')
        self.write(response.body)
        self.finish()


if __name__ == '__main__':
    handlers = [
        (r'/', MainHandler)
    ]
    app = Application(handlers)
    app.listen(8888)
    IOLoop.current().start()
