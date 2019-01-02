# Author: Charse
# 函数
def func1():
    """testing1"""
    print('in the func1')
    return 0


# 过程
def func2():
    '''testing2'''
    print('in the func2')


x = func1()
y = func2()

print('from func1 return is %s' % x)

# 没有返回值时None
print('from func2 return is %s' % y)


def test1():
    pass

def test2():
    return 0

def test3():
    return 0, 'hello', ['a', 'b', 'c'], {'name', 'alex'}

x = test1()
y = test2()
z = test3()
# None
print(x)
# 0
print(y)
# 输出一个元组 (0, 'hello', ['a', 'b', 'c'], {'name', 'alex'})
print(z)

def test4(x, y, z):
  print(x)
  print(y)
  print(z)

# 实参与形参一一对应
test4(1, 2, 3)
# 通过形参的指定,那么实参入参的时候,就没有顺序
test4(x=1, y=2, z=3)
# 通过形参指定,必须在实参的后面  否则会报出错误的: 位置参数在关键字参数之后"positional argument follows keyword argument"
#test4(z=3, 1, 2)positional argument follows keyword argument
#test4(1,x=1, y=2) test4() got multiple values for argument 'x'
test4(1, z=2, y=0)
test4(1, z=2, y=0)




