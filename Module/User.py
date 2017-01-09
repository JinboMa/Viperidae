from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String, Integer
from sqlalchemy.ext.declarative import declarative_base
from Log.logger import write

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
        if len(flag) == 0:
            if len(session().query(User.nickname).filter(User.nickname == user.nickname).all()) == 0:
                session().add(user)
                session().commit()
                return True
            else:
                write('INFO', '[User][registration] 昵称已存在')
                return '昵称已存在'
        else:
            write('INFO', '[User][registration] 手机号已存在')
            return '手机号已存在'

    def log_in(self, session, user):
        flag = session().query(User).filter(User.telphone == user.telphone).first()
        if flag is not None:
            if flag.password == user.password:
                return flag
            else:
                write('INFO', '[User][log_in] 密码错误')
                return '密码错误'
        else:
            write('INFO', '[User][log_in] 用户不存在')
            return '用户不存在'
