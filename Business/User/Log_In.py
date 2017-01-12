from Handler.BaseHandler import BaseHandler
from Module.User import User
from Log.logger import get_logger


class Log_In(BaseHandler):
    class_name = 'Log In'
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.result['result'] = None
        self.result['message'] = {}
        self.logger = get_logger(self.class_name, 'User')

    def post(self, *args, **kwargs):
        try:
            telphone = self.get_argument('telphone')
            password = self.get_argument('password')

            self.logger.info('telphone:{}, password:{}'.format(telphone, password))

            user = User(telphone=telphone, password=password)
            user = user.verification(self.datebase, user)

            if user is not False:
                if isinstance(user, User):
                    # 返回cookie
                    self.set_secure_cookie('user', str(user.id) + '-' + user.password)
                    self.result['result'] = True
                    self.logger.info('log in success and set cookie success')
                else:
                    self.result['result'] = False
                    self.result['message']['error'] = user
                    self.logger.info('log in false, result:{}'.format(user))
            else:
                self.result['result'] = False
                self.result['message']['error'] = '未知错误'
                self.logger.info('log in false, result:{}'.format('unknow'))
        except Exception as e:
            self.result['result'] = False
            self.result['message']['error'] = '参数传递错误'
            self.logger.error('log in false, result:{}'.format(e))

        self.finish(self.result)
