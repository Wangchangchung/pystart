# Author: Charse

# 函数全局变量和局部变量

name = "charse"

#def changeName(age=10, address, name):
# 上面定义函数, 非默认参数不能在默认参数的后面





def changeName(address, age=10):
    print(name +'dddd') # SyntaxWarning: name 'name' is used prior to global declaration 在全局变量声明之前使用最好时不要使用
    # 要么在这之前就声明name是全局的, 要么就重新申明一个名称不一样的变量
    global name
    name = "hello"
    print(age, name, address)


def defaultAge(address, name, age=10):
    print(age, name, address)

defaultAge('beijing', 'linux', 20)
defaultAge('beijing', 'linux')


changeName('beijing', 30)
print(name)


