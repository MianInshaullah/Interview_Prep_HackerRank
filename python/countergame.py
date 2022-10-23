#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    cnt = 0
    if (n == 1): return 'Richard'
    while (n > 1):
        if (int(math.log(n,2)) == math.log(n,2)):
            cnt += 1
            n = n / 2
        else:
            cnt += 1
            n -= 2 ** int(math.log(n,2))
    return 'Louise' if cnt%2 == 1 else 'Richard'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
