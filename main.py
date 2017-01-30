import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from Configuration import *
from Resources.Picture import Picture
from Business.User import *
from Business.Blog import *
from Business.Event import *


class Application(tornado.web.Application):
    def __init__(self):
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
            (r'/blog/list', Blog_List),
            (r'/blog', Blog_Details),

        ]

        settings = dict(
            debug=TORNADO_DEBUG,
            autoreload=False,
            cookie_secret='f72c2505124026952ad55e54664493b1'
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        self.engine = create_engine(
            'mysql+pymysql://' + DATABASE['USERNAME'] + ':' + DATABASE['PASSWORD'] + '@' + DATABASE['HOST'] + ':' +
            DATABASE['POST'] + '/personal?charset=utf8',
            echo=DATABASE_DEBUG)

        self.datebase = scoped_session(
            sessionmaker(
                bind=self.engine,
                autocommit=False,
                autoflush=True,
                expire_on_commit=False
            )
        )


def main():
    application = Application()
    server = tornado.httpserver.HTTPServer(application)
    server.bind(8088)
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
