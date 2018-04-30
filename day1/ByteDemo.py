# Author: Charse
# py byte的使用
# 在2.x 的版本中string类型和byte是没有很明显的区分
# 但是在 3.x 的版本中string可以encode编码成二进制, 也可以decode解码成其他的进制

name = "这个是一个字符串"

print(name.encode("utf-8"))
print(name.encode("utf-8").decode())
