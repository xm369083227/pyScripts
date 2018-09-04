#author:xm
#coding:utf-8
import os,shelve,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting
from src.school import School
from src.classroom import Classroom
from src.course import Course
from src.student import Student
from src.teacher import Teacher

class Count(object):
    '''
    主目录运行类
    '''
    exit_flag = False
    def run(self):
        menu = '''            
            1、学生视图
            2、教师视图
            3、学校视图
            '''
        while True:
            print("\033[35;1m欢迎来的选课系统CRM\033[0m".center(50,"="))
            print(menu)
            user_option = input("\033[34;1m请选择视图...按Q退出>>>:\033[0m").strip()
            if user_option == "1":
                Student_view()
            elif user_option == "2":
                Teacher_view()
            elif user_option == "3":
                School_view()
            elif user_option.capitalize() == "Q":
                break
            else:
                print("\033[31;1m请选择有效视图\033[0m")

class Teacher_view(object):
    '''
    讲师视图类
    '''
    def __init__(self):
        if os.path.exists(setting.school_file + '.dat'):
            self.school_file = shelve.open(setting.school_file)
            self.teacher_manager()
            self.school_file.close()
        else:
            print("\033[31;1m无数据文件请先创建学校\033[0m")
            exit()

    def teacher_manager(self):
        '''
        定义一个讲师管理模块
        :return:
        '''
        while True:
            for sch_name in self.school_file:
                print("学校名称【%s】"%sch_name)
            sch_option = input('请选择管理的学校按b返回>>>:').strip()
            if sch_option in self.school_file:
                self.sch_option = sch_option
                self.sch_obj = self.school_file[sch_option]
                print("学校地址【%s】"%self.sch_obj.sch_addr)
                teaname_option = input('请输入登录讲师姓名>>>:').strip()
                while True:
                    if teaname_option in self.sch_obj.sch_teacher:
                        menu = '''                        欢迎【%s】来到教师中心
                        1、查看讲师信息  show_teacher
                        2、查看班级学员  show_classroom
                        3、退出    exit
                        '''%teaname_option
                        print(menu)
                        menu_option = input('请输入操作命令按b返回>>>:').strip()
                        if hasattr(self,menu_option):
                            getattr(self,menu_option)(teaname_option)
                        elif menu_option == 'b':
                            break
                        else:
                            print('\033[31;1m请输入有效操作命令\033[0m')
                    else:
                        print("\033[31;1m讲师不存在请先创建\033[0m")
                        break
            elif sch_option == "b":
                break
            else:
                print('\033[31;1m请输入有效学校名\033[0m')

    def show_teacher(self,*args):
        '''
        查看班级模块
        :return:
        '''
        self.sch_obj.show_teacher(*args)
        if len(self.sch_obj.sch_classroom) == 0:
            print('\033[31;1m该讲师暂无班级\033[0m')

    def show_classroom(self,teaname_option):
        self.sch_obj.show_tea_clsinfo(teaname_option)
        if len(self.sch_obj.sch_classroom) == 0:
            print('\033[31;1m该讲师暂无班级\033[0m')

    def exit(self,*args):
        '''
        退出程序模块
        :return:
        '''
        self.school_file.close()
        exit("\033[32;1m欢迎下次使用学员管理系统\033[0m")


