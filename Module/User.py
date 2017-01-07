from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String, Integer
from sqlalchemy.ext.declarative import declarative_base

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
            session().add(user)
            session().commit()
            return True
        else:
            return '手机号已存在'

    def log_in(self, session, user):
        user = session().query(User).filter(User.telphone == user.telphone).first()
        if user is not None and user.password == user.password:
            return user
        else:
            return False