import datetime

from Handler.LoginRequireHandler import LoginRequireHandler
from Module.Event import Event


class Create_Event(LoginRequireHandler):
    def datebase(self):
        return self.application.datebase

    def post(self, *args, **kwargs):

        try:
            event_name = self.get_argument('name')
            remarks = self.get_argument('remarks')
            priority = self.get_argument('priority')
            created_time = datetime.datetime.now()
            end_time = self.get_argument('end_time')
            is_open = self.get_argument('is_open')
            status = 'open'
            belong = self.user_id

            event = Event(event_name=event_name, remarks=remarks, priority=priority, created_time=created_time,
                          end_time=end_time, is_open=is_open, status=status, belong=belong)

            if event.create_event(self.datebase(), event):
                self.result['result'] = True
            else:
                self.result['result'] = False
                self.result['message']['error'] = '未知错误'
        except:
            self.result['result'] = False
            self.result['message']['error'] = '请求参数错误'

        self.finish(self.result)
