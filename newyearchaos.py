#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
def swap_round(q):
    n = len(q)
    n_bribes = 0
    for i in range(n-1, 0, -1):
        if q[i] < q[i-1]:
            q[i], q[i-1] = q[i-1], q[i]
            n_bribes += 1
    return n_bribes
    

def minimumBribes(q):
    n = len(q)
    out = swap_round(q) + swap_round(q)
    if q != sorted(q):
        print("Too chaotic")
    else:
        print(out)
    
        
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
