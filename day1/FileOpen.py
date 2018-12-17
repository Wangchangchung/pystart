# Author: Charse

# open之后是一个文件句柄 默认的打开文件的模式是读模式,
# w指定写模式之后就不能进行读  w 是重新创建一个新文件,如果存在了一个已经有的文件,那么会进行覆盖的.如果是不存在的文件名,将会创建

# r指定读模式之后就不能进行写, 否则会报错

# data = open("yesterday", encoding="utf-8").read();

f = open("file/yesterday.txt", mode='r', encoding="utf-8")
# 默认读取的是所有

# f.tell() 返回读取的字符数量
print(f.tell())
data = f.read(2)
print("f.read(2):", data)
print(f.tell())  # 2

# 重新设置到文件指正tell的哪个位置,一般seek 和tell是同时使用的
# 那么f.read() 读取的就是所有的了
f.seek(0)
data = f.read()

# 返回文件的编码
print("f.encoding", f.encoding)

# 返回文件句柄的编号
print("f.fileno():", f.fileno())

# flush 将写入的数据,从缓冲区中写入到文件中
# 截断文件: 从头开始截取, 到第5个字符

f3 = open("file/yesterday.txt", mode='a', encoding="utf-8")
# 下面的 data输出的将是截断后的 只剩5个字符的hello
print("f3.truncate(5)", f3.truncate(5))


data2 = f.read()


# f = open("yesterday2",'r+',encoding="utf-8") #文件句柄 读写
# f = open("yesterday2",'w+',encoding="utf-8") #文件句柄 写读
# f = open("yesterday2",'a+',encoding="utf-8") #文件句柄 追加读写
f4 = open("file/yesterday2", 'wb')  # 文件句柄  二进制文件, 如果你处理的是一个二进制文件,或者你需要处理的是
# 网络请求数据,那么最好是进行使用 wb  rb的形式
f4.write("hello binary\n".encode())
f4.close()

print("data1-----------")
print(data)
print("data2-----------")
# 第二次进行读的时候,文件指针已经在文件的末尾了,所以再次的read之后是空的
print(data2)


f2 = open("file/yesterday1.txt", mode='w', encoding="utf-8")
f2.write("我爱北京天安门,\n")
f2.write("好好学习,天天向上")

# f2.read()

# 如果时一个20G的文件那么你会咋恩

# f.readlines()返回的是一个元祖 List<String>, 每一个元素就是一行,所以我们可以进行遍历
# 但是这种方法时非常不好的,因为将文件的所有内容都加载在内存中
# 如果一个20G的文件,还会采用这样的方法进行读取吗?

'''
# 低效的读取方式
for index, line in enumerate(f.readlines()):
    if index == 1:
        print("----分割线了------")
        continue
    print(line.strip())
'''

# 读取大文件的时候,我们可以选择只加载一行文件内容到内存中那么.这样读取大文件,就不会消耗太多的内存空间

# 比较高效的读取方式
for line in f:
    # 这样的方式读取,每次加载的时候,只加载文件的一行内容.
    print(line)

# 文件关闭
f.close()
f2.close()