from Handler.LoginRequireHandler import LoginRequireHandler
from Module.Event import Event


class Get_Event(LoginRequireHandler):
    def post(self, *args, **kwargs):
        events = Event().get_event_by_id(self.datebase(), self.user_id)
        if events is not None:

            self.result['result'] = True
            self.result['message']['data'] = {
                event.id: {'name': event.event_name, 'remarks': event.remarks, 'priority': event.priority} for event in
                events}
        else:
            self.result['result'] = True

        self.finish(self.result)
