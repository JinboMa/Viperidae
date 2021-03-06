from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from Module.User import User

Base = declarative_base()


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer(), primary_key=True, autoincrement=True)  # 主键
    title = Column(String(20))  # 标题
    content = Column(String(20000))  # 内容
    description = Column(String(50))  # 说明
    author = Column(Integer(), ForeignKey(User.id))  # 所属
    create_time = Column(DateTime())  # 创建时间
    release_time = Column(DateTime())  # 发布时间
    last_edit_time = Column(DateTime())  # 最后编辑时间
    rate = Column(Float())

    def create(self, session, blog):
        session().add(blog)
        try:
            session().commit()
        except Exception as e:
            session().rollback()
            return str(e)
        else:
            return True
        finally:
            session().close()

    def get_blog_by_id(self, session, blog_id):
        blog = session().query(Blog).get(blog_id)
        session().close()
        if blog is not None:
            return blog
        else:
            return None

    def get_blogs_by_author(self, session, user_id, start_id, number):

        blogs = session().query(Blog).filter(Blog.author == user_id).filter(Blog.id >= start_id).order_by(
            'last_edit_time')[0:int(number)]
        session().close()
        if len(blogs) != 0:
            return blogs
        else:
            return None

    def edit_blog(self, session, id, user_id, title, content, description, last_edit_time):
        blog = session().query(Blog).get(id)
        if blog is not None:
            if str(blog.author) == user_id:
                blog.title = title
                blog.content = content
                blog.description = description
                blog.last_edit_time = last_edit_time
                try:
                    session().commit()
                    return True
                except Exception as e:
                    session().rollback()
                    return '数据库操作失败'
                finally:
                    session().close()
            else:
                session().close()
                return '这不是你的文章'
        else:
            session().close()
            return '没有这篇blog'

    def update_rate(self, session, blog_id, rate):
        blog = session().query(Blog).get(blog_id)

        if blog.rate is None:
            blog.rate = rate
        else:
            blog.rate = (blog.rate + rate) / 2.0
        try:
            session().commit()
        except Exception:
            session().rollback()
            return '数据库操作失败'
        else:
            return True
        finally:
            session().close()
