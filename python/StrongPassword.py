#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    password = password.strip()
    chars = f"[!@#$%^&*()\-+]"
    numbers = f"[0-9]"
    lower_case = f"[a-z]"
    upper_case = f"[A-Z]"
    min_chars = 0
    
    if re.search(chars,password) == None:
        min_chars += 1 
    if re.search(lower_case,password) == None:
        min_chars += 1
    if re.search(upper_case,password) == None:
        min_chars += 1
    if re.search(numbers,password) == None:
        min_chars += 1
        
    return(max(min_chars, 6-len(password)) if len(password) < 6 else min_chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
