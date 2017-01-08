from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .User import User

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
    belong = Column(Integer(), ForeignKey(User.id))

    def get_event_by_id(self, session, user_id):
        events = session().query(Event.id, Event.event_name, Event.remarks, Event.priority).filter(
            Event.belong == user_id).all()
        if len(events) == 0:
            return None
        else:
            return events

    def create_event(self, session, event):
        session.add(event)
        session.commit()
        return True


if __name__ == '__main__':
    engine = create_engine(
        "mysql+pymysql://root:xuzhaoning@23.105.208.8:3306/personal?charset=utf8",
        echo=True)

    Base.metadata.create_all(engine)