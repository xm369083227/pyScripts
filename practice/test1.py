import  sys,time,json,datetime
'''
for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)

def test(x,*args,**kwargs):
    print(x,args,kwargs)
test(1,2,3,y=2)
'''
data = {
    'name':'zhangsan',#字典推荐使用单引号，json串使用双引号
    'age':23,
    'gender':'male'
}
# print(data)
str = json.dumps(data)
print(str)
print(json.loads(str))


print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d %H:%M:%S"))

class Dog(object):
    name = "xm"
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def bluck(self):
        print("wang!")
    def test(self):
        print(Dog.name)
    def test1(self):
        print(self.__age)
d = Dog("catte",4)
d.name = "abc"#先找实例name，再找类name
d.bluck()
# d.test()
# d.test1()

# class Teacher(object):
#     def __init__(self,tea_name,tea_sal):
#         self.tea_name = tea_name
#         self.tea_sal = tea_sal
#         self.tea_class = {}
#
#     def add_tea_class(self,self.name,tea_class_obj):
#         self.tea_class[self.name] = tea_class_obj
#
# t = Teacher("uzi",5000)
# print(t.tea_class)
# print(("学生%s信息"%t.tea_name).center(50,"*"))

class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s is eating.."%self.name)
def bulk():
    print("%s is bulking.."% d.name)
d = Dog("lucky",4)

setattr(d,"talk",bulk)
setattr(d,"gender","M")
getattr(d,"talk")()
print(getattr(d,"gender"))

