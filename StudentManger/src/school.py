#author:xm
#coding:utf-8
import os,sys,platform
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,BASE_DIR)
# #print(sys.path)
from .classroom import Classroom
from .course import Course
from .teacher import Teacher
from .student import Student

class School(object):
    '''学校类包含名称，地址，课程，班级，老师等'''
    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_classroom = {}
        self.school_course = {}
        self.school_teacher = {}

    def create_course(self, course_name, course_price, course_time):
        '''创建课程'''
        course_obj = Course(course_name, course_price, course_time)
        '''将课程对象传给学校课程，使之关联'''
        self.school_course[course_name] = course_obj

    def show_course(self):
        '''查看课程信息'''
        for key in self.school_course:
            course_obj = self.school_course[key]
            print("\33[32;1m课程：%s\t价格：%s\t周期：%s月\33[0m" % (course_obj.course_name, course_obj.course_price,
                                                           course_obj.course_time,))
    def create_class(self,class_name,course_obj):
        class_obj = Classroom(class_name, course_obj)
        self.school_classroom[class_name] = class_obj

    def show_class(self):
        for key in self.school_classroom:
            class_obj = self.school_classroom[key]
            print("\33[32;1m班级：%s\t关联课程：%s\33[0m" % (class_obj.class_name, class_obj.class_course.course_name))

    def show_class_course(self):
        for key in self.school_classroom:
            class_obj = self.school_classroom[key]
            course_obj = class_obj.class_course
            print("\33[32;1m班级：%s\t关联课程：%s\t价格：%s\t周期：%s月\33[0m" % (class_obj.class_name, course_obj.course_name,
                                                                    course_obj.course_price, course_obj.course_time))

    def create_teacher(self, teacher_name, teacher_salary, class_name, class_obj):
        '''创建讲师'''
        teacher_obj = Teacher(teacher_name, teacher_salary)
        teacher_obj.teacher_add_class(class_name, class_obj)
        self.school_teacher[teacher_name] = teacher_obj

    def update_teacher(self, teacher_name, class_name, class_obj):
        '''更新教师信息'''
        teacher_obj = self.school_teacher[teacher_name]
        teacher_obj.teacher_add_class(class_name, class_obj)

    def show_teacher(self):
        '''查看讲师信息'''
        for key in self.school_teacher:
            teacher_obj = self.school_teacher[key]
            class_list = []
            for i in teacher_obj.teacher_class:
                class_list.append(i)
            print("\33[32;1m讲师：%s\t薪资：%s\t关联班级：%s\33[0m" % (teacher_obj.teacher_name, teacher_obj.teacher_salary,
                                                            class_list))

    def create_student(self, student_name, student_age, class_choice):
        '''注册学生'''
        student_obj = Student(student_name, student_age)  # 生成学生实例
        class_obj = self.school_classroom[class_choice]  # 获取学生所注册班级的实例对象
        class_obj.class_student[student_name] = student_obj  # 班级实例里添加学生信息
        self.school_classroom[class_choice] = class_obj  # 学校班级字典更新

    def show_teacher_classinfo(self, teacher_name):
        teacher_obj = self.school_teacher[teacher_name]
        for i in teacher_obj.teacher_class:
            class_obj = self.school_classroom[i]
            student_list = []
            for k in class_obj.class_student:
                student_list.append(k)
            print("\33[32;1m班级：%s\t关联课程：%s\t学员:%s\33[0m" % (class_obj.class_name, class_obj.class_course.course_name,
                                                            student_list))