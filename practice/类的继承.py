class People(object):
    role = "students"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s is eating..."% self.name)
    def get_age(self):
        print("%s is %s years old..."% self.name,self.age)
    def sleep(self):
        print("%s is sleeping" % self.name)

class Relation(object):
    def makeFriends(self,obj):
        print("%s is making friends with %s "% (self.name,obj.name))

#多类继承
class Man(People,Relation):
    #继承父类的属性和方法
    def __init__(self,name,age,money):
        # 继承父类的属性
        People.__init__(self,name,age)
        #super(Man, self).__init__(name, age) 跟上面这句作用一模一样
        #声明自己的属性
        self.money = money
        print("%s has %s money when he was born .."%(self.name,self.money))
    def sleep(self):
        #调用父类的方法
        People.sleep(self)
        People.eat(self)
    #重构父类中的方法
    def get_age(self):
        print("my age is %s"% self.age)
m1 = Man("wangdamai",22,200)
m2 = Man("wangxiaomai",12,100)
m1.makeFriends(m2)
m1.sleep()
m1.get_age()


#多态
class Animal(object):
    def __init__(self,name):
        self.name = name
    @staticmethod
    def animal_talk(obj):
        obj.talk()
class Dog(Animal):
    def talk(self):
        print("wang!")
class Cat(Animal):
    def talk(self):
        print("meow!")

d = Dog("zhangsan")
c = Cat("lisi")
Animal.animal_talk(d)
Animal.animal_talk(c)