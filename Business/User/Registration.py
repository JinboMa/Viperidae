import datetime
from Handler.BaseHandler import BaseHandler
from Module.User import User
from Log.logger import get_logger


class Registration(BaseHandler):
    class_name = 'Registration'
    result = {
        'result': None,
        'message': {}
    }

    def prepare(self):
        self.result['result'] = None
        self.result['message'] = {}
        self.logger = get_logger(self.class_name, self.sign, 'User')

    def post(self, *args, **kwargs):

        telphone = self.get_argument('telphone')
        password = self.get_argument('password')
        nickname = self.get_argument('nickname')
        registration_time = datetime.datetime.now()

        self.logger.info('telphone:{}, password:{}, nickname:{}, registration time:{}'
                         .format(telphone, password, nickname, registration_time))

        user = User(telphone=telphone, password=password, nickname=nickname, registration_time=registration_time)
        result = user.registration(self.datebase, user)

        if result is True:
            self.result['result'] = True
            self.logger.info('registration success')
        else:
            self.result['result'] = False
            self.result['message']['error'] = result
            self.logger.error('registration false, result:{}'.format(result))

        self.finish(self.result)
