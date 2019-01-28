# Author: Charse

import pickle

def sayhei(name):
    print("hello2", 'rb')

f = open('text.txt', 'rb')

data = pickle.loads(f.read())

print(data['func']('alex'))


