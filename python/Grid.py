#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    n, m = len(grid), len(grid[0])
    tgrid = [[0 for i in range(n)] for j in range(m)]
    i = 0
    for g in grid:
        j = 0
        for c in sorted(g):
            tgrid[j][i] = c 
            if i > 0 and tgrid[j][i] < tgrid[j][i-1]:
                return "NO"
            j += 1
        i += 1
    # print(tgrid)
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
