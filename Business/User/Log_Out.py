import datetime
from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User
from Log.logger import write, space


class Log_Out(LoginRequireHandler):
    result = {
        'result': None,
        'message': {}
    }

    def datebase(self):
        return self.application.datebase

    def get(self, *args, **kwargs):
        self.clear_cookie('user')
        self.result['result'] = True
        self.finish(self.result)
