import tornado.web


class LoginRequireHandler(tornado.web.RequestHandler):
    result = {
        'result': None,
        'message': {}
    }

    def prepare(self):
        self.result['result'] = None
        self.result['message'] = {}
        try:
            user_cookie = self.get_secure_cookie('user').decode().split('-')
            self.user_id = user_cookie[0]
        except:
            self.result['result'] = False
            self.result['message'] = '尚未登陆'
            self.finish(self.result)
