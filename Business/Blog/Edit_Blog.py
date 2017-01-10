import datetime
from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import write, space


class Edit_Blog(LoginRequireHandler):
    def datebase(self):
        return self.application.datebase

    def post(self, *args, **kwargs):
        try:
            id = self.get_argument('id')
            title = self.get_argument('title')
            content = self.get_argument('content')
            last_edit_time = datetime.datetime.now()

            blog = Blog().edit_blog(self.datebase(), id, self.user_id, title, content, last_edit_time)

            if blog is True:
                self.result['result'] = True
            else:
                self.result['result'] = False
                self.result['message']['error'] = blog
        except:
            self.result['result'] = False
            self.result['message']['error'] = '参数错误'
        finally:
            self.finish(self.result)
