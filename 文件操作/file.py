
# open(文件名，访问模式)
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
f = open('./test.txt', 'w')
print(f)

# 使用write()可以完成向文件写入数据
f.write('abcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg\nabcdefg')
# 关闭文件
f.close

f = open('./test.txt', 'r')
# 使用read(num)可以从文件中读取数据，num表示要从文件中读取的数据的长度（单位是字节），
# 如果没有传入num，那么就表示读取文件中所有的数据
content = f.read(5)
print(content)
content = f.read()
print(content)
f.close()

# 就像read没有参数时一样，readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
f = open('./test.txt', 'r')
content = f.readlines()
print(content)
f.close()

f = open('./test.txt','r')
content = f.readline()
print(content)
f.close()

f = open('./test.txt', 'r')
content = f.read(5)
# 在读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取
position = f.tell()
print(position)
content = f.read(3)
position = f.tell()
print(position)
f.close()


f = open('./test.txt', 'r')
content = f.read(20)
position = f.tell()
print(content,position)
# 如果在读写文件的过程中，需要从另外一个位置进行操作的话，可以使用seek()
# seek(offset, from)有2个参数
# offset:偏移量 from:方向
# 0:表示文件开头
# 1:表示当前位置
# 2:表示文件末尾
f.seek(5,0)
position = f.tell()
print(position)
f.close()


import os
# 文件重命名
os.rename('test.txt', 'rename.txt')
# 删除文件
os.remove('rename.txt')
# 创建文件夹 文件存在会报错
# os.mkdir('Test')
# 获取当前目录
print(os.getcwd())
# 改变默认目录
# os.chdir('../')
# 获取目录列表
print(os.listdir('./'))
# 删除文件夹
os.rmdir('Test')
