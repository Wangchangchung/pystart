# Author: Charse
# py 列表的使用

import copy


name = ["111", "222", "333", "444", "555"]

# 从列表中取得元素
print(name[0], name[2]) # 111 333
print(name[1:3])  # 切片 ['222', '333']
print(name[:3])   # ['111', '222', '333']  与下标从0开始是一样的
print(name[0:3])  # ['111', '222', '333']
print(name[-2:])  # ['444', '555']    与name

# 往列表中添加元素
name.append("666")  # 直接在末尾添加
name.insert(1, "999")        # 在指定位置插入 : 将999插入到下标为1的位置, 原来位置中元素就直接往后顺延
print(name)

# 修改列表中元素
name[0] = "000"
print(name)

# 删除元素
name.pop()  # 默认是删除最后一个下标
print(name)
name.pop(2)
print(name)

# 取出指定元素的下标
print(name.index("999"))

# 反转 改变的是分组里面的元素
name.reverse()
print(name)

# 特殊字符, 数字, 大写字母, 小写字母排序. 改变的是数组中的元素
name.sort()
print(name)

# name.clear()  remove all items 删除所有的元素

# 复制列表
name2 = name.copy()   # 这个是浅copy,如果列表中还有列表,列表的中元素修改了,新的中也同样是修改了
print(name2)
name[1] = "xxx"  # name2中是不会进行修改的

names = ["1", [1, 2], "2"]

names[1][0] = 9
print(names)

names1 = copy.copy(names)  # 这个是浅copy,与列表的copy是一样的.
# 进行深copy
names2 = copy.deepcopy(names)

# 对列表的元素进行修改,两者是同样的被修改
# names2 元素内的列表是不会被修改的
names[1][1] = 3

print(names)
print(names1)
print(names2)

# 遍历列表
for i in names2:
    print(i)

'''
深浅copy


'''








