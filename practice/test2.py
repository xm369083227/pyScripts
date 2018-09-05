#author:xm
#coding:utf8

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def prn_obj(obj):
        print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
s = Student("zhangsan",22)


print(s.prn_obj())