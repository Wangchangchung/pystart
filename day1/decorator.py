# Author: Charse

# 装饰器
import time

def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run tim is %s ' %(stop_time -start_time))
    return warpper

@timmer
def test1():
    time.sleep(3)
    print('in the test1')


test1()


## 函数即是变量

# 示范一
def bar():
    print("in the bar")

def foo():
    print("in the foo")
    bar()
foo()

# 示范二
def foo():
    print("in the foo")
    bar()
def bar():
    print("in the bar")
foo()

# 示范三
'''
def foo1():
    print("in the foo1")
    bar()
foo1()
def bar():
    print("in the bar")

'''
# 这种将会出现异常.






def bar():
    time.sleep(3)
    print("in the bar")



def test2(func):
    print(func)
    return func

bar = test2(bar)
print(bar)
bar()  # 运行bar 函数

# 函数嵌套

def foo():
    print('in the foo--')
    def bar():
        print('in the bar--')
    # 在函数里面定义的函数,只能在函数里面进行使用
    bar()

# 执行foo()函数
foo()