class School_view(object):
    '''
    学校管理视图：根据校区创建课程、班级、教师信息
    '''
    def __init__(self):
        if os.path.exists(setting.school_file + ".dat"):
            self.school_file = shelve.open(setting.school_file)
            self.school_manager()
            self.school_file.close()
        else:
            print("\033[31;1m没有数据文件请先创建\033[0m")
            self.init_school()
            self.school_manager()
            self.school_file.close()

    def init_school(self):
        '''
        创建学校的模块
        :return:
        '''
        self.school_file = shelve.open(setting.school_file)
        self.school_file["北京"] = School('北京',"北京总校")
        self.school_file["上海"] = School("上海","上海分校")

    def school_manager(self):
        '''
        定义一个学校管理模块
        :return:
        '''
        while True:
            for sch_name in self.school_file:
                print("学校名称【%s】"%(sch_name))
            sch_option = input("请选择管理校区按b返回>>>:").strip()
            if sch_option in self.school_file:
                self.sch_option = sch_option
                self.sch_obj = self.school_file[sch_option]
                print("学校地址【%s】"%self.sch_obj.sch_addr)
                while True:
                    menu = u'''                        欢迎来到老男孩【%s】校区
                        1、添加课程  add_course
                        2、添加班级  add_classroom
                        3、添加讲师  add_teacher
                        4、查看班级  show_classroom
                        5、查看课程  show_course
                        6、查看讲师  show_teacher
                        7、退出    exit
                    ''' %(self.sch_obj.sch_name)
                    print(menu)
                    menu_option = input("请选择以上操作命令按b返回>>>:").strip()
                    if hasattr(self,menu_option):
                        getattr(self,menu_option)()
                    else:
                        print("\033[31;1m请输入有效命令\033[0m")
            elif sch_option == 'b':
                break
            else:
                print('\033[31;1m请选择正确的学校名\033[0m')

    def add_course(self):
        '''
        添加课程模块
        :return:
        '''
        add_course_name = input("请输入课程名称>>>:")
        add_course_pice = input("请输入课程价格>>>:")
        add_course_time = input('请输入课程周期>>>:')
        if add_course_name in self.sch_obj.sch_course:
            print('\033[31;1m课程已存在\033[0m')
            # self.sch_obj.create_course(add_course_name,add_course_pice,add_course_time)
            # print("课程更新成功")
        else:
            self.sch_obj.create_course(add_course_name,add_course_pice,add_course_time)
            print('\033[32;1m课程添加成功\033[0m')
        self.school_file.update({self.sch_option:self.sch_obj})

    def add_classroom(self):
        '''
        添加教师模块
        :return:
        '''
        add_cla_name = input("请输入班级名称>>>:")
        add_clacourse_name = input("请输入关联课程名称>>>:")
        if add_cla_name not in self.sch_obj.sch_classroom:  #判断需添加的教室名称 不在学校教师方法中
            if add_clacourse_name in self.sch_obj.sch_course:   #判断 需添加的教室课程名称 在学校课程中
                class_course_obj = self.sch_obj.sch_course[add_clacourse_name]  #将需添加的课程名称 添加到班级中
                self.sch_obj.create_classroom(add_cla_name,class_course_obj)
                print('\033[32;1m班级添加成功\033[0m')
                self.school_file.update({self.sch_option:self.sch_obj})
            else:
                print("\033[31;1m课程不存在\033[0m")
        else:
            print("\033[31;1m班级已存在\033[0m")

    def add_teacher(self):
        '''
        添加教师模块
        :return:
        '''
        add_teacher_name = input('请输入招聘老师姓名>>>:').strip()
        add_teacher_slary = input('请输入老师薪资>>>:').strip()
        teacher_class_name = input('请输入老师关联班级>>>:').strip()
        if teacher_class_name in self.sch_obj.sch_classroom:   #判断输入的班级名称是否在sch_classroom中
            teacher_class_obj = self.sch_obj.sch_classroom[teacher_class_name]  #将输入的班级名称添加到学校教师字典中
            if add_teacher_name not in self.sch_obj.sch_teacher: #判断输入讲师名称是否在sch_teacher中
                self.sch_obj.create_teacher(add_teacher_name,add_teacher_slary,teacher_class_name,teacher_class_obj)
                #在添加讲师模块中加入 add_teacher_name,add_teacher_salary,teacher_class_name,teacher_class_obj
                print("\33[32;1m新讲师招聘成功\33[0m")
            else:
                self.sch_obj.update_teacher(add_teacher_name,teacher_class_name,teacher_class_obj)
                print("\33[32;1m讲师已经存在，信息更新完成\33[0m")
            self.school_file.update({self.sch_option:self.sch_obj})
        else:
            print("\33[31;1m系统错误：关联的班级不存在\33[0m")

    def show_course(self):
        '''
        查看课程模块
        :return:
        '''
        self.sch_obj.show_course()
        if len(self.sch_obj.sch_course) == 0:
            print("\033[31;1m该校区暂无课程\033[0m")

    def show_classroom(self):
        '''
        查看教室模块
        :return:
        '''
        self.sch_obj.show_classroom()
        if len(self.sch_obj.sch_classroom) == 0:
            print("\033[31;1m该校区暂无班级\033[0m")

    def show_teacher(self):
        '''
        查看教师模块
        :return:
        '''
        self.sch_obj.show_teacher()
        if len(self.sch_obj.sch_teacher) == 0:
            print("\033[31;1m该校区暂无教师\033[0m")

    def exit(self):
        '''
        退出程序模块
        :return:
        '''
        self.school_file.close()
        exit("\033[32;1m欢迎下次使用学员管理系统\033[0m")


