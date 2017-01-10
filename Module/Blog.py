from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from Module.User import User
from Log.logger import write, space

Base = declarative_base()


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer(), primary_key=True, autoincrement=True)  # 主键
    title = Column(String(20))  # 标题
    content = Column(String(20000))  # 内容
    author = Column(Integer(), ForeignKey(User.id))  # 所属
    create_time = Column(DateTime())  # 创建时间
    release_time = Column(DateTime())  # 发布时间
    last_edit_time = Column(DateTime())  # 最后编辑时间

    def create(self, session, blog):
        session.add(blog)
        try:
            session.commit()
            return True
        except Exception as e:
            write('ERROR', '[Blog] error:{}'.format(e))
            space()
            return False
        finally:
            session().close()

    def get_blog_by_id(self, session, blog_id):
        blog = session().query(Blog).get(blog_id)
        session().close()
        if blog is not None:
            return blog
        else:
            return None

    def get_blogs_by_author(self, session, user_id):
        blogs = session().query(Blog).filter(Blog.author == user_id).all()
        if len(blogs) != 0:
            return blogs
        else:
            return None

    def edit_blog(self, session, id, user_id, title, content, last_edit_time):
        blog = session().query(Blog).get(id)
        session().close()
        if blog is not None:
            if str(blog.author) == user_id:
                blog.title = title
                blog.content = content
                blog.last_edit_time = last_edit_time
                try:
                    session().commit()
                    return True
                except Exception as e:
                    print(str(e))
                    return '数据库操作失败'
            else:
                return '这不是你的文章'
        else:
            return '没有这篇blog'
