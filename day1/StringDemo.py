# Author: Charse
# py的string用法

name = "charse"

# 是不是以c开始
print(name.startswith("c"))
# 是不是以se开始
print(name.endswith("se"))
# str中是不是都是数字
print(name.isnumeric())
# 是否是小数
print("1A".isdecimal())
#  是否是整数
print("1A".isdigit())
# 判断是不是一个合法的标识符: 是不是一个合法的变量名
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
# 大写全部变小写
print("AleX".casefold())
# 查找A, 找到返回其索引, 找不到返回-1
print("alex".find('l'))

msg = "my name is {}, and age is {}"
print(msg.format("chasrs", 22))

msg = "My Name Ss {name}, And Age Is {age}"
print(msg.format_map({'name': 'alex', 'age': 22}))

# 是否是阿拉伯字符
print("'ab23'.isalnum()", 'ab23'.isalnum())

# 字符串中的大小写互换
print(msg.swapcase())

# 使用+ 连接 1, 2, 3, ==> 1+2+3
print("+".join(["1", "2", "3"]), "+".join(["1", "2", "3"]))

# 将第一个l 替换成大写的 L
print("alex li".replace('l', "L", 1))

# 寻找照最后的 l 的下标
print("alex lil".rfind('l'))

# 后面不足的用* 进行替换
print("name.ljust(50, "'*'")", name.ljust(50, "*"))

# 前面不足的用- 进行替换
print("name.rjust(50, "'-'")", name.rjust(50, "-"))

# 使用+进行切分  1, 2, 3, 4
print('1+2+3+4'.split('+'))

# 将每个字符的首个字母进行大写
print('lex li'.title())

# 使用0 进行填补
print('lex li'.zfill(50))

p = str.maketrans("abcdefli",'123$@456')

# 根据指定的匹配模式进行替换(翻译)
print("alex li".translate(p) )


