import json

import tornado.web
from Module.User import User


class Log_in(tornado.web.RequestHandler):
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def post(self, *args, **kwargs):
        try:
            telphone = self.get_argument('telphone')
            password = self.get_argument('password')

            user = User(telphone=telphone, password=password)
            user = user.log_in(self.datebase, user)

            if user is not False:
                self.set_secure_cookie('user', str(user.id) + '-' + user.password)
                self.result['result'] = True
            else:
                self.result['result'] = False
                self.result['message']['error'] = '用户不存在'
        except:
            self.result['result'] = False
            self.result['message']['error'] = '参数传递错误'

        self.finish(json.dumps(self.result))
