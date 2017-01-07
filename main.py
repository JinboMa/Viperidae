import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from personal_project.Business.log_in import Log_in
from personal_project.Business.registration import Registration


class Application(tornado.web.Application):
    def __init__(self):
        engine = create_engine("mysql+pymysql://root:xuzhaoning@localhost:3306/test", echo=True)

        handlers = [
            (r'/login', Log_in),
            (r'/registration', Registration)
        ]
        settings = dict(
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.engine = engine
        self.datebase = scoped_session(sessionmaker(bind=engine,
                                                    autocommit=False, autoflush=True,
                                                    expire_on_commit=False))


def main():
    tornado.options.parse_command_line()
    Application().listen(8080)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
