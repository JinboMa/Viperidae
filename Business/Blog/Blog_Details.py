from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User


class Blog_Details(LoginRequireHandler):
    def datebase(self):
        return self.application.datebase

    def get(self, blog_id, *args, **kwargs):

        try:
            blog_id = int(blog_id)
            blog = Blog().get_blog_by_id(self.datebase(), blog_id)
            if blog is not None:
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
                self.result['result'] = True
            else:
                self.result['result'] = False
                self.result['message']['error'] = '无此blog'
        except Exception as e:
            print(e)
            self.result['result'] = True
            self.result['message']['error'] = '参数错误'

        self.finish(self.result)
