
a = 10

def f1(x):
    return a * x * x

print(f1(2))

# 闭包 = 函数 + 环境变量
def curve_pre():
    a = 25
    def curve(x):
        return a * x * x
    return curve

# 如果curve_pre函数内部没有局部变量a，那a=30会改变f2(2)的结果
a = 30
f = curve_pre()
print(f(2))
print(f.__closure__)
# (<cell at 0x106c439d8: int object at 0x1069cf320>,)
print(f.__closure__[0].cell_contents)
# 25

def f2():
    a = 10
    def fn(x):
        a = 20
    return fn
f = f2()
print(f.__closure__)
# None 这个函数不是闭包


def f3():
    a = 20
    def fn(x):
        x =  a * x
    return fn
f = f3()
print(f.__closure__)
# 是闭包


# 非闭包
origin = 0
def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos
    return origin

print(go(2))
print(go(3))
print(go(6))


origin = 0

def factory(pos):
    def go(step):
        # 不是本地局部变量
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go

tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(6))