
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


# stu1.__id = '00001'
# print(stu1.__id)
# print(stu1.__dict__)

# stu2 = Stu('dahu', 58)
# stu2.__id = '00002'
# print(stu2.__id)
# print(stu2.__dict__)
del stu1