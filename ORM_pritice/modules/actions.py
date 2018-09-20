#author:xm
#coding:utf-8
import os,sys
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,base)
from sqlalchemy.orm import sessionmaker
from conf import settings
from conf.settings import engine
from modules.models import Teacher,Class
#from .teacher_view import Teacher_Center
from modules.student_view import Student_Center


class Action(object):
    '''主程序入口'''
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.initialize_database()
    def run(self):
        while True:
            print(
                '''
                    欢迎进入CLASS_SYSTEM系统:
                    1.学生视图
                    2.老师视图
                    3.管理视图
                '''
            )
            user_choice = input("请选择要进入的视图，按q退出：")
            if user_choice == "1":
                Student_Center()
            elif user_choice == "2":
                pass
            elif user_choice == "3":
                pass
            elif user_choice == "q":
                print("\033[34;1m感谢使用管理系统,退出\033[0m")
                break
            else:
                print("\033[31;1m请输入正确的选项\033[0m")

    def initialize_database(self):
        '''初始化数据库'''
        rest = self.session.query(Teacher).filter_by(Teacher.teacher_id>0).all()
        if not rest:
            class1 = Class(class_name="S14", course="Python")
            class2 = Class(class_name="S15", course="linux")
            teacher1 = Teacher(teacher_name="Alex")
            #teacher1.classes = [class1]
            self.session.add_all([class1,class2, teacher1])
            self.session.commit()