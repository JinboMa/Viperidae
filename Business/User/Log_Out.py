from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import get_logger


class Log_Out(LoginRequireHandler):
    class_name = 'Log Out'

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.logger = get_logger(self.class_name)
        super(LoginRequireHandler, self).prepare()

    def get(self, *args, **kwargs):
        self.logger.info('user : {} is logout'.format(self.user_id))
        self.clear_cookie('user')
        self.logger.info('user : {} is clear cookie'.format(self.user_id))
        self.result['result'] = True
        self.finish(self.result)
