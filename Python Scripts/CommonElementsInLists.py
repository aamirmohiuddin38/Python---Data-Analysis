import numpy as np
import random

#List1
l1 = list(range(100))
random.shuffle(l1)

#List2
l2 = list(range(50))
random.shuffle(l2)

#Check for Intersection : Time Complexity O(n*m)
cnt = 0
for ele in l1:
    for e in l2:
        if ele == e:
            print(ele)
            cnt += 1

print('{} elements found common'.format(cnt))


