from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User
from Log.logger import write, space


class Blog_Details(LoginRequireHandler):
    def datebase(self):
        return self.application.datebase

    def get(self, blog_id, *args, **kwargs):
        write('INFO', '[Blog Details] enter blog details, blog id is {}'.format(blog_id))
        try:
            blog_id = int(blog_id)
            blog = Blog().get_blog_by_id(self.datebase(), blog_id)
            if blog is not None:
                write('INFO', '[Blog Details] blog is not None')
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
                write('INFO',
                      '[Blog Details] blog details:title:{}, author:{}, content:{}, create_time:{}, last_edit_time:{}'.format(
                          blog.title, User().get_user_by_id(self.datebase(), blog.author).nickname, blog.content,
                          blog.create_time, blog.last_edit_time))
                self.result['result'] = True
            else:
                write('INFO', '[Blog Details] blog is None')
                self.result['result'] = False
                self.result['message']['error'] = '无此blog'
        except Exception as e:
            write('ERROR', '[Blog Details] error:{}'.format(e))
            self.result['result'] = True
            self.result['message']['error'] = '参数错误'
        space()
        self.finish(self.result)