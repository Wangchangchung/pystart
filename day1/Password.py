# Author:chares.wang
# Python 密码输入

import getpass

name = input("username:")

# 注意：在pycharm是不能使用getpass的,但是在py的shell是可能够使用
password = getpass.getpass("password:")

print("username:", name, "password", password)

