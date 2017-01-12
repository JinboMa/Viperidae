import datetime
from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import get_logger


class Edit_Blog(LoginRequireHandler):
    class_name = 'Edit Blog'

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.logger = get_logger(self.class_name, 'Blog')
        super(Edit_Blog, self).prepare()

    def post(self, *args, **kwargs):
        try:
            id = self.get_argument('id')
            title = self.get_argument('title')
            content = self.get_argument('content')
            last_edit_time = datetime.datetime.now()

            self.logger.info('blog id:{}, title:{}, content:{}, last_edit_time:{}'
                             .format(id, title, content, last_edit_time))

            blog = Blog().edit_blog(self.datebase(), id, self.user_id, title, content, last_edit_time)

            if blog is True:
                self.result['result'] = True
                self.logger.info('edit blog success')
            else:
                self.result['result'] = False
                self.result['message']['error'] = blog
                self.logger.info('edit blog false, result:{}'.format(blog))
        except:
            self.result['result'] = False
            self.result['message']['error'] = '参数错误'
            self.logger.info('edit blog false, result:{}'.format('get parameter error'))
        finally:
            self.finish(self.result)
