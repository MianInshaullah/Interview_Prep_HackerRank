#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    s = 1
    gw = len(grid[0])
    gh = len(grid)
    tmpGrid= [list(x) for x in grid]
    bombs = []
    even=True
    allRes=[]
    if n==1 : return grid
    if n%2 == 0: return ["O"*gw] *gh
    while (True):
        s += 1
        if even:
            bombs.clear()
            for x in range(gh):
                nO= tmpGrid[x].count("O")
                for i in range(nO):
                    ind= tmpGrid[x].index("O")
                    tmpGrid[x][ind]="1"
                    bombs.append([x,ind])
                tmpGrid[x]= ["O"]*gw
            even=False
        else:
            for c in bombs:
                row= c[0]
                column=c[1]
                tmpGrid[row][column] ="."
                if column-1 >= 0:
                    tmpGrid[row][column-1] = "."
                if column+1 < gw:
                    tmpGrid[row][column+1] = "."
                if row-1 > -1:
                    tmpGrid[row -1][column] = "."
                if row+1 < gh:
                    tmpGrid[row+1][column] = "."
            even=True
            result = ["".join(xx) for xx in tmpGrid]
            if allRes.count(result) :
                break
            else:
                allRes.append(result)
    rint= n % 4
    if rint >1 : rint=0
    else: rint=1
    return allRes[rint]
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
