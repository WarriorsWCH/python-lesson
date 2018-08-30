info = {'name':'li', 'id':100, 'sex':'f', 'address':'english'}

# 修改元素
info['id'] = 50
print(info)

# 添加新的元素
info['age'] = 23
print(info)

# del删除指定的元素
del info['sex']
print(info)

# clear清空整个字典
info.clear()
print(info)


info = {'name':'li', 'id':100, 'sex':'f', 'address':'english'}

# 键值对的个数
print(len(info))
# 返回一个包含字典所有KEY的列表
print(info.keys())
# 返回一个包含字典所有value的列表
print(info.values())
# 返回一个包含所有（键，值）元组的列表
print(info.items())

for key,value in info.items():
    print(key,value)


print('name' in info)
print('li' in info)
print('li' not in info)