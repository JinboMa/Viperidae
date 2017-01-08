import json
import tornado.web
from Module.User import User
from Business.BaseHandler import BaseHandler


class Log_in(BaseHandler):
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.result['result'] = None
        self.result['message'] = {}

    def post(self, *args, **kwargs):
        try:
            telphone = self.get_argument('telphone')
            password = self.get_argument('password')

            user = User(telphone=telphone, password=password)
            user = user.log_in(self.datebase, user)

            if user is not False:
                if isinstance(user, User):
                    self.set_secure_cookie('user', str(user.id) + '-' + user.password)
                    self.result['result'] = True
                else:
                    self.result['result'] = False
                    self.result['message']['error'] = user
            else:
                self.result['result'] = False
                self.result['message']['error'] = '未知错误'
        except Exception as e:
            print(str(e))
            self.result['result'] = False
            self.result['message']['error'] = '参数传递错误'

        self.finish(self.result)
