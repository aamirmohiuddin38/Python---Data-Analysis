import numpy as np
import random

#List1
l1 = list(np.arange(100))
random.shuffle(l1)

#List2
l2 = list(np.arange(50))
random.shuffle(l2)

# Time complexity: O(n+m)
# Add all elements in the smallest list into hashtable/dict: O(m) Space
smallListDict = {}
for ele in l2:
    smallListDict[ele] = 1 #value can be anything, but Key is imp

#Now finding common
count = 0
for e in l1:
    if smallListDict.get(e) != None: #here search happens in constant time
        print(e)
        count += 1

print('{} elements found Common'.format(count))