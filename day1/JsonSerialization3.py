# Author: Charse

import json

def sayhi(name):
    print("hellio", name)

info = {
    'name':'demo',
    'age':22,
    #'func':sayhi  json不可以序列函数
}
f = open("text.txt",'w')

# TypeError: <function sayhi at 0x7f81156c1f28> is not JSON serializable
f.write(json.dumps(info))

info['age'] = 21
f.write(json.dumps(info))

f.close()
