import json

import tornado.web
from Business.BaseHandler import BaseHandler

from Module.User import User


class User_setting(BaseHandler):
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        try:
            user_cookie = self.get_secure_cookie('user').decode().split('-')
            self.user_id = user_cookie[0]
        except:
            self.result['result'] = False
            self.result['message'] = '尚未登陆'
            self.finish(json.dumps(self.result))

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name')
            nickname = self.get_argument('nickname')
            password = self.get_argument('password')
            email = self.get_argument('email')
            telphone = self.get_argument('telphone')
            id_number = self.get_argument('id_number')

            user = self.datebase().query(User).get(self.user_id)

            user.name = name
            user.nickname = nickname
            user.password = password
            user.email = email
            user.telphone = telphone
            user.id_number = id_number

            self.datebase().commit()

        except:
            self.result['result'] = False
            self.result['message']['error'] = '请求参数错误'

        self.finish(self.result)
