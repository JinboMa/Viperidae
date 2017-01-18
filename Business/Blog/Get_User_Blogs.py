from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User


class Get_User_Blog(LoginRequireHandler):
    def get(self, *args, **kwargs):
        blogs = Blog().get_blogs_by_author(self.datebase(), self.user_id)

        self.result['result'] = True
        if blogs is not None:
            self.result['message'] = {
                blog.id:
                    {
                        'title': blog.title,
                        'author': User().get_user_by_id(self.datebase(), blog.author).nickname
                    } for blog in blogs
                }
        else:
            self.result['message'] = {}

        self.finish(self.result)
