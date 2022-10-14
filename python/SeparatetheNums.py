#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    l = len(s)
    ls = []
    flag = 0
    for i in range(1,l//2+1):
        st = s[:i]
        temp = st
        count = 1
        while len(temp) < len(s):
            temp = temp + str(int(st)+count)
            count += 1
            if temp == s:
                print(f"YES {st}")
                flag = 1
                break
    if flag == 0:
        print("NO")
    
    return(s)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
