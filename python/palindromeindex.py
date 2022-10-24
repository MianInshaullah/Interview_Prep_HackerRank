#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    rev = s[::-1]
    lst = list(s)
    revlst = list(rev)
    if (rev == s):
        return -1
    else:
        for c,v in enumerate(s):
            if v != rev[c]:
                lst.pop(c)
                revlst.pop(c)
                if (lst != lst[::-1]):
                    return (len(s)-c-1)
                if (revlst != revlst[::-1]):
                    return (c)
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
