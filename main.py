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


class Application(tornado.web.Application):
    def __init__(self):
        # engine = create_engine(
        #     "mysql+pymysql://youdian_test1:youdian@test1@shouzhan1.51fubei.com:3306/youdian_online?charset=utf8",
        #     echo=True)

        engine = create_engine(
            "mysql+pymysql://root:xuzhaoning@localhost:3306/test?charset=utf8",
            echo=True)

        handlers = [
            (r'/login', Log_in),
            (r'/registration', Registration),
            (r'/user/setting', User_setting),

            (r'/event/create_event', Create_Event),
            (r'/event/get_event', Get_Event),
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
