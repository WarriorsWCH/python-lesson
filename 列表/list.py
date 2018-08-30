namesList = ['c', 'c++', 'java', 'js', 'go']
for name in namesList:
    print(name)

# 通过append可以向列表添加元素
namesList.append('c#')
print(namesList)

# 通过extend可以将另一个集合中的元素逐一添加到列表中
namesList.extend(['1','2',3])
print(namesList)

# insert(index, object) 在指定位置index前插入元素
namesList.insert(3, 'MM')
print(namesList)


# index和count与字符串中的用法相同
index = namesList.index('1')
print(index)
index = namesList.index('MM', 1, 5)
print(index)

# del：根据下标进行删除
del namesList[1]
print(namesList)

# pop：删除最后一个元素
namesList.pop()
print(namesList)

# remove：根据元素的值进行删除
namesList.remove('1')
print(namesList)

a = [1, 4, 2, 3]

# reverse方法是将list逆置。
a.reverse()
print(a)

# sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
a.sort()
print(a)
a.sort(reverse=True)
print(a)