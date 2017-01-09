from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String, Integer
from sqlalchemy.ext.declarative import declarative_base
from Log.logger import write

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))  # 真实姓名
    nickname = Column(String(20))  # 昵称
    password = Column(String(30))  # 密码
    email = Column(String(30))  # 邮箱
    telphone = Column(String(20))  # 电话号码
    registration_time = Column(DateTime())  # 注册时间
    picture = Column(String(30))  # 头像
    id_number = Column(String(30))  # 身份证号

    def registration(self, session, user):
        flag = session().query(User).filter(User.telphone == user.telphone).all()
        if len(flag) == 0:
            if len(session().query(User.nickname).filter(User.nickname == user.nickname).all()) == 0:
                session().add(user)
                session().commit()
                return True
            else:
                return '昵称已存在'
        else:
            return '手机号已存在'

    def log_in(self, session, user):
        flag = session().query(User).filter(User.telphone == user.telphone).first()
        if flag is not None:
            if flag.password == user.password:
                return flag
            else:
                return '密码错误'
        else:
            return '用户不存在'
