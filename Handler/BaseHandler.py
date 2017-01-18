import tornado.web
from Log.Sign import get_sign


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        self.sign = get_sign()
        super(BaseHandler, self).__init__(*args, **kwargs)

    def datebase(self):
        return self.application.datebase

    def write(self, chunk):
        self.set_header('Access-Control-Allow-Origin', 'http://23.105.208.8')
        self.add_header('Access-Control-Allow-Credentials', 'true')
        super(BaseHandler, self).write(chunk)
