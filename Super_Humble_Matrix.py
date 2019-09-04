#!/bin/python3

import os
import sys
import math
# Complete the solve function below.
def solve(n, m):
    lis_l = [0] * (n+m)
    counter = 1
    for i in range(n):
        for j in range(m):
            lis_l[i+j]+=1
    for i in lis_l:
        counter *= math.factorial(i)
    return counter%(10**9+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
