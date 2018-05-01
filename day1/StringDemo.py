# Author: Charse
# py的string用法

name = "charse"

# 是不是以c开始
print(name.startswith("c"))
# 是不是以se开始
print(name.endswith("se"))
# str中是不是都是数字
print(name.isnumeric())
# 是否是主死
print("1A".isdecimal())
#  是否是整数
print("1A".isdigit())
# 判断是不是一个合法的标识符
print("a 1A".isidentifier())

# 进行拼接, 连接的方式是使用@  : 1@2@3@4@5
print("@".join(['1', '2', '3', '4', '5']))
# 字母转换成小写
print("ALEX".lower())
# 字母转换成大写
print("alex".upper())

# 使用l作为分隔符
print("alex".split('l'))
# 首字母大写
print("alex".capitalize())
# 大学全部变小写
print("AleX".casefold())
# 查找A, 找到返回其索引, 找不到返回-1
print("alex".find('l'))

msg = "my name is {}, and age is {}"
print(msg.format("chasrs", 22))

msg = "My Name Ss {name}, And Age Is {Age}"
# print(msg.fromat_map({'name': 'alex', 'age': 22}))
# 字符串中的大小写互换
print(msg.swapcase())
