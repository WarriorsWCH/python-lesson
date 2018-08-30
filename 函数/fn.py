# 定义函数 参数 返回值 可以返回多个值
def fn(a, b):
    a = a + b
    b = a*3
    return a,b

# 解构
a1,b1 = fn(2,3)
print(a1,b1)
# 返回值是元组
arr = fn(4,5)
print(arr)

# 带有默认值的参数一定要位于参数列表的最后面。
def printinfo(name, age=20):
    print(name,age)

printinfo('han')

# 不定长参数
# 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；
# 而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。
def fun(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

fun(1,2,3,4,5,m='a')

# 匿名函数
# Lambda函数能接收任何数量的参数但只能返回一个表达式的值
# 匿名函数不能直接调用print，因为lambda需要一个表达式
sum = lambda arg1,arg2:arg1+arg2
print(sum(10,20))

stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19}, 
    {"name":"wangwu", "age":17}
]

stus.sort(key = lambda x:x['age'])
print(stus)