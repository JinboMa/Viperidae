from Handler.BaseHandler import BaseHandler
from Module.User import User
from Log.logger import get_logger


class Log_In(BaseHandler):
    class_name = 'Log In'
    result = {
        'result': None,
        'message': {}
    }

    def prepare(self):
        self.result['result'] = None
        self.result['message'] = {}
        self.logger = get_logger(self.class_name, self.sign, 'User')

    def get(self, *args, **kwargs):
        user_cookie = None
        try:
            user_cookie = self.get_secure_cookie('user').decode().split('-')
        except Exception as e:
            self.result['result'] = False
            self.result['message']['error'] = '尚未登陆'

        if user_cookie is not None:
            user = User(id=user_cookie[0], password=user_cookie[1])
            result = user.verification_by_id(self.datebase(), user)
            if result is not False:
                if isinstance(result, User):
                    self.result['result'] = True
                    self.result['message'][result.id] = {
                        'nickname': result.nickname,
                        'picture': result.picture
                    }
                else:
                    self.clear_cookie('user')
                    self.result['result'] = False
            else:
                self.clear_cookie('user')
                self.result['result'] = False
        else:
            self.result['result'] = False
            self.result['message'] = '尚未登陆'

        self.finish(self.result)

    def post(self, *args, **kwargs):

        telphone = self.get_argument('telphone')
        password = self.get_argument('password')

        self.logger.info('telphone:{}, password:{}'.format(telphone, password))

        user = User(telphone=telphone, password=password)
        user = user.verification_by_phone(self.datebase, user)

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

        self.finish(self.result)
