# Author: Charse
# py  调用系统命令

import os
import sys

# 打印系统变量
print(sys.path)

print(sys.argv, "1", "2", "3")
print(sys.argv[0])

# 执行命令,不保存结果
cmd_res = os.system("dir")

cmd = os.popen("dir").read()

# os.mkdir("new_dir"), 新建立一个文件价
print("----->", cmd_res)

print("=====>", cmd)
