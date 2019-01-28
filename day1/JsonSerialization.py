# Author: Charse

import pickle

def sayhi(name):
    print("hello2", name)

f = open("test.txt", "rb")

data = pickle.loads(f.read())

print(data["func"]('Alex'))
