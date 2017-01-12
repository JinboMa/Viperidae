import datetime
from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import get_logger


class Create_Blog(LoginRequireHandler):
    class_name = 'Create Blog'

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.logger = get_logger(self.class_name, 'Blog')
        super(Create_Blog, self).prepare()

    def post(self, *args, **kwargs):
        try:
            title = self.get_argument('title')
            content = self.get_argument('content')
            author = self.user_id
            create_time = datetime.datetime.now()
            last_edit_time = datetime.datetime.now()

            self.logger.info('title:{}, author:{}, create_time:{}, last_edit_time:{}'
                             .format(title, content, create_time, last_edit_time))
            self.logger.info('content:{}'.format(content))

            blog = Blog(title=title, content=content, author=author,
                        create_time=create_time, last_edit_time=last_edit_time)

            if blog.create(self.datebase(), blog):
                self.result['result'] = True
                self.logger.info('add blog success')
            else:
                self.result['result'] = False
                self.result['error'] = '数据库操作失败'
                self.logger.info('add blog false, result:{}'.format('数据库操作失败'))
        except Exception as e:
            self.result['result'] = False
            self.result['message']['error'] = '参数传递错误'
            self.logger.error('add blog error, result:{}'.format(e))
        finally:
            self.finish(self.result)
