# Author: Charse

# 为了避免打开文件后忘记关闭,可以通过管理上下文 with
with open("file/yesterday.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)


# 在python 2.7 之后 with 又支持同时对多个文件的上下文进行管理.
with open("file/yesterday.txt", "r", encoding="utf-8") as f, \
     open("file/yesterday2", "r", encoding="utf-8") as f2:
    for line in f:
        print(line)

