import random
import math
import sys

def d(p, q):
    return (p[0] - q[0])*(p[0] - q[0]) + (p[1] - q[1])*(p[1] - q[1])

def Naive_pair(P):
    min_d = d(P[0], P[1])
    min_i = 0
    min_j = 1
    for i in range(len(P) - 1):
        for j in range(i + 1, len(P)):
            cur_d = d(P[i], P[j])
            if cur_d < min_d:
                min_d = cur_d
                min_i = i
                min_j = j
    return P[min_i], P[min_j]

#Do not change the following code
random.seed(12345)
P = []
for i in range(int(sys.argv[1])):
    P.append((random.random(), random.random()))
    
p1, p2 = Naive_pair(P)
print(p1, p2, math.sqrt(d(p1, p2)))

