#author:xm
#coding:utf-8
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,base_dir)
from sqlalchemy import String,Column,Integer,ForeignKey,DATE,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from conf.settings import engine

Base = declarative_base() #生成orm基类

'''设计表结构'''
#学生类
class Student(Base):
    __tablename__ = "student"
    stu_id = Column(Integer(6),primary_key=True)
    stu_name = Column(String(32),nullable=False,unique=True)
    QQ = Column(String(32),nullable=False)
#班级类
class Class(Base):
    "班级"
    __tablename__ ="class"
    class_id = Column(Integer, primary_key=True)
    class_name = Column(String(32), nullable=False,unique=True)
    course =  Column(String(32), nullable=False)
    students = relationship("Student",backref="class")
#教师类
class Teacher(Base):
    "讲师"
    __tablename__ = "teacher"
    teacher_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(32), nullable=False, unique=True)   #唯一
    classes = relationship("Class", backref="teacher")
#课节类
class Lesson(Base):
    __tablename__ = "lesson"
    lesson_id = Column(Integer, primary_key=True)
    lesson_name = Column(String(32), nullable=False, unique=True)
    def __repr__(self):
        return "节次名：【%s】"%self.lesson_name


class Class_m2m_Lesson(Base):
    '''班级和课节对应表'''
    __tablename__ = "class_m2m_lesson"
    id =  Column(Integer, primary_key=True)
    class_id = Column(Integer,ForeignKey("class.class_id"))
    lesson_id = Column(Integer, ForeignKey("lesson.lesson_id"))
    classes = relationship("Class",backref="class_m2m_lesson")
    lessons = relationship("Lesson", backref="class_m2m_lesson")

class Class_m2m_Student(Base):
    '''班级和学生对应表'''
    __tablename__ = "class_m2m_student"
    class_id = Column(Integer(6),ForeignKey("class.class_id"))
    stu_id = Column(Integer(6),ForeignKey("student.stu_id"))

class Teacher_m2m_Class(Base):
    '''老师和班级对应表'''
    __tablename__ = "teacher_m2m_class"
    teacher_id = Column(Integer(6),ForeignKey("teacher.teacher_id"))
    class_id = Column(Integer(6),ForeignKey("class.class_id"))

class Study_record(Base):
    "上课记录"
    __tablename__ = "study_record"
    id = Column(Integer,primary_key=True)
    class_m2m_lesson_id = Column(Integer,ForeignKey("class_m2m_lesson.id"))
    stu_id = Column(Integer, ForeignKey("student.stu_id"))
    status = Column(String(32),nullable=False)
    score = Column(Integer,nullable=True)
    class_m2m_lessons = relationship("Class_m2m_Lesson",backref="study_record")
    students = relationship("Student", backref="study_record")