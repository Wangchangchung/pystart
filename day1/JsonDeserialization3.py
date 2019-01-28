# Author: Charse

import json

# data = json.loads(f.read()) # data = pickle.loads(f.read())

f = open('text.txt', 'r')

for line in f:
    print(json.loads(line))

