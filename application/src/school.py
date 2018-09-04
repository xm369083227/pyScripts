#author:xm
#coding:utf-8
import os
from src.course import Course
from src.classroom import Classroom
from src.teacher import Teacher
from src.student import Student

class School(object):
    def __init__(self,sch_name,sch_addr):
        self.sch_name = sch_name
        self.sch_addr = sch_addr
        self.sch_teacher = {}
        self.sch_classroom = {}
        self.sch_course = {}
        self.sch_student = {}

    def create_course(self,course_name,course_price,course_time):
        #创建课程对象
        #根据课程名称为key，课程对象为value来建立对应关系
        sch_course_obj = Course(course_name,course_price,course_time)
        self.sch_course[course_name] = sch_course_obj

    def show_course(self):
        '''
        查看课程
        :return:
        '''
        for course_key in self.sch_course:
            show_course_obj = self.sch_course[course_key]
            print("\033[32;1m课程名称【%s】\t课程价格【%s】\t课程周期【%s】\033[0m"
                  % (show_course_obj.course_name,show_course_obj.course_price,show_course_obj.course_time))

    # def modify_course(self,**kwargs):
    # 根据key取出课程对象
    # for course in self.sch_course:
    #     course_obj = self.sch_course[course]
    # 修改course_obj的每个值
    # 保存

    def create_classroom(self,claroom_name,course_obj):
        #添加教师
        sch_classroom_obj = Classroom(claroom_name,course_obj)
        self.sch_classroom[claroom_name] = sch_classroom_obj

    def show_classroom(self):
        #查看教师
        for claroom_key in self.sch_classroom:
            show_claroom_obj = self.sch_classroom[claroom_key]
        for teacher_key in self.sch_teacher:
            teacher_name_obj = self.sch_teacher[teacher_key]
            print("\033[32;1m班级名称【%s】\t班级课程【%s】\t主讲教师【%s】\033[0m"%(show_claroom_obj.cls_name,
                                                    show_claroom_obj.cls_course_obj.course_name
                                                                   ,teacher_name_obj.tea_name))

    def create_teacher(self,sch_tea_name,sch_tea_sal,tea_class_name,class_obj):
        '''
        添加老师
        :param sch_tea_name:
        :param sch_tea_sal:
        :param tea_class_name:
        :param class_obj:
        :return:
        '''
        sch_teacher_obj = Teacher(sch_tea_name,sch_tea_sal)
        sch_teacher_obj.add_tea_class(tea_class_name,class_obj)
        self.sch_teacher[sch_tea_name] = sch_teacher_obj

    def show_teacher(self,*args):
        '''
        查看教师信息
        :return:
        '''
        for show_teacher_key in self.sch_teacher:
            show_teacher_obj = self.sch_teacher[show_teacher_key]
            class_list = []
            for tea_class_key in show_teacher_obj.tea_class:
                class_list.append(tea_class_key)
            print("\033[32;1m讲师名称【%s】讲师薪资【%s】关联班级【%s】\033[0m"
                  %(show_teacher_obj.tea_name,
                    show_teacher_obj.tea_sal,class_list))

    def update_teacher(self,update_tea_name,update_class_name,update_class_obj):
        '''
        更新教师信息
        :param update_tea_name: 更新教师姓名
        :param update_class_name: 更新教师班级名称
        :param update_class_obj: 更新教师班级内容
        :return:
        '''
        update_teacher_obj = self.sch_teacher[update_tea_name]
        update_teacher_obj.add_tea_class(update_class_name,update_class_obj)

    def create_student(self,sch_stu_name,sch_stu_age,sch_stu_sex,cls_name):
        '''
        创建学生
        :param sch_stu_name:学生姓名
        :param sch_stu_age: 学生年龄
        :param sch_stu_sex: 学生性别
        :param cls_name: 班级名称
        :return:
        '''
        sch_stu_obj = Student(sch_stu_name,sch_stu_age,sch_stu_sex)
        stu_class_obj = self.sch_classroom[cls_name]
        stu_class_obj.cls_student[sch_stu_name] = sch_stu_obj
        self.sch_classroom[cls_name] = stu_class_obj

    def show_stu_classroom(self):
        #学生视图查看班级学员信息
        for classroom_name_key in self.sch_classroom:
            cls_name_obj = self.sch_classroom[classroom_name_key]
            stu_list = []
            for cls_stu_name in cls_name_obj.cls_student:
                stu_list.append(cls_stu_name)
            print("\033[32;1m班级名称【%s】\t班级课程【%s】\t学员【%s】\033[0m"
                  %(cls_name_obj.cls_name,cls_name_obj.cls_course_obj.course_name,stu_list))

    def show_tea_clsinfo(self,tea_name):
        '''
        教师视图查看班级 学员信息
        :param tea_name:
        :return:
        '''
        show_teainfo_obj = self.sch_teacher[tea_name]
        for cls_info in show_teainfo_obj.tea_class:
            cls_info_obj = self.sch_classroom[cls_info]
            stu_list = []
            for stu_info in cls_info_obj.cls_student:
                stu_list.append(stu_info)
            print('\033[32;1m班级【%s】\t关联课程【%s】\t学员【%s】\033[0m'%(cls_info_obj.cls_name,
                                              cls_info_obj.cls_course_obj.course_name,stu_list))