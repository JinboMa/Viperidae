from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User


class User_Setting(LoginRequireHandler):
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name')
            nickname = self.get_argument('nickname')
            password = self.get_argument('password')
            email = self.get_argument('email')
            telphone = self.get_argument('telphone')
            picture = self.get_argument('picture')
            id_number = self.get_argument('id_number')

            user = self.datebase().query(User).get(self.user_id)

            user.name = name
            user.nickname = nickname
            user.password = password
            user.email = email
            user.telphone = telphone
            user.picture = picture
            user.id_number = id_number

            try:
                self.datebase().commit()
            except Exception as e:
                self.result['result'] = False
                self.result['message']['error'] = str(e)
            finally:
                self.datebase().close()

        except:
            self.result['result'] = False
            self.result['message']['error'] = '请求参数错误'

        self.finish(self.result)
