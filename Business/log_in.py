from Handler.BaseHandler import BaseHandler
from Module.User import User
from Log.logger import write, space


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

            write('INFO', '[Log_in] telphone:{}, password:{}'.format(telphone, password))

            user = User(telphone=telphone, password=password)
            user = user.log_in(self.datebase, user)

            if user is not False:
                if isinstance(user, User):
                    self.set_secure_cookie('user', str(user.id) + '-' + user.password)
                    self.result['result'] = True
                    write('INFO', '[Log_in] log in success and set cookie success')
                else:
                    self.result['result'] = False
                    self.result['message']['error'] = user
                    write('INFO', '[Log_in] log in false, result:{}'.format(user))
            else:
                self.result['result'] = False
                self.result['message']['error'] = '未知错误'
                write('INFO', '[Log_in] log in false, result:{}'.format('未知错误'))
        except Exception as e:
            write('INFO', '[Log_in] log in false, result:{}'.format(e))
            self.result['result'] = False
            self.result['message']['error'] = '参数传递错误'

        space()
        self.finish(self.result)
