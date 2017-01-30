import datetime
from Module.Blog_Rate_Recording import Blog_Rate_Recording
from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import get_logger


class Blog_Rate(LoginRequireHandler):
    class_name = 'Blog Details'

    def prepare(self):
        self.logger = get_logger(self.class_name, self.sign, 'Blog')
        super(Blog_Rate, self).prepare()

    def post(self, *args, **kwargs):
        blog_id = self.get_argument('id')
        rate = float(self.get_argument('rate'))

        recording = Blog_Rate_Recording(
            user_id=self.user_id,
            blog_id=blog_id,
            rate=rate,
            time=datetime.datetime.now()
        )

        recording_result = recording.add_blog_rate_recording(self.datebase(), recording)

        if recording_result is True:
            update_rate_result = Blog().update_rate(self.datebase(), blog_id, rate)
            if update_rate_result is True:
                self.result['result'] = True
            else:
                self.result['result'] = False
                self.result['message']['error'] = update_rate_result
        else:
            self.result['result'] = False
            self.result['message']['error'] = recording_result

        self.finish(self.result)
