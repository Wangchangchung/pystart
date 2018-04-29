# Author: Charse

# Py while 的使用

old_age = 50

count = 0
while count <= 4:
    guess = int(input("guess age:"))
    if guess == old_age:
        print("yes you are right")
        # 猜对了就跳出循环
        break
    elif guess > old_age:
        print("no bigeer")
    else:
        print("no samller")
    count += 1
    print(count)
#  如果 count <= 4 那么就执行这里的方法
else:
    print("you have fail, fuck off !")
