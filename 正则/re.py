import re

a = "Xi said the people of the DPRK have attained remarkable achievements in the cause of socialist revolution and construction over the past 70 years."

r = re.findall('the', a)
print(r)

# .	匹配任意1个字符（除了\n）
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# \S	匹配非空白
# \w	匹配单词字符，即a-z、A-Z、0-9、_
# \W	匹配非单词字符
r = re.findall('\d', a)
print(r)

# *	匹配前一个字符出现0次或者无限次，即可有可无
# +	匹配前一个字符出现1次或者无限次，即至少有1次
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m}	匹配前一个字符出现m次
# {m,}	匹配前一个字符至少出现m次
# {m,n}	匹配前一个字符出现从m到n次

a = 'python123java456ios999'
r = re.findall('[a-z]{3,6}',a)
# 默认是贪婪模式
print(r)
# ['python', 'java', 'ios']
r = re.findall('[a-z]{3,6}?',a)
print(r)
# ['pyt', 'hon', 'jav', 'ios']

a = 'pytho0python1pythonn2'
r = re.findall('python', a)
print(r)
r = re.findall('python*', a)
print(r)
# ['pytho', 'python', 'pythonn']
r = re.findall('python?',a)
print(r)
# ['pytho', 'python', 'python']
r = re.findall('python{1,2}',a)
print(r)
# ['python', 'pythonn'] 贪婪
r = re.findall('python{1,2}?',a)
print(r)
# ['python', 'python'] 非贪婪

# ^	匹配字符串开头
# $	匹配字符串结尾
# \b	匹配一个单词的边界
# \B	匹配非单词边界
a = 'xiaoWang@163.com'
r = re.match('[\w]{4,20}@163\.com', a)
print(r.group())

a = 'xiaoWang@163.comheihei'
r = re.match('[\w]{4,20}@163\.com', a)
print(r.group())

r = re.findall('[\w]{4,20}@163\.com$', a)
print(r)

# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

a = 'pythonpythonpythonpythonpythonpython'
r = re.findall('(python){3}',a)
# []中式|或关系 ()里是&且关系
print(r)

a = 'pythonC#\njavajs'
# re.I忽略大小写 re.S匹配空
r = re.findall('c#.{1}', a, re.I | re.S)
print(r)

a = 'pythonC#javajsC#'
r = re.sub('C#', 'go', a)
print(r)


def covert(value):
    rep = value.group()
    return '!!' + rep + '!!'
# 动态替换
r = re.sub('C#', covert, a)
print(r)


def fn(value):
    rep = value.group()
    if int(rep) >= 6:
        return '9'
    else:
        return '0'
a = 'ABC3218DF93J5'
r = re.sub('\d', fn, a)
print(r)
