from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import get_logger
from Module.User import User


class User_Setting(LoginRequireHandler):
    class_name = 'User Setting'
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.logger = get_logger(self.class_name)
        super(User_Setting, self).prepare()

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name')
            nickname = self.get_argument('nickname')
            password = self.get_argument('password')
            email = self.get_argument('email')
            telphone = self.get_argument('telphone')
            picture = self.get_argument('picture')
            id_number = self.get_argument('id_number')

            self.logger.info(
                'get info success, name:{}, nickname:{}, password:{}, email:{}, telphone:{}, picture:{}, id_number:{}'.format(
                    name, nickname, password, email, telphone, picture, id_number))

            user = self.datebase().query(User).get(self.user_id)
            self.logger.info('select database success, user id:{}'.format(self.user_id))

            user.name = name
            user.nickname = nickname
            user.password = password
            user.email = email
            user.telphone = telphone
            user.picture = picture
            user.id_number = id_number

            try:
                self.datebase().commit()
                self.logger.warning('commit success')
            except Exception as e:
                self.result['result'] = False
                self.result['message']['error'] = str(e)
                self.logger.error('commit false, error:{}'.format(e))
            finally:
                self.datebase().close()

        except Exception as e:
            self.result['result'] = False
            self.result['message']['error'] = '请求参数错误'
            self.logger.error('get info false, error:{}'.format(e))

        self.finish(self.result)
