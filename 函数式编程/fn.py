
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x


# 映射 对list_x中的每个元素执行square函数
r = map(square, list_x)
print(list(r))
# [1, 4, 9, 16, 25, 36, 49, 64]

list_y = [1, 2, 3, 4, 5]
r = map(lambda x, y: x*x + y, list_x, list_y)
print(list(r))
# [2, 6, 12, 20, 30]


from functools import reduce
# 连续计算，连续调用lambda
r = reduce(lambda x,y: x+y, list_x)
print(r)
# 36

list_x = ['1', '2','3', '4', '5', '6' '7', '8']
r = reduce(lambda x,y: x+y, list_x, 'start')
print(r)



# 装饰器
# 对修改是封闭的，对扩展是开放的

import time

def f1():
    print('f1')

def f2():
    print('f2')

def print_time(func):
    print(time.time())
    func()

print_time(f1)

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

# f = decorator(f1)
# f()

# 语法糖 装饰器
@decorator
def f3():
    print('f3')
# 调用还是f3
f3()