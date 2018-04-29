# Author: Charse
# Python 用户交互输入输出


name = input("name:")
age = int(input("age:"))

# 格式化  字符串拼接是性能最差

# 格式化1
info = '''
------------ info of %s
name: %s
age: %d
''' %(name, int(age))


# 格式化2
info1 = '''
-------- list of {_name}
name:{_name}
age:{_age}
'''.format(_name=name, _age=age)

# 格式化3

info2 = '''
-------- list of {0}
name:{1}
age:{2}
'''.format(name, name, age)

print(info)
print(info1)
print(info2)
