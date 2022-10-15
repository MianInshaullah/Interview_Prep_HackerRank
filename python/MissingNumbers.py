#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(a, c):
    # Write your code here
    a.sort()
    c.sort()
    ac = Counter(a)
    cc = Counter(c)
    res =[]



    for key, val in cc.items():
        print("Key: "+str(key)+" val: "+str(val))
        if (key not in a) or (key in ac and ac[key]!=val):
            res.append(key)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
