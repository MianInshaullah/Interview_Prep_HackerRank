#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isFibo' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def isFibo(n):
    # Write your code here
    fib = []
    a = 1
    b = 0
    c = 0


    while c < 10**10:
        fib.append(c)
        c = a+b
        a = b
        b = c


    if n in fib:
        return("IsFibo")
    else: 
        return("IsNotFibo")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = isFibo(n)

        fptr.write(result + '\n')

    fptr.close()
