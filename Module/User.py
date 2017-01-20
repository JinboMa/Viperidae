from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))  # 真实姓名
    nickname = Column(String(20))  # 昵称
    password = Column(String(50))  # 密码
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
                try:
                    session().commit()
                except Exception as e:
                    session().rollback()
                    return str(e)
                else:
                    return True
                finally:
                    session().close()
            else:
                return '昵称已存在'
        else:
            return '手机号已存在'

    def verification_by_phone(self, session, user):
        flag = session().query(User).filter(User.telphone == user.telphone).first()
        session().close()
        if flag is not None:
            if flag.password == user.password:
                return flag
            else:
                return '密码错误'
        else:
            return '用户不存在'

    def verification_by_id(self, session, user):
        flag = session().query(User).get(user.id)
        session().close()
        if flag is not None:
            if flag.password == user.password:
                return flag
            else:
                return '密码错误'
        else:
            return '用户不存在'

    def setting(self, session, id, info):
        if isinstance(info, dict):
            user = session().query(User).get(id)
            user.name = info['name']
            user.nickname = info['nickname']
            user.password = info['password']
            user.email = info['email']
            user.telphone = info['telphone']
            user.picture = info['picture']
            user.id_number = info['id_number']
            try:
                session().commit()
            except Exception as e:
                session().rollback()
                self.logger.error('commit false, error:{}'.format(e))
                return False
            else:
                return True
            finally:
                self.session().close()
        else:
            return False

    def get_user_by_id(self, session, user_id):
        user = session().query(User).get(user_id)
        session().close()
        return user
