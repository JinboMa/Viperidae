from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DateTime, Float
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from Module.User import User
from Module.Blog import Blog

Base = declarative_base()


class Blog_Rate_Recording(Base):
    __tablename__ = 'blog_rate_recording'

    id = Column(Integer(), primary_key=True, autoincrement=True)  # 主键
    user_id = Column(Integer(), ForeignKey(User.id))
    blog_id = Column(Integer(), ForeignKey(Blog.id))
    rate = Column(Float())
    time = Column(DateTime())

    def add_blog_rate_recording(self, session, recording):
        rate = session().query(Blog_Rate_Recording).filter(Blog_Rate_Recording.blog_id == recording.blog_id).filter(
            Blog_Rate_Recording.user_id == recording.user_id).all()

        if len(rate) == 0:
            session().add(recording)
            try:
                session().commit()
            except Exception:
                session().rollback()
                return '数据库操作失败'
            else:
                return True
            finally:
                session().close()
        else:
            return '已经打过分了'
