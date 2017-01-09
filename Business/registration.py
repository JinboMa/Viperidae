import datetime
from Handler.BaseHandler import BaseHandler
from Module.User import User
from Log.logger import get_logging


class Registration(BaseHandler):
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.log = get_logging()

    def post(self, *args, **kwargs):
        telphone = self.get_argument('telphone')
        password = self.get_argument('password')
        nickname = self.get_argument('nickname')

        self.log.info('[Registration] telphone:{}, password:{}, nickname:{}'.format(telphone, password, nickname))

        registration_time = datetime.datetime.now()

        self.log.info('[Registration] registration time:{}'.format(registration_time))

        user = User(telphone=telphone, password=password, nickname=nickname, registration_time=registration_time)
        result = user.registration(self.datebase, user)

        if result is True:
            self.log.info('[Registration] registration success')
            self.result['result'] = True
        else:
            self.log.info('[Registration] registration false, result:{}'.format(result))
            self.result['result'] = False
            self.result['message']['error'] = result
        self.finish(self.result)
