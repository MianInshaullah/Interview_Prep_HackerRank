#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

from itertools import accumulate, filterfalse
def solve(arr):
    res = []
    all_s = list(accumulate(arr))
    max_s = all_s[-1]
    for s in all_s:
        q, r = divmod(max_s, s)
        if r == 0 and len(set(filterfalse(lambda x: x%s, all_s))) == q:
            res.append(s)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
