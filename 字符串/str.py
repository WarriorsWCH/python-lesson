mystr = 'Software Engineer working primarily with Node.js, GraphQL, and mobile apps.'
print(mystr)

# 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
index = mystr.find('apps')
print(index)

index = mystr.find('with', 4, len(mystr))
print(index)

index = mystr.find('love')
print(index)

# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
index = mystr.index('apps')
print(index)

# 返回 str在start和end之间 在 mystr里面出现的次数
index = mystr.count('w')
print(index)

index = mystr.count('abc')
print(index)

# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
newstr = mystr.replace('w','W')
print(newstr)

# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
strarr = mystr.split(' ')
print(strarr)

# 把字符串的第一个字符大写
newstr = mystr.capitalize()
print(newstr)

# 把字符串的每个单词首字母大写
newstr = mystr.title()
print(newstr)

# 检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
newb = mystr.startswith('Soft')
print(newb)

# 检查字符串是否以obj结束，如果是返回True,否则返回 False.
newb = mystr.endswith('apps.')
print(newb)

# 转换 mystr 中所有大写字符为小写
newstr = mystr.lower()
print(newstr)

# 转换 mystr 中的小写字母为大写
newstr = mystr.upper()
print(newstr)

# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
newstr = mystr.ljust(200)
print(newstr)

# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
newstr = mystr.rjust(200)
print(newstr)

# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
newstr = mystr.center(100)
print(newstr)

# 删除 mystr 左边的空白字符
newstr = mystr.lstrip()
print(newstr)

# 删除 mystr 字符串末尾的空白字符
newstr = mystr.rstrip()
print(newstr)

# 删除mystr字符串两端的空白字符
newstr = mystr.strip()
print(newstr)

# 类似于 find()函数，不过是从右边开始查找.
index = mystr.rfind('app')
print(index)

# 类似于 index()，不过是从右边开始.
index = mystr.rindex('app')
print(index)

# 把mystr以str分割成三部分,str前，str和str后
strarr = mystr.partition('working')
print(strarr)

# 类似于 partition()函数,不过是从右边开始.
strarr = mystr.rpartition('working')
print(strarr)

# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
newb = mystr.isalpha()
print(newb)

# 如果 mystr 只包含数字则返回 True 否则返回 False.
newb = mystr.isdigit()
print(newb)

# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
newb = mystr.isalnum()
print(newb)

# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
newb = mystr.isspace()
print(newb)

mystr = 'abcd'
# 字符串重复 - 字符串乘以数字
newstr = mystr*3
print(newstr)
# 字符串拼接 - 字符串相加
newstr = mystr + mystr
print(newstr)

# 切片
print(mystr[0:2])
print(mystr[0:4:2])
print(mystr[-2])