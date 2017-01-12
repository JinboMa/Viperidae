from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User
from Log.logger import get_logger


class Blog_Details(LoginRequireHandler):
    class_name = 'Blog Details'

    def datebase(self):
        return self.application.datebase

    def prepare(self):
        self.logger = get_logger(self.class_name, 'Blog')
        super(Blog_Details, self).prepare()

    def get(self, *args, **kwargs):
        try:
            blog_id = int(self.get_argument('id'))
            blog = Blog().get_blog_by_id(self.datebase(), blog_id)
            if blog is not None:
                self.logger.info('blog is not None')
                self.result['message'] = {
                    blog.id:
                        {
                            'title': blog.title,
                            'author': User().get_user_by_id(self.datebase(), blog.author).nickname,
                            'content': blog.content,
                            'create_time': str(blog.create_time),
                            'last_edit_time': str(blog.last_edit_time)
                        }
                }
                self.logger.info(
                    'blog details:title:{}, author:{}, content:{}, create_time:{}, last_edit_time:{}'.format(
                        blog.title, User().get_user_by_id(self.datebase(), blog.author).nickname, blog.content,
                        blog.create_time, blog.last_edit_time))

                self.result['result'] = True
            else:
                self.logger.info('blog is None')
                self.result['result'] = False
                self.result['message']['error'] = '无此blog'
        except Exception as e:
            self.logger.error('error:{}'.format(e))
            self.result['result'] = True
            self.result['message']['error'] = '参数错误'
        self.finish(self.result)
