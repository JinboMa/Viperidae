from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Module.User import User


class Get_User_Blog(LoginRequireHandler):
    def get(self, *args, **kwargs):

        start_id = 0
        number = 10

        try:
            number = self.get_argument('number')
            start_id = self.get_argument('id')
        except:
            pass

        print('start id : {}'.format(start_id))
        print('number : {}'.format(number))

        blogs = Blog().get_blogs_by_author(self.datebase(), self.user_id, start_id, number)

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
