#author:xm
#coding:utf-8
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

#连接mysql引擎
engine = create_engine("mysql+pymysql://root:Xt2018@58.206.97.104/my_test",encoding='utf-8',echo=True)
Base = declarative_base() #生成orm基类

class User(Base):
    __tablename__ = 'user'#表名
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    password = Column(String(32))

Base.metadata.create_all(engine)#创建表结构

Session_class = sessionmaker(bind=engine)#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()#生成session实例

# user_obj = User(name="xm",password="123456")#创建user实例
# print(user_obj.id,user_obj.name)#此时还没有创建对象
# session.add(user_obj)#将user对象添加到session对象中，但还没有提交

# print(user_obj.id,user_obj.name,user_obj.password)

#查询
#my_user = session.query(User).filter_by(name="xm").all()#生成一个数据库对象
my_user = session.query(User).filter(User.id>1).all()#返回一个列表对象
print(my_user[0].id,my_user[0].name,my_user[0].password)

#修改
my_user1 = session.query(User).filter_by(id=2).first()#first方法直接返回一个对象
my_user1.name = "Jack"

#删除
my_user2 = session.query(User).filter_by(id=3).delete()
session.commit()#这时才将user对象提交到session对象中
