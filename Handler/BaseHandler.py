import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def write(self, chunk):
        self.set_header('Access-Control-Allow-Origin', 'http://23.105.208.8')
        super(BaseHandler, self).write(chunk)
