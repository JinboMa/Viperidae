import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from Business.log_in import Log_in
from Business.registration import Registration
from Business.user_setting import User_setting
from Business.get_event import Get_Event
from Business.create_event import Create_Event
from Business.Blog.Create_Blog import Create_Blog
from Business.Blog.Get_User_Blogs import Get_User_Blog
from Business.Blog.Blog_Details import Blog_Details
from Business.Blog.Edit_Blog import Edit_Blog


class Application(tornado.web.Application):
    def __init__(self):
        engine = create_engine(
            "mysql+pymysql://root:xuzhaoning@23.105.208.8:3306/personal?charset=utf8",
            echo=False)

        handlers = [

            (r'/login', Log_in),
            (r'/registration', Registration),
            (r'/user/setting', User_setting),

            (r'/event/create', Create_Event),
            (r'/event/get', Get_Event),

            (r'/blog/create', Create_Blog),
            (r'/blog/edit', Edit_Blog),
            (r'/blog/list', Get_User_Blog),
            (r'/blog/(.*)', Blog_Details),

        ]
        settings = dict(
            debug=True,
            autoreload=True,
            cookie_secret='f72c2505124026952ad55e54664493b1'
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.engine = engine
        self.datebase = scoped_session(sessionmaker(bind=engine,
                                                    autocommit=False, autoflush=True,
                                                    expire_on_commit=False))


def main():
    tornado.options.parse_command_line()
    Application().listen(8088)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
