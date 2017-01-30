from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User


class Blog_List(LoginRequireHandler):
    def get(self, *args, **kwargs):

        start_id = 0
        number = 10

        try:
            number = self.get_argument('number')
            start_id = self.get_argument('id')
        except:
            pass

        blogs = Blog().get_blogs_by_author(self.datebase(), self.user_id, start_id, number)

        if blogs is not None:
            self.result['result'] = True
            self.result['message'] = {
                blog.id:
                    {
                        'title': blog.title,
                        'author': User().get_user_by_id(self.datebase(), blog.author).nickname,
                        'description': blog.description
                    } for blog in blogs
                }
        elif blogs is None:
            self.result['result'] = False
            self.result['message'] = {
                'error': 'No more blog'
            }

        self.finish(self.result)
