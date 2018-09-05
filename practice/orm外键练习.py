#author:xm
#coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

#连接mysql引擎，echo为程序运行信息的启动开关
engine = create_engine("mysql+pymysql://root:Xt2018@58.206.97.104/test1",encoding='utf-8',echo=True)
Base = declarative_base() #生成orm基类

class Student(Base):
    __tablename__ = 'student'#表名
    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=False)
    register_date = Column(DATE,nullable=False)
    gender = Column(String(32),nullable=False)

class Study(Base):
    __tablename__ = 'study_record'#表名
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey("student.id"))#关联到student表的id
    #通过此关系可以在study中直接调用my_record字段查询student中的对象
    student = relationship("Student", backref="my_record")

Base.metadata.create_all(engine)#创建表结构
Session_class = sessionmaker(bind=engine)#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()#生成session实例

# s1 = Student(name="xm",register_date="2018-09-05",gender="M")
# s2 = Student(name="uzi",register_date="2018-08-05",gender="M")
# s3 = Student(name="mlxg",register_date="2018-07-05",gender="M")
# s4 = Student(name="faker",register_date="2018-06-05",gender="M")
#
# #1代表xm，2代表uzi
# stu_obj1 = Study(day=1,status="YES",stu_id=1)
# stu_obj2 = Study(day=2,status="NO",stu_id=1)
# stu_obj3 = Study(day=3,status="YES",stu_id=1)
# stu_obj4 = Study(day=4,status="YES",stu_id=2)
#
# #将对象实例添加进数据库session
# session.add_all([s1,s2,s3,s4,stu_obj1,stu_obj2,stu_obj3,stu_obj4])

#以“xm”为关键字查出所有xm的行
stu_obj = session.query(Student).filter(Student.name=="xm").all()
#可以通过Student对象以my_record字段查出Study对象中的属性
print("teacher:"+stu_obj[0].name,"day:",stu_obj[0].my_record[0].day,"status:"+stu_obj[0].my_record[0].status)
session.commit()#提交
