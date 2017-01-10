import datetime
from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import write, space


class Create_Blog(LoginRequireHandler):
    def datebase(self):
        return self.application.datebase

    def post(self, *args, **kwargs):
        try:
            title = self.get_argument('title')
            content = self.get_argument('content')
            author = self.user_id
            create_time = datetime.datetime.now()
            last_edit_time = datetime.datetime.now()

            write('INFO',
                  '[Create Blog] title:{}, author:{}, create_time:{}, last_edit_time:{}'.format(title, content,
                                                                                                create_time,
                                                                                                last_edit_time))
            write('INFO', '[Create Blog] content:{}'.format(content))

            blog = Blog(title=title, content=content, author=author, create_time=create_time,
                        last_edit_time=last_edit_time)

            if blog.create(self.datebase(), blog):
                write('INFO', '[Create Blog] add blog success')
                self.result['result'] = True
            else:
                write('INFO', '[Create Blog] add blog false')
                self.result['result'] = False
                self.result['error'] = '数据库操作失败'
        except Exception as e:
            write('ERROR', e)
            space()
            self.result['result'] = False
            self.result['message']['error'] = '参数传递错误'

        finally:
            space()
            self.finish(self.result)
