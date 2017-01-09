import datetime
import json
import tornado.web
from Module.User import User
from Business.BaseHandler import BaseHandler


class Registration(BaseHandler):
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def post(self, *args, **kwargs):
        telphone = self.get_argument('telphone')
        password = self.get_argument('password')
        nickname = self.get_argument('nickname')

        registration_time = datetime.datetime.now()

        user = User(telphone=telphone, password=password, nickname=nickname, registration_time=registration_time)
        result = user.registration(self.datebase, user)

        if result is True:
            self.result['result'] = True
        else:
            self.result['result'] = False
            self.result['message']['error'] = result
        self.finish(self.result)