class Student_view(object):
    '''
    学生视图
    '''
    def __init__(self):
        if os.path.exists(setting.school_file + '.dat'):
            self.school_file = shelve.open(setting.school_file)
            self.student_manager()
            self.school_file.close()
        else:
            exit('数据文件不存在请先创建学校')

    def student_manager(self):
        while True:
            for sch_name in self.school_file:
                print('学校名称【%s】'%sch_name)
            sch_option = input("请选择注册学校按b返回>>>:").strip()
            if sch_option in self.school_file:
                self.sch_option = sch_option
                self.sch_obj = self.school_file[sch_option]
                print("学校地址：【%s】"%self.sch_obj.sch_addr)
                while True:
                    menu = '''                      欢迎来到【%s】校区
                    1、查看课程  show_course
                    2、查看班级  show_classroom
                    3、注册班级课程    add_stu
                    4、查看学生班级    show_stu_classroom
                    5、退出    exit
                    '''%self.sch_obj.sch_name
                    print(menu)
                    menu_option = input('请输入操作命令按b返回>>>:').strip()
                    if hasattr(self,menu_option):
                        getattr(self,menu_option)()
                    elif menu_option == 'b':
                        break
                    else:
                        print('\033[31;1m请输入有效操作命令\033[0m')
            elif sch_option == 'b':
                break
            else:
                print('\033[31;1m学校不存在\033[0m')

    def add_stu(self):
        add_stu_name = input('请输入注册学生姓名>>>:').strip()
        add_stu_age = input('请输入注册学生年龄>>>:').strip()
        add_stu_sex = input('请输入注册学生性别>>>:').strip()
        add_stu = input('请输入注册班级>>>:').strip()
        if add_stu in self.sch_obj.sch_classroom:
            if add_stu_name not in self.sch_obj.sch_student:
                self.sch_obj.create_student(add_stu_name,add_stu_age,add_stu_sex,add_stu)
                print("\033[32;1m学生注册成功\033[0m")
                self.school_file.update({self.sch_option:self.sch_obj})
            else:
                print("\033[31;1m该学生已注册\033[0m")
        else:
            print("\033[31;1m该班级不存在\033[0m")

    def show_course(self):
        self.sch_obj.show_course()
        if len(self.sch_obj.sch_course) == 0:
            print('\033[31;1m该校区暂无课程\033[0m')

    def show_classroom(self):
        self.sch_obj.show_classroom()
        if len(self.sch_obj.sch_classroom) == 0:
            print('\033[31;1m该校区暂无班级\033[0m')

    def show_stu_classroom(self):
        self.sch_obj.show_stu_classroom()

    def exit(self):
        self.school_file.close()
        exit("欢迎下次继续使用课程管理系统")