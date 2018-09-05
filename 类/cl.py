
class Stu():
    # 类属性
    name = 'dawei'
    age = 20

    # 构造函数 需要传self 创建对象时自动调用
    def __init__(self, name, score):
        # 成员属性
        self.sex = 'fale'
        self.name = name
        # 将属性定义为私有属性，属性名前加__
        self.__score = score
        # 通过__class__访问类属性
        print(self.__class__.name)

    def setScore(self, score):
        if (score > 60):
            self.__score = score
        else:
            print('不及格')
    
    def getScore(self):
        return self.__score

    #类方法，用classmethod来进行修饰
    @classmethod
    def getAge(cls):
        return cls.age

    # 需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数
    @staticmethod
    def staticTest():
        print('静态方法')


    # 析构方法
    # 当对象被删除时，会自动调用
    def __del__(self):
        print('__del__方法被调用',self.name,'马上要狗带了')



# 创建对象
stu1 = Stu('xiaoming', 98)
print(stu1.name)
print(stu1.__class__.age)

# AttributeError: 'Stu' object has no attribute '__score'
# print(stu1.__score)

# __score私有变量被修改了名字为 _Stu__score，所以无法直接访问到
print(stu1.__dict__)
# {'sex': 'fale', 'name': 'xiaoming', '_Stu__score': 98}

# 通过方法访问私有变量（可以设置只读或者只写）
stu1.setScore(88)
print(stu1.getScore())
# 类属性的两种访问方式
print('类属性',Stu.age)
print('类属性',stu1.age)
#可以通过类对象引用
print('类方法',Stu.getAge())
#可以用过实例对象引用
print('类方法',stu1.getAge())

Stu.staticTest()

# stu1.__id = '00001'
# print(stu1.__id)
# print(stu1.__dict__)

# stu2 = Stu('dahu', 58)
# stu2.__id = '00002'
# print(stu2.__id)
# print(stu2.__dict__)
del stu1


class Animal(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def run(self):
        print('run fast')

    def __test(self):
        print('私有的')

class Dog(Animal):

    def dogTest(self):
        print('狗策')

dog1 = Dog('金毛', '黄色')
print(dog1.name)
dog1.run()
# AttributeError: 'Dog' object has no attribute '__test'
# dog1.__test()
# 私有的属性、方法，不会被子类继承


class A:
    def printA(self):
        print('------A------')

    def printTest(self):
        print('test a')

class B:
    def printB(self):
        print('------B------')

    def printTest(self):
        print('test b')

# 多继承
class C(A,B):
    def printC(self):
        print('-------C-----')

c1 = C()
c1.printA()
c1.printB()
# 父类中有相同的方法
c1.printTest() # test a

# __mro__可以查看C类的对象搜索方法时的先后顺序
print(C.__mro__)


class Cat:
    def __init__(self, name):
        self.name = name

class Jumao(Cat):
    def __init__(self, name ,age):
        self.age = age
        # 调用父类的__init__方法
        super().__init__(name)

cat1 = Jumao('doufu',5)
print(cat1.name,cat1.age)