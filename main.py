import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from Resources.Picture import Picture
from Business.User import *
from Business.Blog import *
from Business.Event import *


class Application(tornado.web.Application):
    def __init__(self):
        engine = create_engine(
            "mysql+pymysql://root:xuzhaoning@23.105.208.8:3306/personal?charset=utf8",
            echo=False)

        handlers = [

            # --------------Tool-------------- #
            (r'/picture', Picture),
            # --------------Tool-------------- #

            # --------------User-------------- #
            (r'/login', Log_In),
            (r'/logout', Log_Out),
            (r'/registration', Registration),
            (r'/user/setting', User_Setting),
            # --------------User-------------- #

            (r'/event/create', Create_Event),
            (r'/event/get', Get_Event),

            (r'/blog/create', Create_Blog),
            (r'/blog/edit', Edit_Blog),
            (r'/blog/list', Get_User_Blog),
            (r'/blog', Blog_Details),

        ]

        settings = dict(
            debug=False,
            autoreload=False,
            cookie_secret='f72c2505124026952ad55e54664493b1'
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.engine = engine
        self.datebase = scoped_session(sessionmaker(bind=engine,
                                                    autocommit=False, autoflush=True,
                                                    expire_on_commit=False))


def main():
    application = Application()
    server = tornado.httpserver.HTTPServer(application)
    server.bind(8088)
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
