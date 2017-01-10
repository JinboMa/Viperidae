from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from Module.User import User
from Log.logger import write, space

Base = declarative_base()


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer(), primary_key=True, autoincrement=True)  # 主键
    event_name = Column(String(50))  # 时间名称
    remarks = Column(String(100))  # 备注
    priority = Column(Integer())  # 优先级
    created_time = Column(DateTime())  # 创建时间
    end_time = Column(DateTime())  # 结束时间
    is_open = Column(Boolean())  # 是否公开
    status = Column(String(20))  # 状态
    off_time = Column(DateTime())  # 关闭时间
    belong = Column(Integer(), ForeignKey(User.id))  # 所属

    def get_event_by_id(self, session, user_id):
        events = session().query(Event.id, Event.event_name, Event.remarks, Event.priority).filter(
            Event.belong == user_id).all()
        if len(events) == 0:
            return None
        else:
            return events

    def create_event(self, session, event):
        session.add(event)
        try:
            session.commit()
            return True
        except Exception as e:
            write('ERROR', e)
            space()
            return False
        finally:
            session().close()
