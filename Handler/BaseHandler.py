import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def write(self, chunk):
        self.set_header('Access-Control-Allow-Origin', True)
        super(BaseHandler, self).write(chunk)
