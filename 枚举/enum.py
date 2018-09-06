from enum import Enum
from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    # ValueError: duplicate values found in <enum 'VIP'>: GREEN -> YELLOW
    # GREEN = 1
    # unique 数据相同会报错
     
    BLACK = 3
    RED = 4

print(VIP.BLACK)
# raise AttributeError('Cannot reassign members.')
# VIP.YELLOW = 10
# 枚举值不可改变

# 枚举的名字
print(VIP.BLACK.name)

# 枚举可以遍历
for v in VIP:
    print(v)

# ypeError: '>' not supported between instances of 'VIP' and 'VIP'
# r = VIP.GREEN > VIP.BLACK
# 枚举不能比较大小

# 可以身份比较
r = VIP.GREEN is VIP.BLACK
print(r)

# 可以 == 比较
r = VIP.GREEN == VIP.BLACK
print(r)

a = 1
# 把数据转成枚举
print(VIP(1))
# 代码可读性好
if VIP(1)==VIP.YELLOW:
    print(1)
if a==1:
    print(True)
