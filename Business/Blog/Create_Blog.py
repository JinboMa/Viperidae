import datetime
from Module.Blog import Blog
from Handler.LoginRequireHandler import LoginRequireHandler
from Log.logger import get_logger


class Create_Blog(LoginRequireHandler):
    class_name = 'Create Blog'

    def prepare(self):
        self.logger = get_logger(self.class_name, self.sign, 'Blog')
        super(Create_Blog, self).prepare()

    def post(self, *args, **kwargs):

        title = self.get_argument('title')
        content = self.get_argument('content')
        description = self.get_argument('description')
        author = self.user_id
        create_time = datetime.datetime.now()
        last_edit_time = datetime.datetime.now()

        self.logger.info(
            'title:{}, author:{}, create_time:{}, last_edit_time:{}'
                .format(title, content, create_time, last_edit_time)
        )
        self.logger.info('content:{}'.format(content))

        blog = Blog(
            title=title,
            content=content,
            description=description,
            author=author,
            create_time=create_time,
            last_edit_time=last_edit_time
        )

        result = blog.create(self.datebase(), blog)

        if result is True:
            self.result['result'] = True
            self.logger.info('add blog success')
        else:
            self.result['result'] = False
            self.result['error'] = '数据库操作失败'
            self.logger.info('add blog false, result:{}'.format('数据库操作失败'))
            self.logger.error(result)

        self.finish(self.result)
