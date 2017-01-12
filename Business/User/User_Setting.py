from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import get_logger
from Module.User import User


class User_Setting(LoginRequireHandler):
    class_name = 'User Setting'

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.logger = get_logger(self.class_name, 'User')
        super(User_Setting, self).prepare()

    def post(self, *args, **kwargs):
        try:
            info = {
                'name': self.get_argument('name'),
                'nickname': self.get_argument('nickname'),
                'password': self.get_argument('password'),
                'email': self.get_argument('email'),
                'telphone': self.get_argument('telphone'),
                'picture': self.get_argument('picture'),
                'id_number': self.get_argument('id_number')
            }

            self.logger.info(
                'get info success, name:{}, nickname:{}, password:{}, email:{}, telphone:{}, picture:{}, id_number:{}'
                    .format(
                    info['name'], info['nickname'], info['password'], info['email'],
                    info['telphone'], info['picture'], info['id_number']
                )
            )

            if User().setting(self.datebase(), self.user_id, info) is True:
                self.result['result'] = True
            else:
                self.result['result'] = False
                self.result['message']['error'] = '修改失败'

        except Exception as e:
            self.result['result'] = False
            self.result['message']['error'] = '请求参数错误'
            self.logger.error('get info false, error:{}'.format(e))

        self.finish(self.result)
