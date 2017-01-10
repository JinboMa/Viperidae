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

            write('INFO', '[Edit Blog] blog id:{}, title:{}, content:{}, last_edit_time:{}'.format(id, title, content,
                                                                                                   last_edit_time))

            blog = Blog().edit_blog(self.datebase(), id, self.user_id, title, content, last_edit_time)

            if blog is True:
                write('INFO', '[Edit Blog] edit blog success')
                self.result['result'] = True
            else:
                write('INFO', '[Edit Blog] edit blog false, result:{}'.format(blog))
                self.result['result'] = False
                self.result['message']['error'] = blog
        except:
            write('INFO', '[Edit Blog] edit blog false, result:{}'.format('get parameter error'))
            self.result['result'] = False
            self.result['message']['error'] = '参数错误'
        finally:
            space()
            self.finish(self.result)
