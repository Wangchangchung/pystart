# Author: Charse


# 高阶函数 + 函数嵌套 ==> 装饰器

import time

def tim(func):  # tim(hell1) func=hell1
    def deco():
        start_time = time.time()
        func() # 在这里实际执行的时 hell1
        stop_time = time.time();
        print("run time %s" % (stop_time - start_time))
    return deco

def timer(func):
    # 函数嵌套
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time();
        print("run time %s" %(stop_time-start_time))

    return deco  # 高阶函数


def hell1():
    print("hello 1")

#直接调用timer()

# 返回的时deco函数的内存地址
hell1 = tim(hell1)
# 这里实际执行的时 deco函数,而不是上面定义的hell1
hell1()  # deco

# @ + 装饰器的名称  等价于-->  test1=timer(test1)
@timer
def test1():
    time.sleep(3)
    print("in the test1")

@timer
def test2(name, age):
    print("test2:",name, age)

test1() # 这实际执行的时deco的代码了
test2('alex', 2)
