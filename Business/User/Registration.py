import datetime
from Handler.BaseHandler import BaseHandler
from Module.User import User
from Log.logger import write, space


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

        write('INFO',
              '[Registration] telphone:{}, password:{}, nickname:{}, registration time:{}'.format(telphone, password,
                                                                                                  nickname,
                                                                                                  registration_time))

        user = User(telphone=telphone, password=password, nickname=nickname, registration_time=registration_time)
        result = user.registration(self.datebase, user)

        if result is True:
            write('INFO', '[Registration] registration success')
            self.result['result'] = True
        else:
            write('INFO', '[Registration] registration false, result:{}'.format(result))
            self.result['result'] = False
            self.result['message']['error'] = result

        space()
        self.finish(self.result)
