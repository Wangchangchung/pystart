# Author: Charse
# py 字典操作

'''
1. 字典 天生是无序的
2. 字段 是不能重复的
3.
'''

info = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4',
    'key5': 'value5',
}

print(info)
print(info['key1'])

# key存在,修改
info['key1'] = "new value"

# key不存在,添加
info['key4'] = 'hello world'

# 删除
del info['key5']

# 标准删除:删除指定元素
info.pop("key4")

# 随机删除
info.popitem()
print(info)

# 如果查找的时候不存在key 那么是会报错的 inf['key]

# 安全的获取方式是: get
print("info.get('ke')", info.get('ke'))

# 查看key是否存在info字典中  #print('stu1103' in info) #info.has_key("1103") in py2.x 在2中是使用的has_key进行的.
print('key' in info)

# 多层字典嵌套及操作


# 循环字典
# 方法一
for keys in info:
    print(keys, info[keys])

# 方法二  会先把dict转成list 数据大时不要使用
for k, v in info.items():
    print(k,v)



