# Author: Charse

import sys
# 系统默认的编码格式
print(sys.getdefaultencoding())

s = "我是中文字符"
print(s.encode("gbk"))

print(s.encode("utf-8"))

# s.encode("utf-8") : 转换成Unicode, 带上"utf-8"表示的是告诉unicode, 我是从什么转换而来的
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))
# 如果encode是gb2312,但是解码是用utf-8解码的,那么将会出现异常
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("utf-8"))
