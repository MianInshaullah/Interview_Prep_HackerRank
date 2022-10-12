#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(a):
    # Write your code here
    a.sort()
    d = {}
    l = []

    for i in range(len(a)-1):
        d[a[i],a[i+1]] = a[i+1] - a[i]
        

    for i,j in d.keys():
        if d[i,j]==min(d.values()):
            l.append(i)
            l.append(j)
    return (l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
