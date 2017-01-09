from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from Log.logger import get_logging

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))
    nickname = Column(String(20))
    password = Column(String(30))
    email = Column(String(30))
    telphone = Column(String(20))
    registration_time = Column(DateTime())
    picture = Column(String(30))
    id_number = Column(String(30))

    def registration(self, session, user):
        flag = session().query(User).filter(User.telphone == user.telphone).all()
        get_logging().info('[User][registration] id:{}'.format(flag.id))
        if len(flag) == 0:
            if len(session().query(User.nickname).filter(User.nickname == user.nickname).all()) == 0:
                session().add(user)
                session().commit()
                return True
            else:
                get_logging().info('[User][registration] 昵称已存在')
                return '昵称已存在'
        else:
            get_logging().info('[User][registration] 手机号已存在')
            return '手机号已存在'

    def log_in(self, session, user):
        flag = session().query(User).filter(User.telphone == user.telphone).first()
        get_logging().info('[User][log_in] id:{}'.format(flag.id))
        if flag is not None:
            print('user id : {}'.format(flag.id))
            if flag.password == user.password:
                return flag
            else:
                get_logging().info('[User][log_in] 密码错误')
                return '密码错误'
        else:
            get_logging().info('[User][log_in] 用户不存在')
            return '用户不存在'
