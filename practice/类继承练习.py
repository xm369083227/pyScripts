#author:xm
#coding:utf-8
import json
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = {}#定义学生和老师空字典，后续通过程序关联对象
        self.teachers = {}
        self.course = {}
    #注册学生
    def redister_stu(self):
        print("开始注册学生".center(50, "*"))
        stu_name = input("请输入学生姓名：")
        stu_age = input("请输入学生年龄：")
        stu_gender = input("请输入学生性别：")
        stu_course = input("请输入学生报名课程：")
        stu_tuition = input("请输入学生学费：")
        stu_obj = Student(stu_name,stu_age,stu_gender,stu_course,stu_tuition)
        #循环打印字典中所有的键值对，然后格式化输出
        a = ['%s:%s' % item for item in stu_obj.__dict__.items()]
        if self.students.get(stu_obj.mem_name):
            print("%s学生已经存在，请重新输入"%stu_obj.mem_name)
        else:
            self.students[stu_obj.mem_name] = a
            json.dump(self.students,open("student_db","a+",encoding="utf-8"),ensure_ascii=False, indent=2)

    #雇佣老师
    def hire_tea(self):
        print("开始雇佣老师".center(50, "*"))
        tea_name = input("请输入老师姓名：")
        tea_age = input("请输入老师年龄：")
        tea_gender = input("请输入老师性别：")
        tea_course = input("请输入老师所教课程：")
        tea_tuition = input("请输入老师工资：")
        tea_obj = Teacher(tea_name, tea_age, tea_gender, tea_course, tea_tuition)
        b = ['%s:%s' % item for item in tea_obj.__dict__.items()]
        if self.teachers.get(tea_obj.mem_name):
            print("%s老师已经存在，请重新输入" % tea_obj.mem_name)
        else:
            self.teachers[tea_obj.mem_name] = b
            json.dump(self.teachers, open("teacher_db", "a+", encoding="utf-8"), ensure_ascii=False, indent=2)
    def creat_course(self):
        print("开始创建课程".center(50,"*"))
        course_type = input("请输入课程类型：‘技术/文学/行政/管理’")
        course_name = input("请输入课程名称:")
        course_price = input("请输入课程价格：")
        course_period = input("请输入课程周期：")
        course_obj = Course(course_type,course_name,course_price,course_period)
        course_obj.show_coruse_info()
        # 循环打印字典中所有的键值对，然后格式化输出
        c = ['%s:%s' % item for item in course_obj.__dict__.items()]
        if self.course.get(course_obj.course_name):
            print("%s课程已经存在，请重新输入" % course_obj.course_name)
        else:
            self.course[course_obj.course_name] = c
            json.dump(self.course, open("course_db", "a+", encoding="utf-8"), ensure_ascii=False, indent=2)
class SchoolMember(object):
    def __init__(self,mem_name,mem_age,mem_gender):
        self.mem_name = mem_name
        self.mem_age = mem_age
        self.mem_gender = mem_gender
#学生类继承SchoolMember
class Student(SchoolMember):
    def __init__(self,mem_name,mem_age,mem_gender,stu_course,stu_tuition):
        super(Student,self).__init__(mem_name,mem_age,mem_gender)
        self.stu_course = stu_course
        self.stu_tuition = stu_tuition
    def show_stu_info(self):
        print(("学生%s信息"%self.mem_name).center(50,"*"))
        print(('''
            姓名：%s
            年龄：%s
            性别：%s
            报名课程：%s
            课程学费：%s
        ''')%(self.mem_name,self.mem_age,self.mem_gender,self.stu_course,self.stu_tuition))
#老师类继承SchoolMember
class Teacher(SchoolMember):
    def __init__(self,mem_name,mem_age,mem_gender,tea_course,tea_salary):
        super(Teacher, self).__init__(mem_name,mem_age,mem_gender)
        self.tea_course = tea_course
        self.tea_salary = tea_salary
    def show_tea_info(self):
        print(("老师%s信息"%self.mem_name).center(50,"*"))
        print(('''
            老师姓名：%s
            老师年龄：%s
            老师性别：%s
            所教课程：%s
            老师薪资：%s
        ''')%(self.mem_name,self.mem_age,self.mem_gender,self.tea_course,self.tea_salary))

#课程类
class Course(object):
    def __init__(self, course_type, course_name, course_price, course_period):
        self.course_type = course_type
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period
    def show_coruse_info(self):
        print(("课程%s信息" % self.course_name).center(50, "*"))
        print(('''
                    课程类型：%s
                    课程名称：%s
                    课程价格：%s
                    课程周期：%s
                ''') % (self.course_type, self.course_name, self.course_price, self.course_period))

def students_view():
    while True:
        print('''
            1.注册
            2.返回
            3.退出
        ''')
        num = input("请选择：")
        if num == "1":
            choice_school_obj.redister_stu()
        if num == "2":
            break
        if num == "3":
            exit()
def teacher_view1():
    while True:
        if num2 == "a" or num2 =="b":
            print('''
                                1.查看学生信息
                                2.返回
                                3.退出
                        ''')
            num = input("请选择：")
            if num == "1":
                with open("student_db", "r", encoding="utf-8") as f:
                    for line in f:
                        print(line.strip())
            if num == "2":
                break
            if num == "3":
                exit()

def teacher_view():
    global choice_teacher_obj
    global num2
    while True:
        print('''
            1.选择老师
            2.注册老师
            3.返回
        ''')
        num1 = input("请选择：")
        if num1 == "1":
            print("请选择老师：a.%s，b.%s" % ("Tracy", "kobe"))
            num2 = input("请选择老师：")
            while num2 == "a" or num2 == "b":
                if num2 == "a":
                    choice_teacher_obj = tea1
                if num2 == "b":
                    choice_teacher_obj = tea2
                teacher_view1()
        if num1 == "2":
            print("功能不全，暂时不能注册老师")
        if num1 == "3":
            break
    return num2



school1 = School("信同科技","西安")
school2 = School("阿里巴巴","杭州")
tea1 = Teacher("Tracy",23,"M","linux","15000")
tea2 = Teacher("kobe",24,"M","python","23000")
stu1 = Student("zhangsan",23,"M","linux","6000")
stu2 = Student("lisi",21,"M","python","8000")
def main():
    global choice_school_obj

    while True:
        print("请选择学校".center(50, '*'))
        choice_school = input("1.%s, 2.%s, 3.返回, 4.退出\n" % (school1.name, school2.name))
        if choice_school == '1':
            choice_school_obj = school1  # 将对象引用传给choice_school
        elif choice_school == '2':
            choice_school_obj = school2
        elif choice_school == '3':
            break
        elif choice_school == '4':
           exit()
        else:
            continue
        while True:
            print("1.学员视图\n"
                  "2.讲师视图\n"
                  "3.学校管理视图\n"
                  "4.返回\n"
                  "5.退出")
            num = input("请选择视图:")

            if num == '1':
                print("欢迎进入学员视图".center(50, '*'))
                students_view()
            elif num == '2':
                print("欢迎进入讲师视图".center(50, '*'))
                teacher_view()
            elif num == '3':
                print("欢迎进入学校管理视图".center(50, '*'))
                #school_view()
            elif num == '4':
                break
            elif num == '5':
                exit()
            else:
                continue
if __name__ == "__main__":
    main()



# course1 = Course("技术","linux",1000,"6month")
# course2 = Course("技术","python",13000,"6month")
# course3 = Course("技术","go",8000,"6month")
# stu1.show_stu_info()
# tea1.show_tea_info()
#school.redister_stu()
# school.redister_stu(stu2)
# school.hire_tea(tea1)
# school.creat_course()





